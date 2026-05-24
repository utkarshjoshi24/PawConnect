// Main JavaScript for Animal Adoption System
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
});