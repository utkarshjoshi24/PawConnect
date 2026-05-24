#include "db.h"
#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <cjson/cJSON.h>

sqlite3 *db = NULL;

int init_database() {
    int rc = sqlite3_open("adoption.db", &db);
    if (rc != SQLITE_OK) {
        fprintf(stderr, "Cannot open database: %s\n", sqlite3_errmsg(db));
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
        fprintf(stderr, "SQL error: %s\n", err_msg);
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
        fprintf(stderr, "SQL error: %s\n", err_msg);
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
        fprintf(stderr, "SQL error: %s\n", err_msg);
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
        fprintf(stderr, "SQL error: %s\n", err_msg);
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
        fprintf(stderr, "SQL error: %s\n", err_msg);
        sqlite3_free(err_msg);
        return rc;
    }

    return SQLITE_OK;
}
