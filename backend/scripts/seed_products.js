require('dotenv').config({ path: '../.env' });
const mongoose = require('mongoose');
const Product = require('../models/Product');

const products = [
  {
    name: 'Premium Dog Kibble',
    description: 'High-protein, grain-free kibble for adult dogs.',
    price: 850,
    category: 'Food',
    imageUrl: '/images/dog_food.png'
  },
  {
    name: 'Gourmet Cat Tuna',
    description: 'Delicious canned tuna in gravy for cats of all ages.',
    price: 350,
    category: 'Food',
    imageUrl: '/images/cat_food.png'
  },
  {
    name: 'Interactive Feather Wand',
    description: 'Keep your cat entertained for hours with this wand toy.',
    price: 250,
    category: 'Toys',
    imageUrl: '/images/cat_toy.png'
  },
  {
    name: 'Heavy Duty Chew Rope',
    description: 'Durable cotton rope for aggressive chewers.',
    price: 300,
    category: 'Toys',
    imageUrl: '/images/dog_toy.png'
  },
  {
    name: 'Soothing Oatmeal Shampoo',
    description: 'Gentle shampoo for sensitive pet skin.',
    price: 450,
    category: 'Care',
    imageUrl: '/images/shampoo.png'
  },
  {
    name: 'Bird Seed Mix',
    description: 'Nutrient-rich seed mix for parrots and small birds.',
    price: 200,
    category: 'Food',
    imageUrl: '/images/bird_seed.png'
  }
];

mongoose.connect(process.env.MONGO_URI || 'mongodb://127.0.0.1:27017/animal_adoption')
  .then(async () => {
    console.log('Connected to MongoDB. Seeding products...');
    await Product.deleteMany({});
    await Product.insertMany(products);
    console.log('Successfully seeded 6 products!');
    process.exit(0);
  })
  .catch(err => {
    console.error('Error seeding products:', err);
    process.exit(1);
  });
