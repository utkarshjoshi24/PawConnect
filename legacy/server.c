#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sqlite3.h>
#include <cjson/cJSON.h>

// Include our custom headers
#include "db.h"
#include "api.h"

int main() {
    // Set content type for HTTP response
    printf("Content-Type: application/json\r\n\r\n");

    // Get request method and query string
    char *request_method = getenv("REQUEST_METHOD");
    char *query_string = getenv("QUERY_STRING");
    char *content_length_str = getenv("CONTENT_LENGTH");

    // Initialize database
    if (init_database() != 0) {
        printf("{\"error\": \"Database initialization failed\"}");
        return 1;
    }

    // Handle different HTTP methods
    if (strcmp(request_method, "GET") == 0) {
        handle_get_request(query_string);
    } else if (strcmp(request_method, "POST") == 0) {
        int content_length = content_length_str ? atoi(content_length_str) : 0;
        handle_post_request(content_length);
    } else {
        printf("{\"error\": \"Method not allowed\"}");
        return 1;
    }

    // Close database connection
    close_database();
    return 0;
}
