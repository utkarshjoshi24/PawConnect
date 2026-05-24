# Create comprehensive C source code files for the backend system

# server.c - Main CGI server program
server_c_code = '''#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h>
#include <cjson/cJSON.h>

// Include our custom headers
#include "db.h"
#include "api.h"

int main() {
    // Set content type for HTTP response
    printf("Content-Type: application/json\\r\\n\\r\\n");
    
    // Get request method and query string
    char *request_method = getenv("REQUEST_METHOD");
    char *query_string = getenv("QUERY_STRING");
    char *content_length_str = getenv("CONTENT_LENGTH");
    
    // Initialize database
    if (init_database() != 0) {
        printf("{\\"error\\": \\"Database initialization failed\\"}");
        return 1;
    }
    
    // Handle different HTTP methods
    if (strcmp(request_method, "GET") == 0) {
        handle_get_request(query_string);
    } else if (strcmp(request_method, "POST") == 0) {
        int content_length = content_length_str ? atoi(content_length_str) : 0;
        handle_post_request(content_length);
    } else {
        printf("{\\"error\\": \\"Method not allowed\\"}");
        return 1;
    }
    
    // Close database connection
    close_database();
    return 0;
}
'''

# db.h - Database header file
db_h_code = '''#ifndef DB_H
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
'''

