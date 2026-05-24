import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { createPortal } from 'react-dom';
import { QRCodeSVG } from 'qrcode.react';
import { useAppContext } from '../context/AppContext';

export default function Shop() {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [activeTab, setActiveTab] = useState('All');
  
  const { cart, addToCart, removeFromCart, clearCart, getCartTotal } = useAppContext();
  const [showCheckout, setShowCheckout] = useState(false);

  useEffect(() => {
    axios.get('https://pawconnect-x0gc.onrender.com/api/products')
      .then(res => {
        setProducts(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching products:', err);
        setLoading(false);
      });
  }, []);

  const filteredProducts = activeTab === 'All' 
    ? products 
    : products.filter(p => p.category === activeTab);

  const total = getCartTotal();

  if (loading) return <h2 style={{ textAlign: 'center', marginTop: '50px' }}>Loading Shop...</h2>;

  return (
    <div className="animate-fade-in" style={{ maxWidth: '1200px', margin: '0 auto', padding: '40px 0', display: 'flex', gap: '30px' }}>
      
      {/* Products Section */}
      <div style={{ flex: 1 }}>
        <h2 style={{ fontSize: '2.5rem', marginBottom: '20px' }}>Pet Supplies Shop</h2>
        
        {/* Tabs */}
        <div style={{ display: 'flex', gap: '15px', marginBottom: '30px' }}>
          {['All', 'Food', 'Toys', 'Care'].map(tab => (
            <button 
              key={tab}
              onClick={() => setActiveTab(tab)}
              className="btn-primary"
              style={{ 
                background: activeTab === tab ? 'var(--accent)' : 'transparent',
                color: activeTab === tab ? 'white' : 'var(--text-primary)',
                border: '1px solid var(--accent)'
              }}
            >
              {tab}
            </button>
          ))}
        </div>

        {/* Product Grid */}
        <div className="grid-layout" style={{ padding: 0 }}>
          {filteredProducts.map(product => (
            <div key={product._id} className="glass-panel" style={{ padding: '20px', display: 'flex', flexDirection: 'column' }}>
              <div style={{ height: '200px', borderRadius: '8px', marginBottom: '15px', overflow: 'hidden', background: 'white' }}>
                <img src={product.imageUrl} alt={product.name} style={{ width: '100%', height: '100%', objectFit: 'contain' }} />
              </div>
              <h3 style={{ fontSize: '1.2rem', marginBottom: '5px' }}>{product.name}</h3>
              <p style={{ color: 'var(--text-secondary)', marginBottom: '10px', fontSize: '0.9rem', flex: 1 }}>{product.description}</p>
              <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <span style={{ fontSize: '1.2rem', fontWeight: 'bold', color: 'var(--accent)' }}>₹{product.price}</span>
                <button className="btn-primary" onClick={() => addToCart(product)} style={{ padding: '8px 16px' }}>Add to Cart</button>
              </div>
            </div>
          ))}
        </div>
      </div>

      {/* Cart Sidebar */}
      <div className="glass-panel" style={{ width: '350px', padding: '24px', height: 'fit-content', position: 'sticky', top: '20px' }}>
        <h3 style={{ fontSize: '1.5rem', marginBottom: '20px', borderBottom: '1px solid var(--glass-border)', paddingBottom: '10px' }}>Your Cart</h3>
        
        {cart.length === 0 ? (
          <p style={{ color: 'var(--text-secondary)', fontStyle: 'italic' }}>Your cart is empty.</p>
        ) : (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '15px' }}>
            {cart.map(item => (
              <div key={item._id} style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center' }}>
                <div style={{ flex: 1 }}>
                  <p style={{ fontWeight: 'bold', fontSize: '0.9rem' }}>{item.name}</p>
                  <p style={{ color: 'var(--text-secondary)', fontSize: '0.8rem' }}>₹{item.price} x {item.qty}</p>
                </div>
                <button 
                  onClick={() => removeFromCart(item._id)}
                  style={{ background: 'transparent', border: 'none', color: '#ef4444', cursor: 'pointer', fontSize: '1.2rem' }}
                >
                  &times;
                </button>
              </div>
            ))}
            
            <div style={{ borderTop: '2px solid var(--glass-border)', paddingTop: '15px', marginTop: '10px' }}>
              <div style={{ display: 'flex', justifyContent: 'space-between', fontWeight: 'bold', fontSize: '1.2rem', marginBottom: '20px' }}>
                <span>Total:</span>
                <span>₹{total.toFixed(2)}</span>
              </div>
              <button 
                className="btn-primary" 
                style={{ width: '100%', background: '#10b981' }}
                onClick={() => setShowCheckout(true)}
              >
                Checkout
              </button>
            </div>
          </div>
        )}
      </div>

      {/* Checkout QR Modal */}
      {showCheckout && createPortal(
        <div style={{
          position: 'fixed', top: 0, left: 0, right: 0, bottom: 0,
          background: 'rgba(0, 0, 0, 0.5)', backdropFilter: 'blur(5px)',
          display: 'flex', alignItems: 'center', justifyContent: 'center', zIndex: 99999
        }}>
          <div className="glass-panel animate-fade-in" style={{ padding: '30px', maxWidth: '350px', width: '90%', textAlign: 'center', background: 'rgba(255, 255, 255, 0.95)', boxShadow: '0 25px 50px -12px rgba(0,0,0,0.25)' }}>
            <h2 style={{ marginBottom: '10px', color: 'var(--text-primary)', fontSize: '1.5rem' }}>Checkout</h2>
            <p style={{ marginBottom: '20px', color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
              Scan to pay <strong>₹{total.toFixed(2)}</strong> for your pet supplies.
            </p>
            <div style={{ background: 'white', padding: '15px', borderRadius: '12px', display: 'inline-block', marginBottom: '20px', border: '1px solid #e2e8f0' }}>
              <QRCodeSVG 
                value={`upi://pay?pa=pawconnect@upi&pn=PawConnect%20Shop&am=${total.toFixed(2)}&cu=INR`} 
                size={180} level="H" includeMargin={true}
              />
            </div>
            <div style={{ display: 'flex', gap: '10px' }}>
              <button 
                className="btn-primary" style={{ flex: 1, background: '#10b981', padding: '12px' }}
                onClick={() => {
                  alert('Payment Verified! Your order is placed.');
                  clearCart();
                  setShowCheckout(false);
                }}
              >
                I've Paid
              </button>
              <button 
                className="btn-primary" style={{ flex: 1, background: '#ef4444', padding: '12px' }}
                onClick={() => setShowCheckout(false)}
              >
                Cancel
              </button>
            </div>
          </div>
        </div>,
        document.body
      )}
    </div>
  );
}
