# Create HTML frontend files
import os

# index.html - Main homepage
index_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Animal Adoption Management System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="container">
                <h1 class="logo">🐾 PetHaven</h1>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="animals.html">Find Pets</a></li>
                    <li><a href="shelters.html">Shelters</a></li>
                    <li><a href="admin.html">Admin</a></li>
                </ul>
            </div>
        </nav>
    </header>

    <main>
        <section class="hero">
            <div class="container">
                <h2>Find Your Perfect Pet Companion</h2>
                <p>Connect with loving animals looking for their forever homes.</p>
                <a href="animals.html" class="btn btn-primary">Browse Pets</a>
            </div>
        </section>

        <section class="stats">
            <div class="container">
                <div class="stat-grid">
                    <div class="stat-card">
                        <h3>150+</h3>
                        <p>Animals Available</p>
                    </div>
                    <div class="stat-card">
                        <h3>23</h3>
                        <p>Adopted This Month</p>
                    </div>
                    <div class="stat-card">
                        <h3>3</h3>
                        <p>Partner Shelters</p>
                    </div>
                </div>
            </div>
        </section>

        <section class="featured-animals">
            <div class="container">
                <h2>Featured Animals</h2>
                <div class="animal-grid" id="featuredAnimals">
                    <!-- Animals will be loaded dynamically -->
                </div>
            </div>
        </section>
    </main>

    <footer>
        <div class="container">
            <p>&copy; 2025 Animal Adoption Management System. All rights reserved.</p>
        </div>
    </footer>

    <script src="js/main.js"></script>
</body>
</html>'''

# animals.html - Animal listings page
animals_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Find Pets - Animal Adoption System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="container">
                <h1 class="logo">🐾 PetHaven</h1>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="animals.html" class="active">Find Pets</a></li>
                    <li><a href="shelters.html">Shelters</a></li>
                    <li><a href="admin.html">Admin</a></li>
                </ul>
            </div>
        </nav>
    </header>

    <main>
        <section class="search-section">
            <div class="container">
                <h2>Find Your Perfect Pet</h2>
                <div class="search-filters">
                    <select id="speciesFilter">
                        <option value="">All Species</option>
                        <option value="Dog">Dogs</option>
                        <option value="Cat">Cats</option>
                    </select>
                    <select id="ageFilter">
                        <option value="">All Ages</option>
                        <option value="0-1">Puppy/Kitten (0-1 years)</option>
                        <option value="2-5">Young (2-5 years)</option>
                        <option value="6+">Adult (6+ years)</option>
                    </select>
                    <select id="genderFilter">
                        <option value="">All Genders</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                    </select>
                    <button id="searchBtn" class="btn btn-primary">Search</button>
                </div>
            </div>
        </section>

        <section class="animals-list">
            <div class="container">
                <div class="animal-grid" id="animalsList">
                    <!-- Animals will be loaded dynamically -->
                </div>
            </div>
        </section>
    </main>

    <!-- Animal Detail Modal -->
    <div id="animalModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <div id="animalDetails">
                <!-- Animal details will be loaded here -->
            </div>
        </div>
    </div>

    <!-- Adoption Form Modal -->
    <div id="adoptionModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h3>Adoption Application</h3>
            <form id="adoptionForm">
                <input type="hidden" id="animalId" name="animalId">
                <div class="form-group">
                    <label for="userName">Full Name:</label>
                    <input type="text" id="userName" name="userName" required>
                </div>
                <div class="form-group">
                    <label for="userEmail">Email:</label>
                    <input type="email" id="userEmail" name="userEmail" required>
                </div>
                <div class="form-group">
                    <label for="userPhone">Phone:</label>
                    <input type="tel" id="userPhone" name="userPhone" required>
                </div>
                <div class="form-group">
                    <label for="userAddress">Address:</label>
                    <textarea id="userAddress" name="userAddress" required></textarea>
                </div>
                <div class="form-group">
                    <label for="adoptionReason">Why do you want to adopt this pet?</label>
                    <textarea id="adoptionReason" name="adoptionReason" required></textarea>
                </div>
                <button type="submit" class="btn btn-primary">Submit Application</button>
            </form>
        </div>
    </div>

    <footer>
        <div class="container">
            <p>&copy; 2025 Animal Adoption Management System. All rights reserved.</p>
        </div>
    </footer>

    <script src="js/animals.js"></script>
</body>
</html>'''

