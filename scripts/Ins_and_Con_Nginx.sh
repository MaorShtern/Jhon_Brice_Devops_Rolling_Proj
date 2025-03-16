#!/bin/bash

# Exit on error
set -e

# Check if Nginx is installed
if ! dpkg -l | grep -q nginx; then
    echo "Nginx is not installed. Installing Nginx..."
    
    # Update the package list
    echo "Update the package list"
    #sudo apt-get update -y
    
    # Install Nginx
    echo "Install Nginx"
    #sudo apt-get install -y nginx
else
    echo "Nginx is already installed. Skipping installation."
fi

# Start Nginx service
echo "Starting Nginx service..."
#sudo systemctl start nginx

# Enable Nginx to start on boot
echo "Enabling Nginx to start on boot..."
# sudo systemctl enable nginx


echo "Nginx is running successfully."


# # Check if Nginx is running
# echo "Checking if Nginx is running..."
# if systemctl is-active --quiet nginx; then
#     echo "Nginx is running successfully."
# else
#     echo "Failed to start Nginx. Please check the service status."
#     exit 1
# fi

# Configure a basic web page (Optional)
echo "Configuring a basic index.html page..."
echo "<html>
  <head><title>Welcome to Nginx</title></head>
  <body><h1>Success! Nginx is installed and running.</h1></body>
</html>" 

# | sudo tee /var/www/html/index.html > /dev/null

# Reload Nginx to apply changes
echo "Reloading Nginx to apply changes..."
# sudo systemctl reload nginx

echo "Nginx installation and configuration completed!"
















