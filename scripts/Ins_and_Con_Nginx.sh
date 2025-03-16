#!/bin/bash

# Exit on error
set -e


# Path to the JSON file
JSON_FILE="../configs/instances.json"


# Check if the file exists
if [ ! -f "$JSON_FILE" ]; then
    echo "Error: File $JSON_FILE not found!"
    exit 1
fi


jq -c '.[]' "$JSON_FILE" | while read -r machine; do


    # Extract values from each object
    machine_name=$(echo "$machine" | jq -r '.machine_name')
    oc=$(echo "$machine" | jq -r '.oc')
    cpu=$(echo "$machine" | jq -r '.cpu')
    memory=$(echo "$machine" | jq -r '.memory')
    services=$(echo "$machine" | jq -r '.services')

    # Print the extracted values
    echo "Machine Name: $machine_name"
    echo "Operating System: $oc"
    echo "CPU: $cpu"
    echo "Memory: $memory"
    echo "services: $services"
    echo "--------------------------------"


  has_nginx=$(echo "$machine" | jq '(.services | has("Nginx"))')

    # If "Nginx" is found, print the machine name
    if [ "$has_nginx" == "true" ]; then
        machine_name=$(echo "$machine" | jq -r '.machine_name')
        echo "Nginx is present in the services of machine: $machine_name"
    else
        machine_name=$(echo "$machine" | jq -r '.machine_name')
        echo "Nginx is NOT present in the services of machine: $machine_name"
        echo "Nginx is not installed. Installing Nginx..."
        # Update the package list
        echo "Update the package list"
        #sudo apt-get update -y
        # Install Nginx
        echo "Install Nginx"
        echo "Nginx installation and configuration completed!"
    fi
    echo
done












