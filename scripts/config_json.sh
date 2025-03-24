#!/bin/bash




# Define log file
LOG_FILE="logs/provisioning.log"


# Function to log messages
log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}


# Function to handle errors and exit
log_error() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - ERROR - $1" >> "$LOG_FILE"
    exit 1
}




{



    FILE_PATH="configs/instances.json"


    if [! -f "$FILE_PATH" ]; then
        log_error "File does NOT exist: $FILE_PATH"
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
        # echo "Machine Name: $machine_name"
        # echo "Operating System: $oc"
        # echo "CPU: $cpu"
        # echo "Memory: $memory"

        echo "The new machine: '$machine_name' has been created!"
        log_message "New Machine -->  Name: $machine_name, OC: $oc, CPU: $cpu, Ram: $memory"

        echo "checking if VM has requearment.txt"
        echo "The VM does not have requirements.txt running --> 'pip install -r requirements.txt'" 
        log_message "running --> 'pip install -r requirements.txt'"

        echo "Installs Nginx on the machine"
        echo "Installing..."

        echo "Nginx has been successfully installed!"
        log_message "Nginx has been successfully installed!"
    done

}






# --------------------------------------------
#   change what is print on terminal and what go to logs
#   why echo go to log? --> echo only print to terminal and function write to logs

# Echo to terminal
#echo "This shows up in the terminal."
# Send text to a log file
#echo "This gets saved to the log file." >> /path/to/your_log_file.log

# LOG_FILE="/path/to/your_log_file.log"

# log_message() {
#   local message="$1"
  
#   # Print to terminal
#   echo "$message"
  
#   # Write to log file
#   echo "$message" >> "$LOG_FILE"
# }

# # Example usage
# log_message "Starting the script..."
# log_message "Something happened."
# log_message "Script finished."



#
#   do another check
#   Submit the project
# --------------------------------------------


