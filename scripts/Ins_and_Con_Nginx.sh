#!/bin/bash



# Define log file
LOG_FILE="logs/provisioning.log"

# Function to log messages
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Function to log errors
log_error() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ERROR - $1" >> "$LOG_FILE"
}

# Function to handle errors and exit
handle_error() {
    log_error "$1"
    exit 1
}



{
    sleep 2  # Simulate provisioning task
    # Path to the JSON file
    JSON_FILE="../configs/instances.json"
    # Check if the file exists
    if [ ! -f "$JSON_FILE" ]; then
        echo "Error: File $JSON_FILE not found!"
        exit 1
    fi

    # get json string object
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

    echo "The new machine has beec created by this parameters!"
    echo "Installs Nginx on the machine"
    echo "Installing..."
    echo "Nginx has been successfully installed!" 


} || handle_error "Error occurred during provisioning."













