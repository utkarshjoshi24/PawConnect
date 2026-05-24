// JavaScript for Animals page
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
});