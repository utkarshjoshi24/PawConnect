#include "api.h"
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
        printf("{\"success\": true, \"message\": \"Animal created successfully\"}");
    } else {
        send_error_response("Failed to create animal");
    }

    cJSON_Delete(json);
}

void send_json_response(const char* json) {
    printf("%s", json);
}

void send_error_response(const char* error_msg) {
    printf("{\"error\": \"%s\"}", error_msg);
}

char* read_post_data(int content_length) {
    if (content_length <= 0) return NULL;

    char* buffer = malloc(content_length + 1);
    if (!buffer) return NULL;

    fread(buffer, 1, content_length, stdin);
    buffer[content_length] = '\0';

    return buffer;
}

void parse_query_string(const char* query_string, char* action, char* params) {
    if (!query_string) return;

    char* query_copy = strdup(query_string);
    char* token = strtok(query_copy, "&");

    while (token) {
        char* equals = strchr(token, '=');
        if (equals) {
            *equals = '\0';
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