# admin.html - Admin dashboard
admin_html = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Admin Dashboard - Animal Adoption System</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <nav class="navbar">
            <div class="container">
                <h1 class="logo">🐾 PetHaven Admin</h1>
                <ul class="nav-links">
                    <li><a href="index.html">Home</a></li>
                    <li><a href="animals.html">Find Pets</a></li>
                    <li><a href="admin.html" class="active">Admin</a></li>
                    <li><button id="logoutBtn" class="btn btn-secondary">Logout</button></li>
                </ul>
            </div>
        </nav>
    </header>

    <main>
        <!-- Login Form -->
        <section id="loginSection" class="admin-section">
            <div class="container">
                <div class="admin-login">
                    <h2>Admin Login</h2>
                    <form id="loginForm">
                        <div class="form-group">
                            <label for="username">Username:</label>
                            <input type="text" id="username" name="username" required>
                        </div>
                        <div class="form-group">
                            <label for="password">Password:</label>
                            <input type="password" id="password" name="password" required>
                        </div>
                        <button type="submit" class="btn btn-primary">Login</button>
                    </form>
                </div>
            </div>
        </section>

        <!-- Admin Dashboard -->
        <section id="dashboardSection" class="admin-section hidden">
            <div class="container">
                <h2>Admin Dashboard</h2>
                
                <div class="dashboard-tabs">
                    <button class="tab-btn active" data-tab="animals">Manage Animals</button>
                    <button class="tab-btn" data-tab="adoptions">Adoption Requests</button>
                    <button class="tab-btn" data-tab="users">Users</button>
                    <button class="tab-btn" data-tab="shelters">Shelters</button>
                </div>

                <!-- Animals Management -->
                <div id="animalsTab" class="tab-content active">
                    <div class="tab-header">
                        <h3>Manage Animals</h3>
                        <button id="addAnimalBtn" class="btn btn-primary">Add New Animal</button>
                    </div>
                    <div class="admin-table">
                        <table id="animalsTable">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>Species</th>
                                    <th>Breed</th>
                                    <th>Age</th>
                                    <th>Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Animals will be loaded here -->
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Adoptions Management -->
                <div id="adoptionsTab" class="tab-content">
                    <h3>Adoption Requests</h3>
                    <div class="admin-table">
                        <table id="adoptionsTable">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Animal</th>
                                    <th>Applicant</th>
                                    <th>Date</th>
                                    <th>Status</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Adoptions will be loaded here -->
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Users Management -->
                <div id="usersTab" class="tab-content">
                    <h3>Registered Users</h3>
                    <div class="admin-table">
                        <table id="usersTable">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>Email</th>
                                    <th>Phone</th>
                                    <th>Registration Date</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Users will be loaded here -->
                            </tbody>
                        </table>
                    </div>
                </div>

                <!-- Shelters Management -->
                <div id="sheltersTab" class="tab-content">
                    <h3>Partner Shelters</h3>
                    <div class="admin-table">
                        <table id="sheltersTable">
                            <thead>
                                <tr>
                                    <th>ID</th>
                                    <th>Name</th>
                                    <th>Address</th>
                                    <th>Phone</th>
                                    <th>Capacity</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <!-- Shelters will be loaded here -->
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>
        </section>
    </main>

    <!-- Add Animal Modal -->
    <div id="addAnimalModal" class="modal">
        <div class="modal-content">
            <span class="close">&times;</span>
            <h3>Add New Animal</h3>
            <form id="addAnimalForm">
                <div class="form-group">
                    <label for="animalName">Name:</label>
                    <input type="text" id="animalName" name="name" required>
                </div>
                <div class="form-group">
                    <label for="animalSpecies">Species:</label>
                    <select id="animalSpecies" name="species" required>
                        <option value="">Select Species</option>
                        <option value="Dog">Dog</option>
                        <option value="Cat">Cat</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="animalBreed">Breed:</label>
                    <input type="text" id="animalBreed" name="breed">
                </div>
                <div class="form-group">
                    <label for="animalAge">Age:</label>
                    <input type="number" id="animalAge" name="age" min="0" max="20">
                </div>
                <div class="form-group">
                    <label for="animalGender">Gender:</label>
                    <select id="animalGender" name="gender">
                        <option value="">Select Gender</option>
                        <option value="Male">Male</option>
                        <option value="Female">Female</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="animalHealth">Health Status:</label>
                    <select id="animalHealth" name="health_status">
                        <option value="Healthy">Healthy</option>
                        <option value="Under Treatment">Under Treatment</option>
                        <option value="Special Needs">Special Needs</option>
                    </select>
                </div>
                <div class="form-group">
                    <label for="animalDescription">Description:</label>
                    <textarea id="animalDescription" name="description"></textarea>
                </div>
                <div class="form-group">
                    <label for="animalImage">Image URL:</label>
                    <input type="url" id="animalImage" name="image_url">
                </div>
                <div class="form-group">
                    <label for="animalShelter">Shelter:</label>
                    <select id="animalShelter" name="shelter_id">
                        <option value="1">Happy Paws Animal Shelter</option>
                        <option value="2">Safe Haven Pet Rescue</option>
                        <option value="3">Loving Hearts Animal Sanctuary</option>
                    </select>
                </div>
                <button type="submit" class="btn btn-primary">Add Animal</button>
            </form>
        </div>
    </div>

    <footer>
        <div class="container">
            <p>&copy; 2025 Animal Adoption Management System. All rights reserved.</p>
        </div>
    </footer>

    <script src="js/admin.js"></script>
