# Animal Adoption Management System - Setup Guide

## Overview
This comprehensive guide will help you set up and deploy the Animal Adoption Management System, a full-stack web application built with C backend, SQLite database, and HTML/CSS frontend.

## System Requirements

### Hardware Requirements
- **Server**: Minimum 1GB RAM, 10GB storage
- **CPU**: 1GHz processor or better
- **Network**: Reliable internet connection with sufficient bandwidth

### Software Requirements
- **Operating System**: Linux (Ubuntu 20.04+ recommended), Windows, or macOS
- **Web Server**: Apache 2.4+ or Nginx 1.18+
- **Database**: SQLite 3.31+
- **Compiler**: GCC 9.0+ or compatible C compiler
- **Libraries**: libsqlite3-dev, libcjson-dev

## Installation Steps

### 1. Install Dependencies

#### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install build-essential
sudo apt-get install libsqlite3-dev libcjson-dev
sudo apt-get install apache2 apache2-dev
```

#### CentOS/RHEL:
```bash
sudo yum install gcc gcc-c++ make
sudo yum install sqlite-devel libcjson-devel
sudo yum install httpd httpd-devel
```

#### macOS (with Homebrew):
```bash
brew install sqlite3 cjson
brew install apache2
```

### 2. Compile the C Backend

1. Navigate to the source directory
2. Compile the application:
```bash
make clean
make
```

3. Install the CGI executable:
```bash
sudo make install
```

### 3. Configure Web Server

#### Apache Configuration:

1. Enable CGI module:
```bash
sudo a2enmod cgi
sudo systemctl restart apache2
```

2. Configure CGI directory in `/etc/apache2/sites-available/000-default.conf`:
```apache
<Directory "/var/www/cgi-bin">
    Options +ExecCGI
    AddHandler cgi-script .cgi
    AllowOverride None
    Require all granted
</Directory>
```

3. Set proper permissions:
```bash
sudo chmod 755 /var/www/cgi-bin/server.cgi
sudo chown www-data:www-data /var/www/cgi-bin/server.cgi
```

#### Nginx Configuration:

1. Install fcgiwrap:
```bash
sudo apt-get install fcgiwrap
```

2. Configure nginx site:
```nginx
server {
    listen 80;
    server_name your-domain.com;
    root /var/www/html;
    
    location ~ \.cgi$ {
        gzip off;
        fastcgi_pass unix:/var/run/fcgiwrap.socket;
        include fastcgi_params;
        fastcgi_param SCRIPT_FILENAME /var/www/cgi-bin$fastcgi_script_name;
    }
}
```

### 4. Deploy Frontend Files

1. Copy HTML, CSS, and JavaScript files to web root:
```bash
sudo cp *.html /var/www/html/
sudo cp styles.css /var/www/html/
sudo cp -r js /var/www/html/
```

2. Set proper permissions:
```bash
sudo chown -R www-data:www-data /var/www/html/
sudo chmod -R 644 /var/www/html/*
```

### 5. Initialize Database

1. Create the SQLite database:
```bash
sqlite3 /var/www/adoption.db < init_database.sql
```

2. Set proper permissions:
```bash
sudo chown www-data:www-data /var/www/adoption.db
sudo chmod 664 /var/www/adoption.db
```

### 6. Test the Installation

1. Test CGI backend:
```bash
curl -X GET "http://localhost/cgi-bin/server.cgi?action=animals"
```

2. Access the web interface:
```
http://localhost/index.html
```

## Configuration

### Database Schema
The system automatically creates the following tables:
- `animals`: Pet information and details
- `users`: Registered users and adopters
- `admins`: System administrators
- `adoptions`: Adoption applications and status
- `shelters`: Partner shelter information

### Security Configuration

1. **Database Security**:
   - Ensure SQLite database file is not web-accessible
   - Use proper file permissions (664 for database file)

2. **CGI Security**:
   - Validate all input parameters
   - Use prepared statements for SQL queries
   - Implement proper error handling

3. **Web Server Security**:
   - Enable HTTPS in production
   - Configure proper firewall rules
   - Regular security updates

### Performance Optimization

1. **Database Optimization**:
   - Create indexes on frequently queried columns
   - Regular database maintenance and cleanup

2. **Web Server Optimization**:
   - Enable gzip compression
   - Configure caching headers
   - Optimize static file delivery

## Troubleshooting

### Common Issues

#### 1. CGI Script Not Executing
**Error**: "Internal Server Error" or script downloads instead of executing
**Solution**: 
- Check CGI module is enabled
- Verify file permissions (755 for executable)
- Check server error logs

#### 2. Database Connection Failed
**Error**: "Cannot open database" error
**Solution**:
- Verify database file exists and has correct permissions
- Check database file path in configuration
- Ensure SQLite library is properly installed

#### 3. Permission Denied Errors
**Error**: Various permission-related errors
**Solution**:
- Check file ownership (www-data:www-data)
- Verify directory permissions
- Review SELinux/AppArmor policies

#### 4. Missing Dependencies
**Error**: Compilation or runtime library errors
**Solution**:
- Install required development libraries
- Check library paths and versions
- Update package repositories

### Log Files
- **Apache Error Log**: `/var/log/apache2/error.log`
- **Nginx Error Log**: `/var/log/nginx/error.log`
- **System Log**: `/var/log/syslog`

## Maintenance

### Regular Tasks
1. **Database Backup**:
```bash
cp /var/www/adoption.db /backup/adoption_$(date +%Y%m%d).db
```

2. **Log Rotation**:
   - Configure logrotate for web server logs
   - Monitor disk space usage

3. **Security Updates**:
   - Regular system updates
   - Monitor security advisories
   - Update dependencies as needed

### Monitoring
- Monitor web server performance
- Check database file size and growth
- Review error logs regularly
- Monitor system resource usage

## Production Deployment

### SSL Certificate Setup
1. Install Let's Encrypt:
```bash
sudo apt-get install certbot python3-certbot-apache
sudo certbot --apache -d your-domain.com
```

2. Configure automatic renewal:
```bash
sudo crontab -e
# Add: 0 12 * * * /usr/bin/certbot renew --quiet
```

### Load Balancing (Optional)
For high-traffic deployments, consider:
- Multiple server instances
- Load balancer configuration
- Database clustering or replication

### Backup Strategy
1. **Database Backups**: Daily automated backups
2. **File Backups**: Regular backup of web files
3. **Configuration Backups**: Backup server configurations

## Support and Documentation

### API Documentation
The CGI backend supports the following endpoints:
- `GET ?action=animals`: List available animals
- `GET ?action=animal&id=N`: Get specific animal details
- `POST action=create_animal`: Add new animal (admin only)
- `POST action=create_adoption`: Submit adoption application

### Database Schema Reference
See the ERD diagram and database documentation for complete schema details.

### System Architecture
Refer to the system architecture diagram for understanding component relationships and data flow.

---

**Note**: This system is designed for educational and demonstration purposes. For production use, implement additional security measures, error handling, and performance optimizations as required for your specific environment.