// Animal Adoption Management System - JavaScript
class AnimalAdoptionSystem {
    constructor() {
        // Initialize data from the provided JSON
        this.data = {
            animals: [
                {
                    id: 1, name: "Buddy", species: "Dog", breed: "Golden Retriever", age: 3, gender: "Male",
                    health_status: "Healthy", status: "Available",
                    description: "Buddy is a friendly and energetic Golden Retriever who loves playing fetch and swimming. He's great with children and other dogs. Buddy is house-trained and knows basic commands.",
                    image_url: "https://images.unsplash.com/photo-1552053831-71594a27632d?w=400",
                    shelter_id: 1, date_added: "2025-09-15", personality: ["Friendly", "Energetic", "Loyal"], adoption_fee: 250
                },
                {
                    id: 2, name: "Whiskers", species: "Cat", breed: "Persian", age: 2, gender: "Female",
                    health_status: "Healthy", status: "Available",
                    description: "Whiskers is a calm and affectionate Persian cat who loves to cuddle and purr. She's perfect for a quiet home and gets along well with other cats.",
                    image_url: "https://images.unsplash.com/photo-1574144611937-0df059b5ef3e?w=400",
                    shelter_id: 1, date_added: "2025-09-20", personality: ["Calm", "Affectionate", "Gentle"], adoption_fee: 150
                },
                {
                    id: 3, name: "Max", species: "Dog", breed: "German Shepherd", age: 4, gender: "Male",
                    health_status: "Under Treatment", status: "Not Available",
                    description: "Max is a protective and loyal German Shepherd currently receiving medical treatment. He would be perfect for an experienced dog owner.",
                    image_url: "https://images.unsplash.com/photo-1589941013453-ec89f33b5e95?w=400",
                    shelter_id: 2, date_added: "2025-09-10", personality: ["Protective", "Loyal", "Intelligent"], adoption_fee: 300
                },
                {
                    id: 4, name: "Luna", species: "Cat", breed: "Siamese", age: 1, gender: "Female",
                    health_status: "Healthy", status: "Available",
                    description: "Luna is a playful Siamese kitten who loves toys and climbing. She's very social and would do well with an active family.",
                    image_url: "https://images.unsplash.com/photo-1606214174585-fe31582dc6ee?w=400",
                    shelter_id: 1, date_added: "2025-09-25", personality: ["Playful", "Social", "Active"], adoption_fee: 125
                },
                {
                    id: 5, name: "Rocky", species: "Dog", breed: "Bulldog", age: 5, gender: "Male",
                    health_status: "Healthy", status: "Adopted",
                    description: "Rocky was a gentle and calm Bulldog who found his forever home. He loved relaxing and being around people.",
                    image_url: "https://images.unsplash.com/photo-1583337130417-3346a1be7dee?w=400",
                    shelter_id: 2, date_added: "2025-08-30", personality: ["Gentle", "Calm", "Loving"], adoption_fee: 200
                }
            ],
            shelters: [
                { id: 1, name: "Happy Paws Animal Shelter", address: "100 Animal Way, Springfield", phone: "555-1000", email: "contact@happypaws.org", capacity: 50, website: "www.happypaws.org" },
                { id: 2, name: "Safe Haven Pet Rescue", address: "200 Rescue Road, Springfield", phone: "555-2000", email: "info@safehavenpets.org", capacity: 30, website: "www.safehavenpets.org" },
                { id: 3, name: "Loving Hearts Animal Sanctuary", address: "300 Love Lane, Springfield", phone: "555-3000", email: "help@lovinghearts.org", capacity: 75, website: "www.lovinghearts.org" }
            ],
            users: [
                { id: 1, name: "John Smith", email: "john@email.com", phone: "555-0101", address: "123 Main St", city: "Springfield", registration_date: "2025-09-01" },
                { id: 2, name: "Sarah Johnson", email: "sarah@email.com", phone: "555-0102", address: "456 Oak Ave", city: "Springfield", registration_date: "2025-09-05" }
            ],
            adoptions: [
                { id: 1, user_id: 1, animal_id: 5, application_date: "2025-09-01", status: "Approved", approval_date: "2025-09-05", notes: "Great match, experienced dog owner" },
                { id: 2, user_id: 2, animal_id: 1, application_date: "2025-09-20", status: "Pending", approval_date: null, notes: "Application under review" }
            ],
            admins: [
                { id: 1, username: "admin", email: "admin@pethaven.com", password: "admin123" }
            ],
            stats: { total_animals: 150, adopted_this_month: 23, available_now: 89, shelters_partnered: 3 }
        };

        // Current user session
        this.currentUser = null;
        this.currentAdmin = null;
        this.selectedAnimal = null;

        // Initialize the application
        this.init();
    }