# db.c - Database implementation
db_c_code = '''#include "db.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cjson/cJSON.h>

sqlite3 *db = NULL;

int init_database() {
    int rc = sqlite3_open("adoption.db", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Cannot open database: %s\\n", sqlite3_errmsg(db));
        return rc;
    }
    
    // Create tables if they don't exist
    create_animal_table();
    create_user_table();
    create_adoption_table();
    create_admin_table();
    create_shelter_table();
    
    return SQLITE_OK;
}

void close_database() {
    if (db) {
        sqlite3_close(db);
        db = NULL;
    }
}

int create_animal_table() {
    const char* sql = "CREATE TABLE IF NOT EXISTS animals ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "name TEXT NOT NULL,"
                     "species TEXT NOT NULL,"
                     "breed TEXT,"
                     "age INTEGER,"
                     "gender TEXT,"
                     "health_status TEXT,"
                     "status TEXT DEFAULT 'Available',"
                     "description TEXT,"
                     "image_url TEXT,"
                     "shelter_id INTEGER,"
                     "date_added DATETIME DEFAULT CURRENT_TIMESTAMP,"
                     "FOREIGN KEY(shelter_id) REFERENCES shelters(id)"
                     ");";
    
    char *err_msg = 0;
    int rc = sqlite3_exec(db, sql, 0, 0, &err_msg);
    
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\\n", err_msg);
        sqlite3_free(err_msg);
        return rc;
    }
    
    return SQLITE_OK;
}

int insert_animal(const char* name, const char* species, const char* breed, 
                 int age, const char* gender, const char* health_status, 
                 const char* status, const char* description, const char* image_url, 
                 int shelter_id) {
    const char* sql = "INSERT INTO animals (name, species, breed, age, gender, "
                     "health_status, status, description, image_url, shelter_id) "
                     "VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);";
    
    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    
    if (rc != SQLITE_OK) {
        return rc;
    }
    
    sqlite3_bind_text(stmt, 1, name, -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 2, species, -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 3, breed, -1, SQLITE_STATIC);
    sqlite3_bind_int(stmt, 4, age);
    sqlite3_bind_text(stmt, 5, gender, -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 6, health_status, -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 7, status, -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 8, description, -1, SQLITE_STATIC);
    sqlite3_bind_text(stmt, 9, image_url, -1, SQLITE_STATIC);
    sqlite3_bind_int(stmt, 10, shelter_id);
    
    rc = sqlite3_step(stmt);
    sqlite3_finalize(stmt);
    
    return (rc == SQLITE_DONE) ? SQLITE_OK : rc;
}

int get_animals(char** json_result) {
    const char* sql = "SELECT a.*, s.name as shelter_name FROM animals a "
                     "LEFT JOIN shelters s ON a.shelter_id = s.id "
                     "WHERE a.status = 'Available' ORDER BY a.date_added DESC;";
    
    sqlite3_stmt *stmt;
    int rc = sqlite3_prepare_v2(db, sql, -1, &stmt, NULL);
    
    if (rc != SQLITE_OK) {
        return rc;
    }
    
    cJSON *json_array = cJSON_CreateArray();
    
    while ((rc = sqlite3_step(stmt)) == SQLITE_ROW) {
        cJSON *animal = cJSON_CreateObject();
        
        cJSON_AddNumberToObject(animal, "id", sqlite3_column_int(stmt, 0));
        cJSON_AddStringToObject(animal, "name", (char*)sqlite3_column_text(stmt, 1));
        cJSON_AddStringToObject(animal, "species", (char*)sqlite3_column_text(stmt, 2));
        cJSON_AddStringToObject(animal, "breed", (char*)sqlite3_column_text(stmt, 3));
        cJSON_AddNumberToObject(animal, "age", sqlite3_column_int(stmt, 4));
        cJSON_AddStringToObject(animal, "gender", (char*)sqlite3_column_text(stmt, 5));
        cJSON_AddStringToObject(animal, "health_status", (char*)sqlite3_column_text(stmt, 6));
        cJSON_AddStringToObject(animal, "status", (char*)sqlite3_column_text(stmt, 7));
        cJSON_AddStringToObject(animal, "description", (char*)sqlite3_column_text(stmt, 8));
        cJSON_AddStringToObject(animal, "image_url", (char*)sqlite3_column_text(stmt, 9));
        cJSON_AddNumberToObject(animal, "shelter_id", sqlite3_column_int(stmt, 10));
        cJSON_AddStringToObject(animal, "date_added", (char*)sqlite3_column_text(stmt, 11));
        cJSON_AddStringToObject(animal, "shelter_name", (char*)sqlite3_column_text(stmt, 12));
        
        cJSON_AddItemToArray(json_array, animal);
    }
    
    *json_result = cJSON_Print(json_array);
    cJSON_Delete(json_array);
    sqlite3_finalize(stmt);
    
    return SQLITE_OK;
}

int create_user_table() {
    const char* sql = "CREATE TABLE IF NOT EXISTS users ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "name TEXT NOT NULL,"
                     "email TEXT UNIQUE NOT NULL,"
                     "password TEXT NOT NULL,"
                     "phone TEXT,"
                     "address TEXT,"
                     "city TEXT,"
                     "registration_date DATETIME DEFAULT CURRENT_TIMESTAMP"
                     ");";
    
    char *err_msg = 0;
    int rc = sqlite3_exec(db, sql, 0, 0, &err_msg);
    
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\\n", err_msg);
        sqlite3_free(err_msg);
        return rc;
    }
    
    return SQLITE_OK;
}

int create_adoption_table() {
    const char* sql = "CREATE TABLE IF NOT EXISTS adoptions ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "user_id INTEGER NOT NULL,"
                     "animal_id INTEGER NOT NULL,"
                     "application_date DATETIME DEFAULT CURRENT_TIMESTAMP,"
                     "status TEXT DEFAULT 'Pending',"
                     "approval_date DATETIME,"
                     "notes TEXT,"
                     "FOREIGN KEY(user_id) REFERENCES users(id),"
                     "FOREIGN KEY(animal_id) REFERENCES animals(id)"
                     ");";
    
    char *err_msg = 0;
    int rc = sqlite3_exec(db, sql, 0, 0, &err_msg);
    
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\\n", err_msg);
        sqlite3_free(err_msg);
        return rc;
    }
    
    return SQLITE_OK;
}

int create_admin_table() {
    const char* sql = "CREATE TABLE IF NOT EXISTS admins ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "username TEXT UNIQUE NOT NULL,"
                     "password TEXT NOT NULL,"
                     "email TEXT,"
                     "role TEXT DEFAULT 'Admin',"
                     "created_date DATETIME DEFAULT CURRENT_TIMESTAMP"
                     ");";
    
    char *err_msg = 0;
    int rc = sqlite3_exec(db, sql, 0, 0, &err_msg);
    
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\\n", err_msg);
        sqlite3_free(err_msg);
        return rc;
    }
    
    return SQLITE_OK;
}

int create_shelter_table() {
    const char* sql = "CREATE TABLE IF NOT EXISTS shelters ("
                     "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                     "name TEXT NOT NULL,"
                     "address TEXT,"
                     "phone TEXT,"
                     "email TEXT,"
                     "capacity INTEGER DEFAULT 50"
                     ");";
    
    char *err_msg = 0;
    int rc = sqlite3_exec(db, sql, 0, 0, &err_msg);
    
    if (rc != SQLITE_OK) {
        fprintf(stderr, "SQL error: %s\\n", err_msg);
        sqlite3_free(err_msg);
        return rc;
    }
    
    return SQLITE_OK;
}
'''

