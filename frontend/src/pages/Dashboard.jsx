import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import { useAppContext } from '../context/AppContext';

export default function Dashboard() {
  const navigate = useNavigate();
  const { user, logout } = useAppContext();
  const [profileData, setProfileData] = useState(null);

  useEffect(() => {
    if (!user) {
      navigate('/login');
      return;
    }

    axios.get(`http://localhost:5001/api/user/profile?userId=${user.id || user._id}`)
      .then(res => setProfileData(res.data))
      .catch(err => console.error(err));
  }, [user, navigate]);

  if (!profileData) return <h2 style={{ textAlign: 'center', marginTop: '50px' }}>Loading Dashboard...</h2>;

  return (
    <div className="animate-fade-in" style={{ maxWidth: '1000px', margin: '40px auto', padding: '0 20px' }}>
      <div className="glass-panel" style={{ padding: '40px' }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '30px' }}>
          <h2 style={{ fontSize: '2.5rem' }}>Welcome to your Dashboard</h2>
          <button 
            className="btn-primary" 
            style={{ background: '#ef4444' }}
            onClick={() => {
              logout();
              navigate('/login');
            }}
          >
            Logout
          </button>
        </div>
        
        <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '24px' }}>
          
          {/* Profile Section */}
          <div style={{ background: 'rgba(255,255,255,0.5)', padding: '24px', borderRadius: '12px', border: '1px solid var(--glass-border)' }}>
            <h3 style={{ marginBottom: '15px', color: 'var(--accent)' }}>Profile Details</h3>
            <p style={{ marginBottom: '8px' }}><strong>Name:</strong> {profileData.name}</p>
            <p style={{ marginBottom: '8px' }}><strong>Email:</strong> {profileData.email}</p>
            <p style={{ marginBottom: '8px' }}><strong>Member Since:</strong> {new Date(profileData.registration_date).toLocaleDateString()}</p>
          </div>

          {/* Adoption Status */}
          <div style={{ background: 'rgba(255,255,255,0.5)', padding: '24px', borderRadius: '12px', border: '1px solid var(--glass-border)' }}>
            <h3 style={{ marginBottom: '15px', color: 'var(--accent)' }}>My Adopted Pets</h3>
            
            {profileData.adoptedPets && profileData.adoptedPets.length > 0 ? (
              <ul style={{ listStyleType: 'none', padding: 0 }}>
                {profileData.adoptedPets.map(pet => (
                  <li key={pet._id} style={{ padding: '10px', borderBottom: '1px solid var(--glass-border)' }}>
                    <strong>{pet.name}</strong> - {pet.breed} ({pet.age} yrs)
                  </li>
                ))}
              </ul>
            ) : (
              <>
                <p style={{ color: 'var(--text-secondary)', fontStyle: 'italic' }}>You haven't adopted any pets yet.</p>
                <button 
                  className="btn-primary" 
                  style={{ marginTop: '20px' }}
                  onClick={() => navigate('/animals')}
                >
                  Browse Pets
                </button>
              </>
            )}
          </div>

        </div>
      </div>
    </div>
  );
}
