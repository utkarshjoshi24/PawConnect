# Makefile for Animal Adoption System
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
