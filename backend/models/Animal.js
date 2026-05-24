const mongoose = require('mongoose');

const animalSchema = new mongoose.Schema({
  name: { type: String, required: true },
  species: { type: String, required: true },
  breed: { type: String },
  age: { type: Number },
  gender: { type: String },
  health_status: { type: String },
  status: { type: String, default: 'Available' },
  description: { type: String },
  image_url: { type: String },
  shelter_id: { type: String }, // keeping as string/number based on CSV for simplicity of migration
  date_added: { type: Date, default: Date.now }
});

module.exports = mongoose.model('Animal', animalSchema);