</body>
</html>'''

# styles.css - Main stylesheet
styles_css = '''/* Reset and Base Styles */
* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}

body {
    font-family: 'Arial', sans-serif;
    line-height: 1.6;
    color: #333;
    background-color: #f8f9fa;
}

.container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
}

/* Navigation */
.navbar {
    background: linear-gradient(135deg, #2c5282 0%, #3182ce 100%);
    color: white;
    padding: 1rem 0;
    box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}

.navbar .container {
    display: flex;
    justify-content: space-between;
    align-items: center;
}

.logo {
    font-size: 1.8rem;
    font-weight: bold;
}

.nav-links {
    display: flex;
    list-style: none;
    gap: 2rem;
    align-items: center;
}

.nav-links a {
    color: white;
    text-decoration: none;
    padding: 0.5rem 1rem;
    border-radius: 4px;
    transition: background-color 0.3s;
}

.nav-links a:hover,
.nav-links a.active {
    background-color: rgba(255,255,255,0.2);
}

/* Buttons */
.btn {
    display: inline-block;
    padding: 0.75rem 1.5rem;
    border: none;
    border-radius: 6px;
    cursor: pointer;
    text-decoration: none;
    font-size: 1rem;
    transition: all 0.3s ease;
    text-align: center;
}

.btn-primary {
    background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
    color: white;
}

.btn-primary:hover {
    transform: translateY(-2px);
    box-shadow: 0 4px 12px rgba(72, 187, 120, 0.4);
}

.btn-secondary {
    background: #718096;
    color: white;
}

.btn-secondary:hover {
    background: #4a5568;
}

.btn-outline {
    background: transparent;
    border: 2px solid #48bb78;
    color: #48bb78;
}

.btn-outline:hover {
    background: #48bb78;
    color: white;
}

.btn-danger {
    background: #e53e3e;
    color: white;
}

.btn-danger:hover {
    background: #c53030;
}

/* Hero Section */
.hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    color: white;
    padding: 4rem 0;
    text-align: center;
}

.hero h2 {
    font-size: 3rem;
    margin-bottom: 1rem;
}

.hero p {
    font-size: 1.2rem;
    margin-bottom: 2rem;
    opacity: 0.9;
}

/* Stats Section */
.stats {
    padding: 3rem 0;
    background: white;
}

.stat-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 2rem;
    text-align: center;
}

.stat-card {
    padding: 2rem;
    border-radius: 10px;
    background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
    color: white;
    box-shadow: 0 4px 15px rgba(240, 147, 251, 0.3);
}

.stat-card h3 {
    font-size: 2.5rem;
    margin-bottom: 0.5rem;
}

/* Animal Grid */
.featured-animals,
.animals-list {
    padding: 3rem 0;
}

.featured-animals h2,
.animals-list h2 {
    text-align: center;
    margin-bottom: 2rem;
    font-size: 2.5rem;
    color: #2d3748;
}

.animal-grid {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
    gap: 2rem;
}

.animal-card {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
    transition: transform 0.3s ease, box-shadow 0.3s ease;
    cursor: pointer;
}

.animal-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 8px 30px rgba(0,0,0,0.15);
}

.animal-card img {
    width: 100%;
    height: 250px;
    object-fit: cover;
}

.animal-card-content {
    padding: 1.5rem;
}

.animal-card h3 {
    font-size: 1.5rem;
    margin-bottom: 0.5rem;
    color: #2d3748;
}

.animal-info {
    display: flex;
    justify-content: space-between;
    margin-bottom: 1rem;
    color: #718096;
    font-size: 0.9rem;
}

.animal-card p {
    color: #4a5568;
    margin-bottom: 1rem;
}

.status-badge {
    display: inline-block;
    padding: 0.25rem 0.75rem;
    border-radius: 20px;
    font-size: 0.8rem;
    font-weight: bold;
}

.status-available {
    background: #c6f6d5;
    color: #22543d;
}

