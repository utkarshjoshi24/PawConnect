require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const cors = require('cors');
const Razorpay = require('razorpay');
const { GoogleGenAI } = require('@google/genai');

const Animal = require('./models/Animal');
const User = require('./models/User');
const Product = require('./models/Product');

const app = express();
app.use(cors());
app.use(express.json());

// Initialize AI and Razorpay (using dummy keys if not provided to avoid crash)
const ai = new GoogleGenAI({ apiKey: process.env.GEMINI_API_KEY || 'dummy' });
const razorpay = new Razorpay({
  key_id: process.env.RAZORPAY_KEY_ID || 'dummy',
  key_secret: process.env.RAZORPAY_KEY_SECRET || 'dummy'
});

// Connect to MongoDB
mongoose.connect(process.env.MONGO_URI)
  .then(() => console.log('Connected to MongoDB'))
  .catch(err => console.error('MongoDB connection error:', err));

// --- Auth Routes ---
app.post('/api/auth/register', async (req, res) => {
  try {
    const { name, email, password } = req.body;
    let user = await User.findOne({ email });
    if (user) return res.status(400).json({ message: 'User already exists' });
    
    user = new User({ name, email, password });
    await user.save();
    res.status(201).json({ token: 'dummy-jwt-token', user: { id: user._id, name: user.name, email: user.email } });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/api/auth/login', async (req, res) => {
  const { email, password } = req.body;
  const user = await User.findOne({ email });
  if (user && user.password === password) {
    // Dummy JWT for now
    res.json({ token: 'dummy-jwt-token', user: { id: user._id, name: user.name, email: user.email } });
  } else {
    res.status(401).json({ message: 'Invalid credentials' });
  }
});

// --- User Profile & Adoption Routes ---
app.get('/api/user/profile', async (req, res) => {
  try {
    // In a real app, user ID comes from JWT verification middleware
    const { userId } = req.query;
    const user = await User.findById(userId).populate('adoptedPets');
    if (!user) return res.status(404).json({ message: 'User not found' });
    res.json(user);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

app.post('/api/user/adopt', async (req, res) => {
  try {
    const { userId, animalId } = req.body;
    const user = await User.findById(userId);
    if (!user) return res.status(404).json({ message: 'User not found' });
    
    // Check if already adopted
    if (!user.adoptedPets.includes(animalId)) {
      user.adoptedPets.push(animalId);
      await user.save();
    }
    
    // Update animal status
    await Animal.findByIdAndUpdate(animalId, { status: 'Adopted' });
    
    res.json({ message: 'Adoption successful', user });
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// --- Product Routes ---
app.get('/api/products', async (req, res) => {
  try {
    const products = await Product.find();
    res.json(products);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
});

// --- Animal Routes ---
app.get('/api/animals', async (req, res) => {
  const animals = await Animal.find();
  res.json(animals);
});

// --- Payment Route (Razorpay) ---
app.post('/api/payment/create-order', async (req, res) => {
  try {
    const options = {
      amount: 50000, // amount in the smallest currency unit (e.g., 500 INR)
      currency: "INR",
      receipt: "receipt_order_74394"
    };
    
    // If we are using dummy keys, Razorpay will fail. Let's return a mock order for demo purposes.
    if (process.env.RAZORPAY_KEY_ID === 'test_key_id' || !process.env.RAZORPAY_KEY_ID) {
      console.log('Using mock order creation for dummy keys');
      return res.json({
        id: "order_mock_" + Math.floor(Math.random() * 1000000),
        amount: options.amount,
        currency: options.currency
      });
    }

    const order = await razorpay.orders.create(options);
    res.json(order);
  } catch (error) {
    console.error('Razorpay Error:', error);
    res.status(500).json({ error: error.message });
  }
});

// --- AI Assistant Route ---
app.post('/api/ai/chat', async (req, res) => {
  try {
    const { message } = req.body;
    
    // Fetch available pets and products to give the AI context
    const animals = await Animal.find();
    const products = await Product.find();
    
    const animalContext = animals.map(a => `${a.name} (${a.breed} ${a.species}, ${a.age} yrs, ${a.status})`).join(', ');
    const productContext = products.map(p => `${p.name} (₹${p.price})`).join(', ');

    const promptContext = `
You are a highly knowledgeable and friendly AI assistant for "PawConnect", a modern pet adoption and pet supply store. 
Your goal is to resolve any doubts the user has about pet care, food, adoption, and training.
Here is the current context of our store:
Available Pets: ${animalContext || 'None right now'}
Available Products in Shop: ${productContext || 'None right now'}

User says: "${message}"

Please provide a helpful, concise, and friendly response. If they ask about pets or products, recommend from the available lists. If they ask general pet care questions, answer them accurately.
    `;

    // Try generating content with Gemini
    const response = await ai.models.generateContent({
      model: 'gemini-2.5-flash',
      contents: promptContext,
    });
    
    res.json({ reply: response.text });
  } catch (error) {
    console.error('AI Error:', error.message);
    res.status(500).json({ reply: "My advanced AI brain needs a valid GEMINI_API_KEY in the backend/.env file to answer that! Please provide one." });
  }
});

const PORT = process.env.PORT || 5000;
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
