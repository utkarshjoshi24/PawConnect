#ifndef API_H
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
