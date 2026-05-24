# Create sample data for database tables to demonstrate the structure
import json
import csv

# Sample data for the animal adoption database tables
animals_data = [
    {"id": 1, "name": "Buddy", "species": "Dog", "breed": "Golden Retriever", "age": 3, "gender": "Male", "health_status": "Healthy", "status": "Available", "description": "Friendly and energetic dog", "image_url": "buddy.jpg", "shelter_id": 1, "date_added": "2025-09-15"},
    {"id": 2, "name": "Whiskers", "species": "Cat", "breed": "Persian", "age": 2, "gender": "Female", "health_status": "Healthy", "status": "Available", "description": "Calm and affectionate cat", "image_url": "whiskers.jpg", "shelter_id": 1, "date_added": "2025-09-20"},
    {"id": 3, "name": "Max", "species": "Dog", "breed": "German Shepherd", "age": 4, "gender": "Male", "health_status": "Under Treatment", "status": "Not Available", "description": "Protective and loyal", "image_url": "max.jpg", "shelter_id": 2, "date_added": "2025-09-10"},
    {"id": 4, "name": "Luna", "species": "Cat", "breed": "Siamese", "age": 1, "gender": "Female", "health_status": "Healthy", "status": "Available", "description": "Playful kitten", "image_url": "luna.jpg", "shelter_id": 1, "date_added": "2025-09-25"},
    {"id": 5, "name": "Rocky", "species": "Dog", "breed": "Bulldog", "age": 5, "gender": "Male", "health_status": "Healthy", "status": "Adopted", "description": "Gentle and calm", "image_url": "rocky.jpg", "shelter_id": 2, "date_added": "2025-08-30"}
]

users_data = [
    {"id": 1, "name": "John Smith", "email": "john@email.com", "password": "hashed_password", "phone": "555-0101", "address": "123 Main St", "city": "Springfield", "registration_date": "2025-09-01"},
    {"id": 2, "name": "Sarah Johnson", "email": "sarah@email.com", "password": "hashed_password", "phone": "555-0102", "address": "456 Oak Ave", "city": "Springfield", "registration_date": "2025-09-05"},
    {"id": 3, "name": "Mike Davis", "email": "mike@email.com", "password": "hashed_password", "phone": "555-0103", "address": "789 Pine St", "city": "Riverside", "registration_date": "2025-09-12"},
    {"id": 4, "name": "Emma Wilson", "email": "emma@email.com", "password": "hashed_password", "phone": "555-0104", "address": "321 Elm Dr", "city": "Springfield", "registration_date": "2025-09-18"}
]

admins_data = [
    {"id": 1, "username": "admin1", "password": "hashed_admin_password", "email": "admin1@shelter.org", "role": "Super Admin", "created_date": "2025-08-01"},
    {"id": 2, "username": "shelter_manager", "password": "hashed_admin_password", "email": "manager@shelter.org", "role": "Shelter Manager", "created_date": "2025-08-15"},
    {"id": 3, "username": "volunteer_coord", "password": "hashed_admin_password", "email": "volunteer@shelter.org", "role": "Volunteer Coordinator", "created_date": "2025-09-01"}
]

adoptions_data = [
    {"id": 1, "user_id": 1, "animal_id": 5, "application_date": "2025-09-01", "status": "Approved", "approval_date": "2025-09-05", "notes": "Great match, experienced dog owner"},
    {"id": 2, "user_id": 2, "animal_id": 1, "application_date": "2025-09-20", "status": "Pending", "approval_date": None, "notes": "Application under review"},
    {"id": 3, "user_id": 3, "animal_id": 2, "application_date": "2025-09-25", "status": "Pending", "approval_date": None, "notes": "First-time pet owner, needs counseling"},
    {"id": 4, "user_id": 4, "animal_id": 4, "application_date": "2025-09-28", "status": "Rejected", "approval_date": "2025-09-30", "notes": "Housing not suitable for pets"}
]

shelters_data = [
    {"id": 1, "name": "Happy Paws Animal Shelter", "address": "100 Animal Way", "phone": "555-1000", "email": "contact@happypaws.org", "capacity": 50},
    {"id": 2, "name": "Safe Haven Pet Rescue", "address": "200 Rescue Road", "phone": "555-2000", "email": "info@safehavenpets.org", "capacity": 30},
    {"id": 3, "name": "Loving Hearts Animal Sanctuary", "address": "300 Love Lane", "phone": "555-3000", "email": "help@lovinghearts.org", "capacity": 75}
]

# Save to CSV files
def save_to_csv(data, filename):
    if data:
        with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = data[0].keys()
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(data)
        print(f"Saved {filename} with {len(data)} records")

# Save all tables
save_to_csv(animals_data, 'animals.csv')
save_to_csv(users_data, 'users.csv')
save_to_csv(admins_data, 'admins.csv')
save_to_csv(adoptions_data, 'adoptions.csv')
save_to_csv(shelters_data, 'shelters.csv')

print("\nDatabase sample data created successfully!")
print("\nTables created:")
print("- animals.csv: Pet information and details")
print("- users.csv: Registered users/adopters")
print("- admins.csv: System administrators")
print("- adoptions.csv: Adoption applications and status")
print("- shelters.csv: Animal shelters information")