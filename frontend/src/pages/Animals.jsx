import React, { useState, useEffect } from 'react';
import { createPortal } from 'react-dom';
import axios from 'axios';
import { QRCodeSVG } from 'qrcode.react';
import { useAppContext } from '../context/AppContext';

export default function Animals() {
  const { user } = useAppContext();
  const [animals, setAnimals] = useState([]);
  const [loading, setLoading] = useState(true);
  
  // Payment Modal State
  const [showQRModal, setShowQRModal] = useState(false);
  const [selectedAnimal, setSelectedAnimal] = useState(null);

  useEffect(() => {
    axios.get('https://pawconnect-x0gc.onrender.com/api/animals')
      .then(res => {
        setAnimals(res.data);
        setLoading(false);
      })
      .catch(err => {
        console.error('Error fetching animals:', err);
        setLoading(false);
      });
  }, []);

  const handleAdoptClick = (animal) => {
    if (!user) {
      alert("Please login or sign up first to adopt a pet!");
      return;
    }
    setSelectedAnimal(animal);
    setShowQRModal(true);
  };

  const getAnimalImage = (species) => {
    const s = (species || '').toLowerCase();
    if (s.includes('dog')) return '/images/dog.png';
    if (s.includes('cat')) return '/images/cat.png';
    if (s.includes('bird')) return '/images/bird.png';
    if (s.includes('rabbit')) return '/images/rabbit.png';
    return '/images/dog.png'; // Fallback
  };

  if (loading) return <h2 style={{ textAlign: 'center', marginTop: '50px' }}>Loading wonderful pets...</h2>;

  return (
    <div className="animate-fade-in" style={{ maxWidth: '1200px', margin: '0 auto', padding: '40px 0' }}>
      <h2 style={{ fontSize: '2.5rem', marginBottom: '30px', textAlign: 'center' }}>Meet Our Animals</h2>
      
      <div className="grid-layout">
        {animals.map((animal) => (
          <div 
            key={animal._id} 
            className="glass-panel pet-card" 
            style={{ 
              padding: '20px', 
              display: 'flex', 
              flexDirection: 'column',
              transition: 'transform 0.3s ease, box-shadow 0.3s ease',
              cursor: 'pointer'
            }}
            onMouseOver={(e) => {
              e.currentTarget.style.transform = 'translateY(-10px) rotateX(5deg) rotateY(5deg)';
              e.currentTarget.style.boxShadow = '0 20px 40px rgba(139, 92, 246, 0.2)';
            }}
            onMouseOut={(e) => {
              e.currentTarget.style.transform = 'translateY(0) rotateX(0) rotateY(0)';
              e.currentTarget.style.boxShadow = 'var(--glass-shadow)';
            }}
          >
            <div style={{ 
              height: '250px', 
              borderRadius: '8px',
              marginBottom: '20px',
              overflow: 'hidden',
              background: '#f1f5f9'
            }}>
              <img 
                src={getAnimalImage(animal.species)} 
                alt={animal.name} 
                style={{ width: '100%', height: '100%', objectFit: 'cover' }}
              />
            </div>
            <h3 style={{ fontSize: '1.5rem', marginBottom: '10px' }}>{animal.name}</h3>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '5px' }}><strong>Breed:</strong> {animal.breed}</p>
            <p style={{ color: 'var(--text-secondary)', marginBottom: '15px' }}><strong>Age:</strong> {animal.age} years</p>
            <p style={{ marginBottom: '20px', flex: 1, color: 'var(--text-primary)' }}>{animal.description}</p>
            
            <button 
              className="btn-primary" 
              onClick={() => handleAdoptClick(animal)}
              style={{ width: '100%', textAlign: 'center' }}
            >
              Adopt {animal.name}
            </button>
          </div>
        ))}
      </div>

      {/* Custom QR Code Payment Modal - Rendered via Portal to avoid CSS transform trapping */}
      {showQRModal && selectedAnimal && createPortal(
        <div style={{
          position: 'fixed',
          top: 0, left: 0, right: 0, bottom: 0,
          background: 'rgba(0, 0, 0, 0.5)',
          backdropFilter: 'blur(5px)',
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'center',
          zIndex: 99999
        }}>
          <div className="glass-panel animate-fade-in" style={{ padding: '30px', maxWidth: '350px', width: '90%', textAlign: 'center', background: 'rgba(255, 255, 255, 0.95)', boxShadow: '0 25px 50px -12px rgba(0, 0, 0, 0.25)' }}>
            <h2 style={{ marginBottom: '10px', color: 'var(--text-primary)', fontSize: '1.5rem' }}>Adoption Fee</h2>
            <p style={{ marginBottom: '20px', color: 'var(--text-secondary)', fontSize: '0.9rem' }}>
              Scan the QR Code below to securely complete your adoption of <strong>{selectedAnimal.name}</strong>.
            </p>
            <div style={{ background: 'white', padding: '15px', borderRadius: '12px', display: 'inline-block', marginBottom: '20px', border: '1px solid #e2e8f0' }}>
              <QRCodeSVG 
                value={`upi://pay?pa=utkarsh.joshi.2423-2@okicici&pn=PawConnect&am=500.00&cu=INR`} 
                size={180}
                level="H"
                includeMargin={true}
              />
            </div>
            <div style={{ display: 'flex', gap: '10px' }}>
              <button 
                className="btn-primary" 
                style={{ flex: 1, background: '#10b981', padding: '12px' }}
                onClick={async () => {
                  try {
                    await axios.post('https://pawconnect-x0gc.onrender.com/api/user/adopt', {
                      userId: user.id || user._id,
                      animalId: selectedAnimal._id
                    });
                    alert(`Payment Verified! You have successfully adopted ${selectedAnimal.name}. They will now appear on your dashboard.`);
                    setShowQRModal(false);
                    // refresh animal list to show it as adopted (or just remove it from UI)
                    setAnimals(prev => prev.filter(a => a._id !== selectedAnimal._id));
                  } catch (err) {
                    console.error(err);
                    alert("Something went wrong. Please try again.");
                  }
                }}
              >
                I've Paid
              </button>
              <button 
                className="btn-primary" 
                style={{ flex: 1, background: '#ef4444', padding: '12px' }}
                onClick={() => setShowQRModal(false)}
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
