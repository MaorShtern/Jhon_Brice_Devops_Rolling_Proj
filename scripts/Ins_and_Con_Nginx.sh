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


machine=$1


# Extract values from each object
machine_name=$(echo "$machine" | jq -r '.Machine_name')
oc=$(echo "$machine" | jq -r '.OC')
cpu=$(echo "$machine" | jq -r '.CPU')
memory=$(echo "$machine" | jq -r '.Memory')


# echo "Received JSON: $machine"
# Print the extracted values
echo "Machine Name: $machine_name"
echo "Operating System: $oc"
echo "CPU: $cpu"
echo "Memory: $memory"
echo "--------------------------------"
# echo "$machine" | jq -r 'values[]'



echo "The new machine has beec created by this parameters!"
echo "Installs Nginx on the machine"
echo "Installing..."
echo "Nginx has been successfully installed!" 