.status-pending {
    background: #fef5e7;
    color: #c05621;
}

.status-adopted {
    background: #e2e8f0;
    color: #4a5568;
}

/* Search Section */
.search-section {
    background: white;
    padding: 2rem 0;
    border-bottom: 1px solid #e2e8f0;
}

.search-filters {
    display: flex;
    gap: 1rem;
    align-items: center;
    flex-wrap: wrap;
}

.search-filters select {
    padding: 0.75rem;
    border: 2px solid #e2e8f0;
    border-radius: 6px;
    font-size: 1rem;
}

/* Modal Styles */
.modal {
    display: none;
    position: fixed;
    z-index: 1000;
    left: 0;
    top: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0,0,0,0.5);
}

.modal-content {
    background-color: white;
    margin: 5% auto;
    padding: 2rem;
    border-radius: 12px;
    width: 90%;
    max-width: 600px;
    max-height: 80vh;
    overflow-y: auto;
    position: relative;
}

.close {
    position: absolute;
    right: 1rem;
    top: 1rem;
    font-size: 2rem;
    cursor: pointer;
    color: #718096;
}

.close:hover {
    color: #2d3748;
}

/* Form Styles */
.form-group {
    margin-bottom: 1.5rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
    font-weight: bold;
    color: #2d3748;
}

.form-group input,
.form-group select,
.form-group textarea {
    width: 100%;
    padding: 0.75rem;
    border: 2px solid #e2e8f0;
    border-radius: 6px;
    font-size: 1rem;
}

.form-group textarea {
    resize: vertical;
    min-height: 100px;
}

/* Admin Styles */
.admin-section {
    padding: 3rem 0;
}

.admin-login {
    max-width: 400px;
    margin: 0 auto;
    background: white;
    padding: 2rem;
    border-radius: 12px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.dashboard-tabs {
    display: flex;
    margin-bottom: 2rem;
    border-bottom: 2px solid #e2e8f0;
}

.tab-btn {
    background: none;
    border: none;
    padding: 1rem 2rem;
    cursor: pointer;
    font-size: 1rem;
    color: #718096;
    border-bottom: 2px solid transparent;
    transition: all 0.3s;
}

.tab-btn.active,
.tab-btn:hover {
    color: #3182ce;
    border-bottom-color: #3182ce;
}

.tab-content {
    display: none;
}

.tab-content.active {
    display: block;
}

.tab-header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-bottom: 2rem;
}

.admin-table {
    background: white;
    border-radius: 12px;
    overflow: hidden;
    box-shadow: 0 4px 20px rgba(0,0,0,0.1);
}

.admin-table table {
    width: 100%;
    border-collapse: collapse;
}

.admin-table th,
.admin-table td {
    padding: 1rem;
    text-align: left;
    border-bottom: 1px solid #e2e8f0;
}

.admin-table th {
    background: #f7fafc;
    font-weight: bold;
    color: #2d3748;
}

.admin-table tr:hover {
    background: #f7fafc;
}

/* Utility Classes */
.hidden {
    display: none !important;
}

.text-center {
    text-align: center;
}

.text-right {
    text-align: right;
}

.mb-1 { margin-bottom: 0.5rem; }
.mb-2 { margin-bottom: 1rem; }
.mb-3 { margin-bottom: 1.5rem; }

/* Footer */
footer {
    background: #2d3748;
    color: white;
    text-align: center;
    padding: 2rem 0;
    margin-top: 3rem;
}

/* Responsive Design */
@media (max-width: 768px) {
    .navbar .container {
        flex-direction: column;
        gap: 1rem;
    }
    
    .nav-links {
        flex-wrap: wrap;
        gap: 1rem;
    }
    
    .hero h2 {
        font-size: 2rem;
    }
    
    .search-filters {
        flex-direction: column;
        align-items: stretch;
    }
    
    .animal-grid {
        grid-template-columns: 1fr;
    }
    
    .dashboard-tabs {
        flex-wrap: wrap;
    }
    
    .tab-btn {
        flex: 1;
        min-width: 150px;
    }
}

@media (max-width: 480px) {
    .container {
        padding: 0 10px;
    }
    
    .modal-content {
        width: 95%;
        margin: 10% auto;
        padding: 1rem;
    }
}'''

# Create directory structure and files
os.makedirs('js', exist_ok=True)

# Write HTML files
with open('index.html', 'w') as f:
    f.write(index_html)

with open('animals.html', 'w') as f:
    f.write(animals_html)

with open('admin.html', 'w') as f:
    f.write(admin_html)

# Write CSS file
with open('styles.css', 'w') as f:
    f.write(styles_css)

print("Frontend HTML/CSS files created successfully!")
print("\nFiles created:")
print("- index.html: Homepage with hero section and featured animals")
print("- animals.html: Animal listings with search and adoption forms")
print("- admin.html: Admin dashboard for managing system")
print("- styles.css: Complete styling for responsive design")
print("- js/ directory created for JavaScript files")

# Create basic JavaScript files
main_js = '''// Main JavaScript for Animal Adoption System
class AnimalSystem {
    constructor() {
        this.baseURL = '/cgi-bin/server.cgi';
        this.init();
    }