# api.h - API header file
api_h_code = '''#ifndef API_H
#define API_H

// Request handlers
void handle_get_request(const char* query_string);
void handle_post_request(int content_length);

// Utility functions
void parse_query_string(const char* query_string, char* action, char* params);
void send_json_response(const char* json);
void send_error_response(const char* error_msg);
char* read_post_data(int content_length);
void url_decode(char* dst, const char* src);

// API endpoints
void api_get_animals(const char* params);
void api_get_animal(int animal_id);
void api_get_shelters();
void api_create_animal(const char* json_data);
void api_create_adoption(const char* json_data);
void api_authenticate_user(const char* json_data);
void api_register_user(const char* json_data);

#endif
'''

# api.c - API implementation
api_c_code = '''#include "api.h"
#include "db.h"
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <cjson/cJSON.h>

void handle_get_request(const char* query_string) {
    if (!query_string) {
        send_error_response("No query parameters provided");
        return;
    }
    
    char action[256] = {0};
    char params[1024] = {0};
    parse_query_string(query_string, action, params);
    
    if (strcmp(action, "animals") == 0) {
        api_get_animals(params);
    } else if (strcmp(action, "animal") == 0) {
        int animal_id = atoi(params);
        api_get_animal(animal_id);
    } else if (strcmp(action, "shelters") == 0) {
        api_get_shelters();
    } else {
        send_error_response("Unknown action");
    }
}

void handle_post_request(int content_length) {
    char* post_data = read_post_data(content_length);
    if (!post_data) {
        send_error_response("Failed to read POST data");
        return;
    }
    
    cJSON *json = cJSON_Parse(post_data);
    if (!json) {
        send_error_response("Invalid JSON data");
        free(post_data);
        return;
    }
    
    cJSON *action_item = cJSON_GetObjectItemCaseSensitive(json, "action");
    if (!cJSON_IsString(action_item)) {
        send_error_response("Action field required");
        cJSON_Delete(json);
        free(post_data);
        return;
    }
    
    const char* action = action_item->valuestring;
    
    if (strcmp(action, "create_animal") == 0) {
        api_create_animal(post_data);
    } else if (strcmp(action, "create_adoption") == 0) {
        api_create_adoption(post_data);
    } else if (strcmp(action, "authenticate") == 0) {
        api_authenticate_user(post_data);
    } else if (strcmp(action, "register") == 0) {
        api_register_user(post_data);
    } else {
        send_error_response("Unknown action");
    }
    
    cJSON_Delete(json);
    free(post_data);
}

void api_get_animals(const char* params) {
    char* json_result = NULL;
    
    if (get_animals(&json_result) == SQLITE_OK) {
        send_json_response(json_result);
        free(json_result);
    } else {
        send_error_response("Failed to retrieve animals");
    }
}

void api_get_animal(int animal_id) {
    char* json_result = NULL;
    
    if (get_animal_by_id(animal_id, &json_result) == SQLITE_OK) {
        send_json_response(json_result);
        free(json_result);
    } else {
        send_error_response("Animal not found");
    }
}

void api_get_shelters() {
    char* json_result = NULL;
    
    if (get_shelters(&json_result) == SQLITE_OK) {
        send_json_response(json_result);
        free(json_result);
    } else {
        send_error_response("Failed to retrieve shelters");
    }
}

void api_create_animal(const char* json_data) {
    cJSON *json = cJSON_Parse(json_data);
    if (!json) {
        send_error_response("Invalid JSON");
        return;
    }
    
    // Extract animal data from JSON
    cJSON *name = cJSON_GetObjectItemCaseSensitive(json, "name");
    cJSON *species = cJSON_GetObjectItemCaseSensitive(json, "species");
    cJSON *breed = cJSON_GetObjectItemCaseSensitive(json, "breed");
    cJSON *age = cJSON_GetObjectItemCaseSensitive(json, "age");
    cJSON *gender = cJSON_GetObjectItemCaseSensitive(json, "gender");
    cJSON *health_status = cJSON_GetObjectItemCaseSensitive(json, "health_status");
    cJSON *description = cJSON_GetObjectItemCaseSensitive(json, "description");
    cJSON *image_url = cJSON_GetObjectItemCaseSensitive(json, "image_url");
    cJSON *shelter_id = cJSON_GetObjectItemCaseSensitive(json, "shelter_id");
    
    if (!cJSON_IsString(name) || !cJSON_IsString(species)) {
        send_error_response("Name and species are required");
        cJSON_Delete(json);
        return;
    }
    
    int result = insert_animal(
        name->valuestring,
        species->valuestring,
        cJSON_IsString(breed) ? breed->valuestring : "",
        cJSON_IsNumber(age) ? age->valueint : 0,
        cJSON_IsString(gender) ? gender->valuestring : "",
        cJSON_IsString(health_status) ? health_status->valuestring : "Unknown",
        "Available",
        cJSON_IsString(description) ? description->valuestring : "",
        cJSON_IsString(image_url) ? image_url->valuestring : "",
        cJSON_IsNumber(shelter_id) ? shelter_id->valueint : 1
    );
    
    if (result == SQLITE_OK) {
        printf("{\\"success\\": true, \\"message\\": \\"Animal created successfully\\"}");
    } else {
        send_error_response("Failed to create animal");
    }
    
    cJSON_Delete(json);
}

void send_json_response(const char* json) {
    printf("%s", json);
}

void send_error_response(const char* error_msg) {
    printf("{\\"error\\": \\"%s\\"}", error_msg);
}

char* read_post_data(int content_length) {
    if (content_length <= 0) return NULL;
    
    char* buffer = malloc(content_length + 1);
    if (!buffer) return NULL;
    
    fread(buffer, 1, content_length, stdin);
    buffer[content_length] = '\\0';
    
    return buffer;
}

void parse_query_string(const char* query_string, char* action, char* params) {
    if (!query_string) return;
    
    char* query_copy = strdup(query_string);
    char* token = strtok(query_copy, "&");
    
    while (token) {
        char* equals = strchr(token, '=');
        if (equals) {
            *equals = '\\0';
            char* key = token;
            char* value = equals + 1;
            
            if (strcmp(key, "action") == 0) {
                strcpy(action, value);
            } else if (strcmp(key, "id") == 0) {
                strcpy(params, value);
            }
        }
        token = strtok(NULL, "&");
    }
    
    free(query_copy);
}
'''

