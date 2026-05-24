#ifndef DB_H
#define DB_H

#include <sqlite3.h>

// Database connection
extern sqlite3 *db;

// Database initialization and cleanup
int init_database();
void close_database();

// Animal operations
int create_animal_table();
int insert_animal(const char* name, const char* species, const char* breed, 
                 int age, const char* gender, const char* health_status, 
                 const char* status, const char* description, const char* image_url, 
                 int shelter_id);
int get_animals(char** json_result);
int get_animal_by_id(int id, char** json_result);
int update_animal_status(int id, const char* status);
int delete_animal(int id);

// User operations
int create_user_table();
int insert_user(const char* name, const char* email, const char* password,
               const char* phone, const char* address, const char* city);
int get_user_by_email(const char* email, char** json_result);
int authenticate_user(const char* email, const char* password);

// Adoption operations
int create_adoption_table();
int insert_adoption(int user_id, int animal_id, const char* notes);
int get_adoptions(char** json_result);
int update_adoption_status(int id, const char* status, const char* notes);

// Admin operations
int create_admin_table();
int authenticate_admin(const char* username, const char* password);

// Shelter operations
int create_shelter_table();
int get_shelters(char** json_result);

#endif
