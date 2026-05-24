require('dotenv').config();
const mongoose = require('mongoose');
const Animal = require('../models/Animal');

const mockPets = [
  { name: 'Bella', species: 'Dog', breed: 'Labrador Retriever', age: 2, gender: 'Female', description: 'Very friendly and loves to play fetch.' },
  { name: 'Charlie', species: 'Dog', breed: 'Beagle', age: 4, gender: 'Male', description: 'Curious and always sniffing around.' },
  { name: 'Daisy', species: 'Dog', breed: 'Poodle', age: 1, gender: 'Female', description: 'Smart and highly energetic.' },
  { name: 'Milo', species: 'Cat', breed: 'Maine Coon', age: 3, gender: 'Male', description: 'Large, fluffy, and very gentle.' },
  { name: 'Leo', species: 'Cat', breed: 'British Shorthair', age: 2, gender: 'Male', description: 'Loves lounging by the window.' },
  { name: 'Chloe', species: 'Cat', breed: 'Ragdoll', age: 5, gender: 'Female', description: 'Affectionate and loves being held.' },
  { name: 'Rocky', species: 'Dog', breed: 'Bulldog', age: 3, gender: 'Male', description: 'Stubborn but incredibly sweet.' },
  { name: 'Zoe', species: 'Dog', breed: 'Shih Tzu', age: 6, gender: 'Female', description: 'A great lap dog, very calm.' },
  { name: 'Oliver', species: 'Cat', breed: 'Sphynx', age: 1, gender: 'Male', description: 'Needs a warm sweater but has a huge heart.' },
  { name: 'Kiwi', species: 'Bird', breed: 'Parakeet', age: 1, gender: 'Female', description: 'Chirps all day and loves mirrors.' },
  { name: 'Mango', species: 'Bird', breed: 'Cockatiel', age: 2, gender: 'Male', description: 'Whistles tunes and is very social.' },
  { name: 'Thumper', species: 'Rabbit', breed: 'Holland Lop', age: 1, gender: 'Male', description: 'Hops around joyfully and loves carrots.' },
  { name: 'Snowball', species: 'Rabbit', breed: 'Lionhead', age: 2, gender: 'Female', description: 'Fluffy mane and very timid at first.' },
  { name: 'Spike', species: 'Reptile', breed: 'Bearded Dragon', age: 4, gender: 'Male', description: 'Loves basking under the heat lamp.' },
  { name: 'Nemo', species: 'Fish', breed: 'Clownfish', age: 1, gender: 'Male', description: 'Active swimmer, needs a saltwater tank.' }
];

async function seedPets() {
  try {
    await mongoose.connect(process.env.MONGO_URI);
    console.log('Connected to MongoDB');

    const inserted = await Animal.insertMany(mockPets);
    console.log(`Successfully seeded ${inserted.length} new pets!`);
    
    process.exit(0);
  } catch (error) {
    console.error('Error seeding pets:', error);
    process.exit(1);
  }
}

seedPets();