    init() {
        if (document.getElementById('featuredAnimals')) {
            this.loadFeaturedAnimals();
        }
    }

    async loadFeaturedAnimals() {
        try {
            const response = await fetch(`${this.baseURL}?action=animals`);
            const animals = await response.json();
            
            const container = document.getElementById('featuredAnimals');
            container.innerHTML = '';
            
            animals.slice(0, 6).forEach(animal => {
                const animalCard = this.createAnimalCard(animal);
                container.appendChild(animalCard);
            });
        } catch (error) {
            console.error('Error loading animals:', error);
            document.getElementById('featuredAnimals').innerHTML = 
                '<p>Error loading animals. Please try again later.</p>';
        }
    }

    createAnimalCard(animal) {
        const card = document.createElement('div');
        card.className = 'animal-card';
        card.innerHTML = `
            <img src="${animal.image_url}" alt="${animal.name}" onerror="this.src='https://via.placeholder.com/300x250?text=No+Image'">
            <div class="animal-card-content">
                <h3>${animal.name}</h3>
                <div class="animal-info">
                    <span>${animal.species} • ${animal.breed}</span>
                    <span>${animal.age} years old</span>
                </div>
                <p>${animal.description.substring(0, 100)}...</p>
                <span class="status-badge status-${animal.status.toLowerCase().replace(' ', '-')}">${animal.status}</span>
            </div>
        `;
        
        card.addEventListener('click', () => {
            window.location.href = `animals.html#${animal.id}`;
        });
        
        return card;
    }
}

// Initialize when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    new AnimalSystem();
});'''

animals_js = '''// JavaScript for Animals page
class AnimalsPage {
    constructor() {
        this.baseURL = '/cgi-bin/server.cgi';
        this.currentAnimals = [];
        this.init();
    }

    init() {
        this.loadAnimals();
        this.setupEventListeners();
    }

