require('dotenv').config();
const mongoose = require('mongoose');
const fs = require('fs');
const path = require('path');
const csv = require('csv-parser');

const Animal = require('../models/Animal');
const User = require('../models/User');
const Adoption = require('../models/Adoption');
const Shelter = require('../models/Shelter');

const LEGACY_DIR = path.join(__dirname, '../../legacy');

async function migrate() {
  try {
    await mongoose.connect(process.env.MONGO_URI);
    console.log('Connected to MongoDB');

    // Clear existing data
    await Animal.deleteMany({});
    await User.deleteMany({});
    await Adoption.deleteMany({});
    await Shelter.deleteMany({});
    console.log('Cleared existing collections');

    // Migrate Users
    await migrateCSV('users.csv', User, (row) => ({
      name: row.name,
      email: row.email,
      password: row.password, // Ideally re-hash but we keep it for now
      phone: row.phone,
      address: row.address,
      city: row.city,
      registration_date: new Date(row.registration_date)
    }));
    console.log('Migrated Users');

    // Migrate Animals
    await migrateCSV('animals.csv', Animal, (row) => ({
      name: row.name,
      species: row.species,
      breed: row.breed,
      age: parseInt(row.age) || null,
      gender: row.gender,
      health_status: row.health_status,
      status: row.status,
      description: row.description,
      image_url: row.image_url,
      shelter_id: row.shelter_id,
      date_added: new Date(row.date_added)
    }));
    console.log('Migrated Animals');

    // Migrate Adoptions
    await migrateCSV('adoptions.csv', Adoption, (row) => ({
      user_id: row.user_id,
      animal_id: row.animal_id,
      application_date: new Date(row.application_date),
      status: row.status,
      approval_date: row.approval_date ? new Date(row.approval_date) : null,
      notes: row.notes
    }));
    console.log('Migrated Adoptions');

    // Migrate Shelters
    await migrateCSV('shelters.csv', Shelter, (row) => ({
      name: row.name,
      location: row.location,
      capacity: parseInt(row.capacity) || null,
      contact_phone: row.contact_phone,
      contact_email: row.contact_email
    }));
    console.log('Migrated Shelters');

    console.log('Migration Complete!');
    process.exit(0);
  } catch (error) {
    console.error('Migration failed:', error);
    process.exit(1);
  }
}

function migrateCSV(filename, Model, mapRow) {
  return new Promise((resolve, reject) => {
    const results = [];
    const filePath = path.join(LEGACY_DIR, filename);
    if (!fs.existsSync(filePath)) {
      console.log(`Skipping ${filename} (not found)`);
      return resolve();
    }
    
    fs.createReadStream(filePath)
      .pipe(csv())
      .on('data', (data) => {
        results.push(mapRow(data));
      })
      .on('end', async () => {
        if (results.length > 0) {
          await Model.insertMany(results);
        }
        resolve();
      })
      .on('error', (err) => reject(err));
  });
}

migrate();
