const mongoose = require('mongoose');

const shelterSchema = new mongoose.Schema({
  name: { type: String, required: true },
  location: { type: String },
  capacity: { type: Number },
  contact_phone: { type: String },
  contact_email: { type: String }
});

module.exports = mongoose.model('Shelter', shelterSchema);