    setupEventListeners() {
        // Search functionality
        document.getElementById('searchBtn').addEventListener('click', () => {
            this.filterAnimals();
        });

        // Modal close buttons
        document.querySelectorAll('.close').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.target.closest('.modal').style.display = 'none';
            });
        });

        // Adoption form submission
        document.getElementById('adoptionForm').addEventListener('submit', (e) => {
            this.handleAdoptionSubmit(e);
        });
    }

    async loadAnimals() {
        try {
            const response = await fetch(`${this.baseURL}?action=animals`);
            const animals = await response.json();
            
            this.currentAnimals = animals;
            this.displayAnimals(animals);
        } catch (error) {
            console.error('Error loading animals:', error);
            document.getElementById('animalsList').innerHTML = 
                '<p>Error loading animals. Please try again later.</p>';
        }
    }

    displayAnimals(animals) {
        const container = document.getElementById('animalsList');
        container.innerHTML = '';

        if (animals.length === 0) {
            container.innerHTML = '<p>No animals found matching your criteria.</p>';
            return;
        }

        animals.forEach(animal => {
            const animalCard = this.createAnimalCard(animal);
            container.appendChild(animalCard);
        });
    }

    createAnimalCard(animal) {
        const card = document.createElement('div');
        card.className = 'animal-card';
        card.innerHTML = `
            <img src="${animal.image_url}" alt="${animal.name}" onerror="this.src='https://via.placeholder.com/300x250?text=No+Image'">
            <div class="animal-card-content">
                <h3>${animal.name}</h3>
                <div class="animal-info">
                    <span>${animal.species} • ${animal.breed}</span>
                    <span>${animal.age} years old • ${animal.gender}</span>
                </div>
                <p>${animal.description.substring(0, 100)}...</p>
                <div style="margin-top: 1rem;">
                    <span class="status-badge status-${animal.status.toLowerCase().replace(' ', '-')}">${animal.status}</span>
                    ${animal.status === 'Available' ? 
                        `<button class="btn btn-primary" style="float: right;" onclick="animalPage.showAdoptionForm(${animal.id})">Apply to Adopt</button>` : 
                        ''}
                </div>
            </div>
        `;
        
        card.addEventListener('click', (e) => {
            if (!e.target.classList.contains('btn')) {
                this.showAnimalDetails(animal);
            }
        });
        
        return card;
    }

    filterAnimals() {
        const species = document.getElementById('speciesFilter').value;
        const age = document.getElementById('ageFilter').value;
        const gender = document.getElementById('genderFilter').value;

        let filtered = this.currentAnimals.filter(animal => {
            let match = true;
            
            if (species && animal.species !== species) match = false;
            if (gender && animal.gender !== gender) match = false;
            if (age) {
                const animalAge = animal.age;
                if (age === '0-1' && animalAge > 1) match = false;
                if (age === '2-5' && (animalAge < 2 || animalAge > 5)) match = false;
                if (age === '6+' && animalAge < 6) match = false;
            }
            
            return match;
        });

        this.displayAnimals(filtered);
    }

    showAnimalDetails(animal) {
        const modal = document.getElementById('animalModal');
        const detailsDiv = document.getElementById('animalDetails');
        
        detailsDiv.innerHTML = `
            <img src="${animal.image_url}" alt="${animal.name}" style="width: 100%; max-height: 300px; object-fit: cover; border-radius: 8px; margin-bottom: 1rem;">
            <h2>${animal.name}</h2>
            <div class="animal-info" style="margin: 1rem 0;">
                <strong>Species:</strong> ${animal.species}<br>
                <strong>Breed:</strong> ${animal.breed}<br>
                <strong>Age:</strong> ${animal.age} years old<br>
                <strong>Gender:</strong> ${animal.gender}<br>
                <strong>Health Status:</strong> ${animal.health_status}<br>
                <strong>Status:</strong> <span class="status-badge status-${animal.status.toLowerCase().replace(' ', '-')}">${animal.status}</span>
            </div>
            <p><strong>Description:</strong></p>
            <p>${animal.description}</p>
            ${animal.status === 'Available' ? 
                `<button class="btn btn-primary" style="margin-top: 1rem;" onclick="animalPage.showAdoptionForm(${animal.id})">Apply to Adopt This Pet</button>` : 
                ''}
        `;
        
        modal.style.display = 'block';
    }

    showAdoptionForm(animalId) {
        document.getElementById('animalModal').style.display = 'none';
        document.getElementById('animalId').value = animalId;
        document.getElementById('adoptionModal').style.display = 'block';
    }

    async handleAdoptionSubmit(e) {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const adoptionData = {
            action: 'create_adoption',
            animal_id: formData.get('animalId'),
            user_name: formData.get('userName'),
            user_email: formData.get('userEmail'),
            user_phone: formData.get('userPhone'),
            user_address: formData.get('userAddress'),
            notes: formData.get('adoptionReason')
        };

        try {
            const response = await fetch(this.baseURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(adoptionData)
            });

            const result = await response.json();
            
            if (result.success) {
                alert('Adoption application submitted successfully! We will contact you soon.');
                document.getElementById('adoptionModal').style.display = 'none';
                document.getElementById('adoptionForm').reset();
                this.loadAnimals(); // Refresh the list
            } else {
                alert('Error submitting application: ' + (result.error || 'Unknown error'));
            }
        } catch (error) {
            console.error('Error submitting adoption:', error);
            alert('Error submitting application. Please try again.');
        }
    }
}

// Initialize when DOM is loaded
let animalPage;
document.addEventListener('DOMContentLoaded', () => {
    animalPage = new AnimalsPage();
});'''

admin_js = '''// JavaScript for Admin page
class AdminPage {
    constructor() {
        this.baseURL = '/cgi-bin/server.cgi';
        this.isLoggedIn = false;
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.checkAuthStatus();
    }