    init() {
        this.setupEventListeners();
        this.loadHomePage();
        this.updateStats();
        this.checkUserSession();
    }

    setupEventListeners() {
        // Navigation
        document.querySelectorAll('[data-page]').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                this.navigateToPage(link.dataset.page);
            });
        });

        // Navigation links
        document.querySelectorAll('.nav-link').forEach(link => {
            link.addEventListener('click', (e) => {
                e.preventDefault();
                this.setActiveNavLink(link);
                this.navigateToPage(link.dataset.page);
            });
        });

        // Modal controls
        document.querySelectorAll('.modal-close, .modal-overlay').forEach(el => {
            el.addEventListener('click', () => this.closeModal());
        });

        // Authentication
        document.getElementById('loginBtn').addEventListener('click', () => this.openModal('loginModal'));
        document.getElementById('registerBtn').addEventListener('click', () => this.openModal('registerModal'));
        document.getElementById('logoutBtn').addEventListener('click', () => this.logout());
        document.getElementById('dashboardBtn').addEventListener('click', () => this.openDashboard());

        // Forms
        document.getElementById('loginForm').addEventListener('submit', (e) => this.handleLogin(e));
        document.getElementById('registerForm').addEventListener('submit', (e) => this.handleRegister(e));
        document.getElementById('adoptionForm').addEventListener('submit', (e) => this.handleAdoptionApplication(e));

        // Search and filters
        document.getElementById('searchInput').addEventListener('input', () => this.filterAnimals());
        document.getElementById('speciesFilter').addEventListener('change', () => this.filterAnimals());
        document.getElementById('ageFilter').addEventListener('change', () => this.filterAnimals());
        document.getElementById('statusFilter').addEventListener('change', () => this.filterAnimals());

        // Dashboard navigation
        document.querySelectorAll('.menu-item').forEach(item => {
            item.addEventListener('click', (e) => {
                e.preventDefault();
                this.switchDashboardSection(item);
            });
        });

        // Admin actions
        document.getElementById('addAnimalBtn').addEventListener('click', () => this.showAddAnimalForm());
        document.getElementById('applyAdoptBtn').addEventListener('click', () => this.showAdoptionForm());
    }

    // Navigation System
    navigateToPage(pageId) {
        // Hide all pages
        document.querySelectorAll('.page').forEach(page => page.classList.remove('active'));
        
        // Handle special cases for dashboard pages
        let targetPageId;
        if (pageId === 'userDashboard' || pageId === 'adminDashboard') {
            targetPageId = pageId;
        } else {
            targetPageId = pageId + 'Page';
        }
        
        // Show selected page
        const targetPage = document.getElementById(targetPageId);
        if (targetPage) {
            targetPage.classList.add('active');
            
            // Load page-specific content
            switch(pageId) {
                case 'home':
                    this.loadHomePage();
                    break;
                case 'animals':
                    this.loadAnimalsPage();
                    break;
                case 'shelters':
                    this.loadSheltersPage();
                    break;
                case 'about':
                    // About page is static
                    break;
                case 'userDashboard':
                    this.loadUserDashboard();
                    break;
                case 'adminDashboard':
                    this.loadAdminDashboard();
                    break;
            }
        }
    }

    setActiveNavLink(activeLink) {
        document.querySelectorAll('.nav-link').forEach(link => link.classList.remove('active'));
        activeLink.classList.add('active');
    }

    // Page Loading Functions
    loadHomePage() {
        this.loadFeaturedAnimals();
        this.updateStats();
    }

    loadFeaturedAnimals() {
        const container = document.getElementById('featuredAnimalsGrid');
        const availableAnimals = this.data.animals.filter(animal => animal.status === 'Available').slice(0, 3);
        
        container.innerHTML = availableAnimals.map(animal => this.createAnimalCard(animal)).join('');
        
        // Add click handlers
        container.querySelectorAll('.animal-card').forEach(card => {
            card.addEventListener('click', () => {
                const animalId = parseInt(card.dataset.animalId);
                this.showAnimalDetails(animalId);
            });
        });
    }

    loadAnimalsPage() {
        this.filterAnimals();
    }

    loadSheltersPage() {
        const container = document.getElementById('sheltersGrid');
        container.innerHTML = this.data.shelters.map(shelter => this.createShelterCard(shelter)).join('');
    }

    filterAnimals() {
        const searchTerm = document.getElementById('searchInput').value.toLowerCase();
        const speciesFilter = document.getElementById('speciesFilter').value;
        const ageFilter = document.getElementById('ageFilter').value;
        const statusFilter = document.getElementById('statusFilter').value;

        let filteredAnimals = this.data.animals.filter(animal => {
            const matchesSearch = !searchTerm || 
                animal.name.toLowerCase().includes(searchTerm) ||
                animal.breed.toLowerCase().includes(searchTerm) ||
                animal.species.toLowerCase().includes(searchTerm);

            const matchesSpecies = !speciesFilter || animal.species === speciesFilter;
            
            const matchesAge = !ageFilter || this.checkAgeRange(animal.age, ageFilter);
            
            const matchesStatus = !statusFilter || animal.status === statusFilter;

            return matchesSearch && matchesSpecies && matchesAge && matchesStatus;
        });

        const container = document.getElementById('animalsGrid');
        if (filteredAnimals.length === 0) {
            container.innerHTML = '<div class="empty-state"><h3>No animals found</h3><p>Try adjusting your search criteria.</p></div>';
        } else {
            container.innerHTML = filteredAnimals.map(animal => this.createAnimalCard(animal)).join('');
            
            // Add click handlers
            container.querySelectorAll('.animal-card').forEach(card => {
                card.addEventListener('click', () => {
                    const animalId = parseInt(card.dataset.animalId);
                    this.showAnimalDetails(animalId);
                });
            });
        }
    }

    checkAgeRange(age, range) {
        switch(range) {
            case 'young': return age <= 2;
            case 'adult': return age >= 3 && age <= 7;
            case 'senior': return age >= 8;
            default: return true;
        }
    }

    // Card Creation Functions
    createAnimalCard(animal) {
        const statusClass = animal.status.toLowerCase().replace(' ', '-');
        return `
            <div class="animal-card" data-animal-id="${animal.id}">
                <div class="animal-card-image">
                    <img src="${animal.image_url}" alt="${animal.name}" loading="lazy">
                    <div class="animal-status ${statusClass}">${animal.status}</div>
                </div>
                <div class="animal-card-content">
                    <h3>${animal.name}</h3>
                    <div class="animal-meta">
                        <span class="meta-tag">${animal.species}</span>
                        <span class="meta-tag">${animal.breed}</span>
                        <span class="meta-tag">${animal.age} years</span>
                        <span class="meta-tag">${animal.gender}</span>
                    </div>
                    <p class="animal-description">${animal.description}</p>
                    <div class="adoption-fee">Adoption Fee: $${animal.adoption_fee}</div>
                </div>
            </div>
        `;
    }

    createShelterCard(shelter) {
        return `
            <div class="shelter-card">
                <h3>${shelter.name}</h3>
                <div class="shelter-info">
                    <p><strong>Address:</strong> ${shelter.address}</p>
                    <p><strong>Phone:</strong> ${shelter.phone}</p>
                    <p><strong>Capacity:</strong> ${shelter.capacity} animals</p>
                </div>
                <div class="shelter-contact">
                    <a href="mailto:${shelter.email}">Email Us</a> | 
                    <a href="http://${shelter.website}" target="_blank">Visit Website</a>
                </div>
            </div>
        `;
    }

    // Modal Management
    openModal(modalId) {
        const modal = document.getElementById(modalId);
        if (modal) {
            modal.classList.remove('hidden');
            document.body.style.overflow = 'hidden';
        }
    }

    closeModal() {
        document.querySelectorAll('.modal').forEach(modal => {
            modal.classList.add('hidden');
        });
        document.body.style.overflow = '';
    }

    // Animal Details
    showAnimalDetails(animalId) {
        const animal = this.data.animals.find(a => a.id === animalId);
        if (!animal) return;

        this.selectedAnimal = animal;

        // Populate modal with animal details
        document.getElementById('animalModalName').textContent = animal.name;
        document.getElementById('animalModalImage').src = animal.image_url;
        document.getElementById('animalModalSpecies').textContent = animal.species;
        document.getElementById('animalModalBreed').textContent = animal.breed;
        document.getElementById('animalModalAge').textContent = animal.age;
        document.getElementById('animalModalGender').textContent = animal.gender;
        document.getElementById('animalModalHealth').textContent = animal.health_status;
        document.getElementById('animalModalFee').textContent = animal.adoption_fee;
        document.getElementById('animalModalDescription').textContent = animal.description;

        // Personality tags
        const personalityContainer = document.getElementById('animalModalPersonality');
        personalityContainer.innerHTML = animal.personality.map(trait => 
            `<span class="personality-tag">${trait}</span>`
        ).join('');

        // Show/hide apply button based on availability and login status
        const applyBtn = document.getElementById('applyAdoptBtn');
        if (animal.status !== 'Available') {
            applyBtn.style.display = 'none';
        } else if (!this.currentUser) {
            applyBtn.textContent = 'Login to Apply';
            applyBtn.onclick = () => {
                this.closeModal();
                this.openModal('loginModal');
            };
        } else {
            applyBtn.style.display = 'block';
            applyBtn.textContent = 'Apply to Adopt';
            applyBtn.onclick = () => this.showAdoptionForm();
        }

        this.openModal('animalModal');
    }

    // Authentication
    handleLogin(e) {
        e.preventDefault();
        const email = document.getElementById('loginEmail').value;
        const password = document.getElementById('loginPassword').value;
        const isAdmin = document.getElementById('isAdmin').checked;

        if (isAdmin) {
            // Admin login
            const admin = this.data.admins.find(a => a.email === email && a.password === password);
            if (admin) {
                this.currentAdmin = admin;
                this.updateAuthUI();
                this.closeModal();
                this.showNotification('Admin login successful!', 'success');
            } else {
                this.showNotification('Invalid admin credentials!', 'error');
            }
        } else {
            // User login
            const user = this.data.users.find(u => u.email === email);
            if (user) {
                this.currentUser = user;
                this.updateAuthUI();
                this.closeModal();
                this.showNotification('Login successful!', 'success');
            } else {
                this.showNotification('Invalid credentials!', 'error');
            }
        }
    }

    handleRegister(e) {
        e.preventDefault();
        const formData = {
            name: document.getElementById('registerName').value,
            email: document.getElementById('registerEmail').value,
            phone: document.getElementById('registerPhone').value,
            address: document.getElementById('registerAddress').value,
            city: document.getElementById('registerCity').value,
            password: document.getElementById('registerPassword').value
        };

        // Check if email already exists
        if (this.data.users.find(u => u.email === formData.email)) {
            this.showNotification('Email already registered!', 'error');
            return;
        }

        // Add new user
        const newUser = {
            id: this.data.users.length + 1,
            ...formData,
            registration_date: new Date().toISOString().split('T')[0]
        };

        this.data.users.push(newUser);
        this.currentUser = newUser;
        this.updateAuthUI();
        this.closeModal();
        this.showNotification('Registration successful!', 'success');
    }

    logout() {
        this.currentUser = null;
        this.currentAdmin = null;
        this.updateAuthUI();
        this.navigateToPage('home');
        this.showNotification('Logged out successfully!', 'success');
    }

    updateAuthUI() {
        const loginBtn = document.getElementById('loginBtn');
        const registerBtn = document.getElementById('registerBtn');
        const userMenu = document.getElementById('userMenu');
        const userName = document.getElementById('userName');

        if (this.currentUser || this.currentAdmin) {
            loginBtn.style.display = 'none';
            registerBtn.style.display = 'none';
            userMenu.classList.remove('hidden');
            userName.textContent = (this.currentUser?.name || this.currentAdmin?.username || 'User');
        } else {
            loginBtn.style.display = 'block';
            registerBtn.style.display = 'block';
            userMenu.classList.add('hidden');
        }
    }

    checkUserSession() {
        // In a real app, this would check stored session data
        this.updateAuthUI();
    }

    // Adoption System
    showAdoptionForm() {
        if (!this.currentUser) {
            this.showNotification('Please login to apply for adoption!', 'error');
            return;
        }

        if (!this.selectedAnimal) {
            this.showNotification('No animal selected!', 'error');
            return;
        }

        this.closeModal();
        this.openModal('adoptionModal');
    }

    handleAdoptionApplication(e) {
        e.preventDefault();
        
        const applicationData = {
            id: this.data.adoptions.length + 1,
            user_id: this.currentUser.id,
            animal_id: this.selectedAnimal.id,
            application_date: new Date().toISOString().split('T')[0],
            status: 'Pending',
            approval_date: null,
            reason: document.getElementById('adoptionReason').value,
            experience: document.getElementById('adoptionExperience').value,
            living_situation: document.getElementById('adoptionLiving').value,
            notes: document.getElementById('adoptionNotes').value
        };

        this.data.adoptions.push(applicationData);
        this.closeModal();
        this.showNotification('Adoption application submitted successfully!', 'success');
        
        // Reset form
        document.getElementById('adoptionForm').reset();
    }

    // Dashboard System
    openDashboard() {
        if (this.currentAdmin) {
            this.navigateToPage('adminDashboard');
        } else if (this.currentUser) {
            this.navigateToPage('userDashboard');
        }
    }

    switchDashboardSection(activeItem) {
        // Update menu
        document.querySelectorAll('.menu-item').forEach(item => item.classList.remove('active'));
        activeItem.classList.add('active');

        // Show section
        const sectionId = activeItem.dataset.section;
        document.querySelectorAll('.dashboard-section').forEach(section => section.classList.remove('active'));
        document.getElementById(sectionId + 'Section').classList.add('active');

        // Load section data
        this.loadDashboardSection(sectionId);
    }

    loadUserDashboard() {
        this.loadUserProfile();
        this.loadUserApplications();
    }

    loadUserProfile() {
        if (!this.currentUser) return;

        document.getElementById('profileName').value = this.currentUser.name;
        document.getElementById('profileEmail').value = this.currentUser.email;
        document.getElementById('profilePhone').value = this.currentUser.phone || '';
        document.getElementById('profileAddress').value = this.currentUser.address || '';
    }

    loadUserApplications() {
        if (!this.currentUser) return;

        const userApplications = this.data.adoptions.filter(app => app.user_id === this.currentUser.id);
        const container = document.getElementById('userApplications');

        if (userApplications.length === 0) {
            container.innerHTML = '<div class="empty-state"><h3>No Applications</h3><p>You haven\'t submitted any adoption applications yet.</p></div>';
        } else {
            container.innerHTML = userApplications.map(app => {
                const animal = this.data.animals.find(a => a.id === app.animal_id);
                return `
                    <div class="application-card">
                        <div class="application-header">
                            <h4>Application for ${animal?.name || 'Unknown Animal'}</h4>
                            <span class="application-status ${app.status.toLowerCase()}">${app.status}</span>
                        </div>
                        <div class="application-meta">
                            <p>Applied: ${app.application_date}</p>
                            ${app.approval_date ? `<p>Processed: ${app.approval_date}</p>` : ''}
                            ${app.notes ? `<p>Notes: ${app.notes}</p>` : ''}
                        </div>
                    </div>
                `;
            }).join('');
        }
    }

    loadAdminDashboard() {
        // Load all admin sections on initial load
        this.loadAdminAnimals();
        this.loadAdminApplications();
        this.loadAdminUsers();
        this.loadAdminShelters();
        this.updateAdminStats();
    }

    loadDashboardSection(sectionId) {
        switch(sectionId) {
            case 'admin-animals':
                this.loadAdminAnimals();
                break;
            case 'admin-applications':
                this.loadAdminApplications();
                break;
            case 'admin-users':
                this.loadAdminUsers();
                break;
            case 'admin-shelters':
                this.loadAdminShelters();
                break;
            case 'admin-stats':
                this.updateAdminStats();
                break;
            case 'applications':
                this.loadUserApplications();
                break;
            case 'profile':
                this.loadUserProfile();
                break;
        }
    }

    loadAdminAnimals() {
        const table = document.getElementById('adminAnimalsTable');
        if (!table) return;
        
        const tbody = table.querySelector('tbody');
        tbody.innerHTML = this.data.animals.map(animal => `
            <tr>
                <td>${animal.id}</td>
                <td>${animal.name}</td>
                <td>${animal.species}</td>
                <td>${animal.breed}</td>
                <td>${animal.age}</td>
                <td><span class="status ${animal.status.toLowerCase().replace(' ', '-')}">${animal.status}</span></td>
                <td>
                    <div class="table-actions">
                        <button class="btn btn--outline btn-table" onclick="app.editAnimal(${animal.id})">Edit</button>
                        <button class="btn btn--secondary btn-table" onclick="app.deleteAnimal(${animal.id})">Delete</button>
                    </div>
                </td>
            </tr>
        `).join('');
    }

    loadAdminApplications() {
        const table = document.getElementById('adminApplicationsTable');
        if (!table) return;
        
        const tbody = table.querySelector('tbody');
        tbody.innerHTML = this.data.adoptions.map(app => {
            const user = this.data.users.find(u => u.id === app.user_id);
            const animal = this.data.animals.find(a => a.id === app.animal_id);
            return `
                <tr>
                    <td>${app.id}</td>
                    <td>${user?.name || 'Unknown'}</td>
                    <td>${animal?.name || 'Unknown'}</td>
                    <td>${app.application_date}</td>
                    <td><span class="status ${app.status.toLowerCase()}">${app.status}</span></td>
                    <td>
                        <div class="table-actions">
                            ${app.status === 'Pending' ? 
                                `<button class="btn btn--primary btn-table" onclick="app.approveApplication(${app.id})">Approve</button>
                                 <button class="btn btn--secondary btn-table" onclick="app.rejectApplication(${app.id})">Reject</button>` :
                                `<button class="btn btn--outline btn-table" onclick="app.viewApplication(${app.id})">View</button>`
                            }
                        </div>
                    </td>
                </tr>
            `;
        }).join('');
    }

    loadAdminUsers() {
        const table = document.getElementById('adminUsersTable');
        if (!table) return;
        
        const tbody = table.querySelector('tbody');
        tbody.innerHTML = this.data.users.map(user => `
            <tr>
                <td>${user.id}</td>
                <td>${user.name}</td>
                <td>${user.email}</td>
                <td>${user.phone || 'N/A'}</td>
                <td>${user.registration_date}</td>
                <td>
                    <div class="table-actions">
                        <button class="btn btn--outline btn-table" onclick="app.viewUser(${user.id})">View</button>
                    </div>
                </td>
            </tr>
        `).join('');
    }

    loadAdminShelters() {
        const table = document.getElementById('adminSheltersTable');
        if (!table) return;
        
        const tbody = table.querySelector('tbody');
        tbody.innerHTML = this.data.shelters.map(shelter => `
            <tr>
                <td>${shelter.id}</td>
                <td>${shelter.name}</td>
                <td>${shelter.address}</td>
                <td>${shelter.phone}</td>
                <td>${shelter.email}</td>
                <td>${shelter.capacity}</td>
            </tr>
        `).join('');
    }

    // Admin Actions
    approveApplication(appId) {
        const application = this.data.adoptions.find(app => app.id === appId);
        if (application) {
            application.status = 'Approved';
            application.approval_date = new Date().toISOString().split('T')[0];
            
            // Update animal status
            const animal = this.data.animals.find(a => a.id === application.animal_id);
            if (animal) {
                animal.status = 'Adopted';
            }
            
            this.loadAdminApplications();
            this.loadAdminAnimals();
            this.showNotification('Application approved successfully!', 'success');
        }
    }

    rejectApplication(appId) {
        const application = this.data.adoptions.find(app => app.id === appId);
        if (application) {
            application.status = 'Rejected';
            application.approval_date = new Date().toISOString().split('T')[0];
            this.loadAdminApplications();
            this.showNotification('Application rejected.', 'success');
        }
    }

    editAnimal(animalId) {
        this.showNotification('Edit functionality would be implemented here.', 'success');
    }

    deleteAnimal(animalId) {
        if (confirm('Are you sure you want to delete this animal?')) {
            this.data.animals = this.data.animals.filter(animal => animal.id !== animalId);
            this.loadAdminAnimals();
            this.showNotification('Animal deleted successfully!', 'success');
        }
    }

    showAddAnimalForm() {
        this.showNotification('Add animal form would be implemented here.', 'success');
    }

    viewApplication(appId) {
        this.showNotification('Application details would be shown here.', 'success');
    }

    viewUser(userId) {
        this.showNotification('User details would be shown here.', 'success');
    }

    // Statistics
    updateStats() {
        document.getElementById('totalAnimals').textContent = this.data.stats.total_animals;
        document.getElementById('adoptedThisMonth').textContent = this.data.stats.adopted_this_month;
        document.getElementById('availableNow').textContent = this.data.stats.available_now;
    }

    updateAdminStats() {
        const totalAnimals = this.data.animals.length;
        const totalUsers = this.data.users.length;
        const pendingApplications = this.data.adoptions.filter(app => app.status === 'Pending').length;
        const approvedApplications = this.data.adoptions.filter(app => app.status === 'Approved').length;

        document.getElementById('adminTotalAnimals').textContent = totalAnimals;
        document.getElementById('adminTotalUsers').textContent = totalUsers;
        document.getElementById('adminPendingApplications').textContent = pendingApplications;
        document.getElementById('adminApprovedApplications').textContent = approvedApplications;
    }

    // Notifications
    showNotification(message, type = 'success') {
        // Remove existing notifications
        document.querySelectorAll('.notification').forEach(n => n.remove());

        const notification = document.createElement('div');
        notification.className = `notification ${type}`;
        notification.textContent = message;
        
        document.body.appendChild(notification);
        
        // Show notification
        setTimeout(() => notification.classList.add('show'), 100);
        
        // Hide notification after 3 seconds
        setTimeout(() => {
            notification.classList.remove('show');
            setTimeout(() => notification.remove(), 300);
        }, 3000);
    }
}

// Initialize the application when DOM is loaded
document.addEventListener('DOMContentLoaded', () => {
    window.app = new AnimalAdoptionSystem();
});

// Handle page refresh and navigation
window.addEventListener('beforeunload', () => {
    // In a real app, you might want to save session data here
});

// Prevent form submission on Enter key in search
document.addEventListener('keydown', (e) => {
    if (e.key === 'Enter' && e.target.id === 'searchInput') {
        e.preventDefault();
    }
});