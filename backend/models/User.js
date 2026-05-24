const mongoose = require('mongoose');

const userSchema = new mongoose.Schema({
  name: { type: String, required: true },
  email: { type: String, required: true, unique: true },
  password: { type: String, required: true },
  phone: { type: String },
  address: { type: String },
  city: { type: String },
  registration_date: { type: Date, default: Date.now },
  adoptedPets: [{
    type: mongoose.Schema.Types.ObjectId,
    ref: 'Animal'
  }]
});

module.exports = mongoose.model('User', userSchema);
