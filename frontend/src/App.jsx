import React, { Suspense } from 'react';
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import { Canvas } from '@react-three/fiber';
import { OrbitControls, Sparkles } from '@react-three/drei';
import { AppProvider, useAppContext } from './context/AppContext';
import Home from './pages/Home';
import Login from './pages/Login';
import Animals from './pages/Animals';
import Dashboard from './pages/Dashboard';
import Shop from './pages/Shop';
import AIChat from './components/AIChat';
import './index.css';

function Navbar() {
  const { user, cart } = useAppContext();
  const cartCount = cart.reduce((acc, item) => acc + item.qty, 0);

  return (
    <nav className="glass-panel" style={{ padding: '20px', display: 'flex', justifyContent: 'space-between', alignItems: 'center', margin: '20px', position: 'relative', zIndex: 10 }}>
      <Link to="/" style={{ color: 'var(--text-primary)', textDecoration: 'none', fontSize: '24px', fontWeight: 'bold' }}>PawConnect 3D</Link>
      <div style={{ display: 'flex', gap: '20px', alignItems: 'center' }}>
        <Link to="/animals" className="btn-primary" style={{ background: 'transparent', border: '1px solid var(--glass-border)', color: 'var(--text-primary)' }}>Adopt</Link>
        <Link to="/shop" className="btn-primary" style={{ background: 'transparent', border: '1px solid var(--glass-border)', color: 'var(--text-primary)' }}>Shop</Link>
        
        {cartCount > 0 && (
          <Link to="/shop" style={{ textDecoration: 'none', color: 'var(--accent)', fontWeight: 'bold' }}>
            Cart ({cartCount})
          </Link>
        )}

        {user ? (
          <Link to="/dashboard" className="btn-primary">Dashboard</Link>
        ) : (
          <Link to="/login" className="btn-primary">Login / Sign Up</Link>
        )}
      </div>
    </nav>
  );
}

function Scene() {
  return (
    <Canvas style={{ position: 'fixed', top: 0, left: 0, width: '100vw', height: '100vh', zIndex: -1 }}>
      <ambientLight intensity={0.5} />
      <directionalLight position={[10, 10, 5]} intensity={1} />
      <Sparkles count={200} scale={20} size={10} speed={0.4} opacity={0.3} color="#8b5cf6" />
      <OrbitControls enableZoom={false} autoRotate autoRotateSpeed={0.5} />
      {/* Interactive 3D elements will be added per page if needed */}
    </Canvas>
  );
}

function App() {
  return (
    <AppProvider>
      <Router>
        <Scene />
        <Navbar />
        <div style={{ padding: '0 20px', position: 'relative', zIndex: 1 }}>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/animals" element={<Animals />} />
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/shop" element={<Shop />} />
          </Routes>
        </div>
        <AIChat />
      </Router>
    </AppProvider>
  );
}

export default App;
