import React, { useRef } from 'react';
import { Canvas, useFrame } from '@react-three/fiber';
import { Float, Text3D, Center, PresentationControls } from '@react-three/drei';
import * as THREE from 'three';

function AnimatedDog() {
  const groupRef = useRef();
  
  useFrame((state) => {
    // Gentle floating and looking around animation
    groupRef.current.position.y = Math.sin(state.clock.elapsedTime * 2) * 0.1;
    groupRef.current.rotation.y = Math.sin(state.clock.elapsedTime) * 0.2;
    groupRef.current.rotation.x = Math.sin(state.clock.elapsedTime * 0.5) * 0.1;
  });

  return (
    <group ref={groupRef} scale={1.5}>
      {/* Head */}
      <mesh position={[0, 0, 0]}>
        <sphereGeometry args={[1, 32, 32]} />
        <meshStandardMaterial color="#fcd34d" roughness={0.4} />
      </mesh>
      
      {/* Snout */}
      <mesh position={[0, -0.2, 0.8]}>
        <sphereGeometry args={[0.5, 32, 32]} />
        <meshStandardMaterial color="#fef3c7" roughness={0.6} />
      </mesh>

      {/* Nose */}
      <mesh position={[0, -0.1, 1.25]}>
        <sphereGeometry args={[0.15, 16, 16]} />
        <meshStandardMaterial color="#1e293b" />
      </mesh>

      {/* Left Eye */}
      <mesh position={[-0.3, 0.3, 0.8]}>
        <sphereGeometry args={[0.12, 16, 16]} />
        <meshStandardMaterial color="#1e293b" />
      </mesh>

      {/* Right Eye */}
      <mesh position={[0.3, 0.3, 0.8]}>
        <sphereGeometry args={[0.12, 16, 16]} />
        <meshStandardMaterial color="#1e293b" />
      </mesh>

      {/* Left Ear */}
      <mesh position={[-0.8, 0.6, 0]} rotation={[0, 0, Math.PI / 4]}>
        <coneGeometry args={[0.4, 1.2, 32]} />
        <meshStandardMaterial color="#d97706" />
      </mesh>

      {/* Right Ear */}
      <mesh position={[0.8, 0.6, 0]} rotation={[0, 0, -Math.PI / 4]}>
        <coneGeometry args={[0.4, 1.2, 32]} />
        <meshStandardMaterial color="#d97706" />
      </mesh>
    </group>
  );
}

export default function Home() {
  return (
    <div className="animate-fade-in" style={{ display: 'flex', minHeight: '80vh', alignItems: 'center', justifyContent: 'center' }}>
      <div style={{ flex: 1, padding: '40px', zIndex: 1 }}>
        <div className="glass-panel" style={{ padding: '40px', maxWidth: '600px' }}>
          <h1 style={{ fontSize: '4rem', marginBottom: '20px', background: 'linear-gradient(to right, #a855f7, #ec4899)', WebkitBackgroundClip: 'text', WebkitTextFillColor: 'transparent' }}>
            Find Your New Best Friend.
          </h1>
          <p style={{ fontSize: '1.2rem', color: 'var(--text-secondary)', marginBottom: '30px', lineHeight: '1.6' }}>
            Experience the future of animal adoption. Browse our 3D interactive gallery and meet pets waiting for a loving home.
          </p>
          <a href="/animals" className="btn-primary" style={{ fontSize: '1.2rem', padding: '16px 32px' }}>
            Explore Animals
          </a>
        </div>
      </div>
      
      <div style={{ flex: 1, height: '600px', zIndex: 1 }}>
        <Canvas camera={{ position: [0, 0, 5] }}>
          <ambientLight intensity={0.5} />
          <directionalLight position={[10, 10, 5]} intensity={2} />
          <PresentationControls global zoom={0.8} rotation={[0, 0, 0]} polar={[-0.2, 0.2]} azimuth={[-0.5, 0.5]}>
            <AnimatedDog />
          </PresentationControls>
        </Canvas>
      </div>
    </div>
  );
}