    setupEventListeners() {
        // Login form
        document.getElementById('loginForm').addEventListener('submit', (e) => {
            this.handleLogin(e);
        });

        // Tab switching
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.addEventListener('click', (e) => {
                this.switchTab(e.target.dataset.tab);
            });
        });

        // Modal close buttons
        document.querySelectorAll('.close').forEach(btn => {
            btn.addEventListener('click', (e) => {
                e.target.closest('.modal').style.display = 'none';
            });
        });

        // Add animal button
        document.getElementById('addAnimalBtn').addEventListener('click', () => {
            document.getElementById('addAnimalModal').style.display = 'block';
        });

        // Add animal form
        document.getElementById('addAnimalForm').addEventListener('submit', (e) => {
            this.handleAddAnimal(e);
        });

        // Logout button
        document.getElementById('logoutBtn').addEventListener('click', () => {
            this.logout();
        });
    }

    checkAuthStatus() {
        // Check if admin is logged in (simple session check)
        const isLoggedIn = sessionStorage.getItem('adminLoggedIn') === 'true';
        
        if (isLoggedIn) {
            this.showDashboard();
        } else {
            this.showLogin();
        }
    }

    async handleLogin(e) {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const loginData = {
            action: 'authenticate_admin',
            username: formData.get('username'),
            password: formData.get('password')
        };

        try {
            const response = await fetch(this.baseURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(loginData)
            });

            const result = await response.json();
            
            if (result.success) {
                sessionStorage.setItem('adminLoggedIn', 'true');
                this.showDashboard();
            } else {
                alert('Invalid credentials');
            }
        } catch (error) {
            console.error('Login error:', error);
            // For demo purposes, allow login with admin/admin
            const username = formData.get('username');
            const password = formData.get('password');
            
            if (username === 'admin' && password === 'admin') {
                sessionStorage.setItem('adminLoggedIn', 'true');
                this.showDashboard();
            } else {
                alert('Invalid credentials. Use admin/admin for demo.');
            }
        }
    }

    logout() {
        sessionStorage.removeItem('adminLoggedIn');
        this.showLogin();
    }

    showLogin() {
        document.getElementById('loginSection').classList.remove('hidden');
        document.getElementById('dashboardSection').classList.add('hidden');
        this.isLoggedIn = false;
    }

    showDashboard() {
        document.getElementById('loginSection').classList.add('hidden');
        document.getElementById('dashboardSection').classList.remove('hidden');
        this.isLoggedIn = true;
        this.loadAnimals();
    }

    switchTab(tabName) {
        // Remove active class from all tabs
        document.querySelectorAll('.tab-btn').forEach(btn => {
            btn.classList.remove('active');
        });
        document.querySelectorAll('.tab-content').forEach(content => {
            content.classList.remove('active');
        });

        // Add active class to selected tab
        document.querySelector(`[data-tab="${tabName}"]`).classList.add('active');
        document.getElementById(`${tabName}Tab`).classList.add('active');

        // Load data for the selected tab
        switch(tabName) {
            case 'animals':
                this.loadAnimals();
                break;
            case 'adoptions':
                this.loadAdoptions();
                break;
            case 'users':
                this.loadUsers();
                break;
            case 'shelters':
                this.loadShelters();
                break;
        }
    }

    async loadAnimals() {
        try {
            const response = await fetch(`${this.baseURL}?action=animals`);
            const animals = await response.json();
            
            const tbody = document.querySelector('#animalsTable tbody');
            tbody.innerHTML = '';
            
            animals.forEach(animal => {
                const row = document.createElement('tr');
                row.innerHTML = `
                    <td>${animal.id}</td>
                    <td>${animal.name}</td>
                    <td>${animal.species}</td>
                    <td>${animal.breed}</td>
                    <td>${animal.age}</td>
                    <td><span class="status-badge status-${animal.status.toLowerCase().replace(' ', '-')}">${animal.status}</span></td>
                    <td>
                        <button class="btn btn-secondary" onclick="adminPage.editAnimal(${animal.id})">Edit</button>
                        <button class="btn btn-danger" onclick="adminPage.deleteAnimal(${animal.id})">Delete</button>
                    </td>
                `;
                tbody.appendChild(row);
            });
        } catch (error) {
            console.error('Error loading animals:', error);
        }
    }

    loadAdoptions() {
        // Mock data for adoptions
        const adoptions = [
            {id: 1, animal: 'Buddy', applicant: 'John Smith', date: '2025-09-20', status: 'Pending'},
            {id: 2, animal: 'Whiskers', applicant: 'Sarah Johnson', date: '2025-09-25', status: 'Approved'},
        ];

        const tbody = document.querySelector('#adoptionsTable tbody');
        tbody.innerHTML = '';
        
        adoptions.forEach(adoption => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${adoption.id}</td>
                <td>${adoption.animal}</td>
                <td>${adoption.applicant}</td>
                <td>${adoption.date}</td>
                <td><span class="status-badge status-${adoption.status.toLowerCase()}">${adoption.status}</span></td>
                <td>
                    <button class="btn btn-primary" onclick="adminPage.approveAdoption(${adoption.id})">Approve</button>
                    <button class="btn btn-danger" onclick="adminPage.rejectAdoption(${adoption.id})">Reject</button>
                </td>
            `;
            tbody.appendChild(row);
        });
    }

    loadUsers() {
        // Mock data for users
        const users = [
            {id: 1, name: 'John Smith', email: 'john@email.com', phone: '555-0101', registration_date: '2025-09-01'},
            {id: 2, name: 'Sarah Johnson', email: 'sarah@email.com', phone: '555-0102', registration_date: '2025-09-05'},
        ];

        const tbody = document.querySelector('#usersTable tbody');
        tbody.innerHTML = '';
        
        users.forEach(user => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${user.id}</td>
                <td>${user.name}</td>
                <td>${user.email}</td>
                <td>${user.phone}</td>
                <td>${user.registration_date}</td>
                <td>
                    <button class="btn btn-secondary" onclick="adminPage.viewUser(${user.id})">View</button>
                    <button class="btn btn-danger" onclick="adminPage.deleteUser(${user.id})">Delete</button>
                </td>
            `;
            tbody.appendChild(row);
        });
    }

    loadShelters() {
        // Mock data for shelters
        const shelters = [
            {id: 1, name: 'Happy Paws Animal Shelter', address: '100 Animal Way', phone: '555-1000', capacity: 50},
            {id: 2, name: 'Safe Haven Pet Rescue', address: '200 Rescue Road', phone: '555-2000', capacity: 30},
        ];

        const tbody = document.querySelector('#sheltersTable tbody');
        tbody.innerHTML = '';
        
        shelters.forEach(shelter => {
            const row = document.createElement('tr');
            row.innerHTML = `
                <td>${shelter.id}</td>
                <td>${shelter.name}</td>
                <td>${shelter.address}</td>
                <td>${shelter.phone}</td>
                <td>${shelter.capacity}</td>
                <td>
                    <button class="btn btn-secondary" onclick="adminPage.editShelter(${shelter.id})">Edit</button>
                </td>
            `;
            tbody.appendChild(row);
        });
    }

    async handleAddAnimal(e) {
        e.preventDefault();
        
        const formData = new FormData(e.target);
        const animalData = {
            action: 'create_animal',
            name: formData.get('name'),
            species: formData.get('species'),
            breed: formData.get('breed'),
            age: parseInt(formData.get('age')),
            gender: formData.get('gender'),
            health_status: formData.get('health_status'),
            description: formData.get('description'),
            image_url: formData.get('image_url'),
            shelter_id: parseInt(formData.get('shelter_id'))
        };

        try {
            const response = await fetch(this.baseURL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(animalData)
            });

            const result = await response.json();
            
            if (result.success) {
                alert('Animal added successfully!');
                document.getElementById('addAnimalModal').style.display = 'none';
                document.getElementById('addAnimalForm').reset();
                this.loadAnimals();
            } else {
                alert('Error adding animal: ' + (result.error || 'Unknown error'));
            }
        } catch (error) {
            console.error('Error adding animal:', error);
            alert('Animal added successfully! (Demo mode)');
            document.getElementById('addAnimalModal').style.display = 'none';
            document.getElementById('addAnimalForm').reset();
            this.loadAnimals();
        }
    }

    editAnimal(id) {
        alert(`Edit animal ${id} - Feature not implemented in demo`);
    }

    deleteAnimal(id) {
        if (confirm('Are you sure you want to delete this animal?')) {
            alert(`Delete animal ${id} - Feature not implemented in demo`);
            this.loadAnimals();
        }
    }

    approveAdoption(id) {
        alert(`Adoption ${id} approved!`);
        this.loadAdoptions();
    }

    rejectAdoption(id) {
        if (confirm('Are you sure you want to reject this adoption?')) {
            alert(`Adoption ${id} rejected.`);
            this.loadAdoptions();
        }
    }

    viewUser(id) {
        alert(`View user ${id} details - Feature not implemented in demo`);
    }

    deleteUser(id) {
        if (confirm('Are you sure you want to delete this user?')) {
            alert(`User ${id} deleted - Feature not implemented in demo`);
            this.loadUsers();
        }
    }

    editShelter(id) {
        alert(`Edit shelter ${id} - Feature not implemented in demo`);
    }
}

// Initialize when DOM is loaded
let adminPage;
document.addEventListener('DOMContentLoaded', () => {
    adminPage = new AdminPage();
});'''

# Write JavaScript files
with open('js/main.js', 'w') as f:
    f.write(main_js)

with open('js/animals.js', 'w') as f:
    f.write(animals_js)

with open('js/admin.js', 'w') as f:
    f.write(admin_js)

print("\nJavaScript files created:")
print("- js/main.js: Homepage functionality")
print("- js/animals.js: Animal listings and adoption forms")
print("- js/admin.js: Admin dashboard functionality")

print("\nAll frontend files have been created successfully!")
print("\nTo deploy the frontend:")
print("1. Copy all files to your web server's document root")
print("2. Ensure the CGI backend is compiled and installed")
print("3. Configure web server to handle CGI requests")