# Makefile
makefile_code = '''# Makefile for Animal Adoption System
CC = gcc
CFLAGS = -Wall -Wextra -std=c99
LIBS = -lsqlite3 -lcjson
TARGET = server.cgi
SOURCES = server.c db.c api.c

# Default target
all: $(TARGET)

# Build the CGI executable
$(TARGET): $(SOURCES)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCES) $(LIBS)

# Install dependencies (Ubuntu/Debian)
install-deps:
	sudo apt-get update
	sudo apt-get install libsqlite3-dev libcjson-dev apache2

# Clean build files
clean:
	rm -f $(TARGET) *.o

# Install CGI script to web server
install: $(TARGET)
	sudo cp $(TARGET) /var/www/cgi-bin/
	sudo chmod 755 /var/www/cgi-bin/$(TARGET)
	sudo chown www-data:www-data /var/www/cgi-bin/$(TARGET)

# Test the application
test:
	@echo "Testing animal listing..."
	@curl -X GET "http://localhost/cgi-bin/server.cgi?action=animals"

.PHONY: all clean install install-deps test
'''

# Save all files
files_to_create = [
    ('server.c', server_c_code),
    ('db.h', db_h_code),
    ('db.c', db_c_code),
    ('api.h', api_h_code),
    ('api.c', api_c_code),
    ('Makefile', makefile_code)
]

for filename, content in files_to_create:
    with open(filename, 'w') as f:
        f.write(content)
    print(f"Created {filename}")

print("\nC Backend source files created successfully!")
print("\nFiles created:")
print("- server.c: Main CGI server program")
print("- db.h/db.c: Database operations and SQLite integration")
print("- api.h/api.c: API endpoints and request handling")
print("- Makefile: Build configuration")
print("\nTo compile and install:")
print("1. make install-deps  # Install required libraries")
print("2. make              # Compile the application")
print("3. make install      # Install to web server")