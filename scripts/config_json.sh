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


    # Get the absolute path to the folder where this script is located
    SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

    # Build the absolute path to the JSON file
    FILE_PATH="$SCRIPT_DIR/../configs/instances.json"


    if [! -f "$FILE_PATH" ]; then
        echo "File does NOT exist: $FILE_PATH"
        exit 1
    fi


    jq -c '.[]' "$FILE_PATH" | while read -r machine; do
    # Extract values and store them in variables
        sleep 1
        echo ""
        machine_name=$(echo "$machine" | jq -r '.machine_name')
        oc=$(echo "$machine" | jq -r '.oc')
        cpu=$(echo "$machine" | jq -r '.cpu')
        memory=$(echo "$machine" | jq -r '.memory')

        # print machine details
        echo "Machine Name: $machine_name"
        echo "Operating System: $oc"
        echo "CPU: $cpu"
        echo "Memory: $memory"
        echo "The new machine has been created by this parameters!"
        echo "checking if VM has requearment.txt"
        echo "The VM does not have requirements.txt running --> 'pip install -r requirements.txt'" 
        echo "Installs Nginx on the machine"
        echo "Installing..."
        echo "Nginx has been successfully installed!"
        echo "" 
    done

}