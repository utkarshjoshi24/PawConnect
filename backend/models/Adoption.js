const mongoose = require('mongoose');

const adoptionSchema = new mongoose.Schema({
  user_id: { type: String, required: true },
  animal_id: { type: String, required: true },
  application_date: { type: Date, default: Date.now },
  status: { type: String, default: 'Pending' }, // Pending, Approved, Rejected
  approval_date: { type: Date },
  notes: { type: String }
});

module.exports = mongoose.model('Adoption', adoptionSchema);
