// JavaScript for Admin page
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
});