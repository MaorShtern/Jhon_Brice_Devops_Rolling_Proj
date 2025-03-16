#!/bin/bash

# Exit on error
# set -e

# Update the package list
echo "Updating package list..."
# sudo apt-get update -y

# Install Nginx
echo "Installing Nginx..."
# sudo apt-get install -y nginx

# Start Nginx service
echo "Starting Nginx service..."
# sudo systemctl start nginx

# Enable Nginx to start on boot
echo "Enabling Nginx to start on boot..."
# sudo systemctl enable nginx

# Check if Nginx is running
echo "Checking if Nginx is running..."
# sudo systemctl status nginx

# Configure a basic web page (Optional)
echo "Configuring a basic index.html page..."
echo "<html>
  <head><title>Welcome to Nginx</title></head>
  <body><h1>Success! Nginx is installed and running.</h1></body>
</html>" 

# | sudo tee /var/www/html/index.html > /dev/null

# Reload Nginx to apply changes
echo "Reloading Nginx to apply changes..."
#sudo systemctl reload nginx

# Print completion message
echo "Nginx installation and configuration completed!"
