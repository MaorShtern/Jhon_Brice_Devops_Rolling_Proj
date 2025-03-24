
import logging
import re
from src.Machine import Machine
import json
import os
import jsonschema
from jsonschema import validate
import subprocess
import sys
from json.decoder import JSONDecodeError


machines_list = []


def Define_logging():

    log_file = 'logs/provisioning.log'
    # Create a custom logger
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)

    # Create handlers for the file 
    file_handler = logging.FileHandler(log_file)

    # Define the log format
    log_format = '%(asctime)s - %(levelname)s - %(message)s'
    date_format = '%d-%m-%Y %H:%M:%S'
    formatter = logging.Formatter(log_format, datefmt=date_format)

    # Add formatters to handlers
    file_handler.setFormatter(formatter)

    # Add handlers to the logger
    logger.addHandler(file_handler)




def Handle_Logging_Info(message):
    print(message)
    logging.info(message)


def Handle_Logging_Error(message):
    print(message)
    logging.error(message)



def Prompt_Users_For_Input():
    print()
    print(" ---------------------------------------------------------------------------------- ")
    print("Please enter the machine details as specified.")
    print("Enter virtual machine name: (enter 'exit' to finish)")
    print("What system would you like the machine to run on? ( Ubuntu / Windows / CentOS )")
    print("What number of CPU cores allocated to the machine? ( 1 - 16 )")
    print("How much memory int MB would you like to allocate? ( 1 and higher )")
    print(" ---------------------------------------------------------------------------------- ")
    print()




# Check whether the name the user entered into the system is correct.
def validate_name(machine_name):

    # Is the machine name between 3 and 50 characters?
    if len(machine_name) < 3 or len(machine_name) > 50:
        print()
        print("the machine name must be between 3 and 50 characters.")
        print()
        return False
    
    # Does the machine name contain spaces?
    elif machine_name.count(" ") > 0:
        print()
        print("no spaces are allowed.")
        print()
        return False

    # Check that the name recognizes numbers, letters, and specific characters.
    # checking if a variable name matches a specific pattern using a regular expression (regex).
    elif not re.match("^[a-zA-Z0-9_-]+$", machine_name):
        print()
        print("VM name can only contain letters, numbers, hyphens, and underscores.")
        print()
        return False
    
    # Notify that the name meets the criteria
    return True



# Check whether the system the user entered into the system is correct.
def validate_OC(oc):
    supported_os = ["ubuntu", "windows", "centos"]
    if oc.lower() not in supported_os:
        print()
        print("Invalid OS choice. Supported OS are: Ubuntu / Windows / CentOS")
        print()
        return False
    return True



def validate_CPU(cpu):

    # Check whether the value the user entered into the system is a number between 1 - 16.
    if 1 <= cpu <= 16:
        return True
    print()
    print("CPU cores must be an integer between 1 and 16.")
    print()
    return False



def validated_Memory(memory):
    if memory >= 1 :
        return True
    print()
    print("Memory size  must be a number 1 and higher.")
    print()
    return False


# A function that checks the validity of the values ​​that the user entered into the system.
def validated_user_machine_input(machine_name,oc,cpu,memory):
    if validate_name(machine_name) and validate_OC(oc) and validate_CPU(cpu) and validated_Memory(memory):
        return True
    return False




def create_new_machine(machine_name,oc,cpu,memory):

    if not validated_user_machine_input(machine_name,oc,cpu,memory):
        return False


    # A schema that ensures that the object meets the criteria we require of it
    schema = {
        "type": "object",
        "properties": {
            "machine_name": {"type": "string"},
            "oc": {"type": "string"},
            "cpu": {"type": "integer"},
            "memory": {"type": "integer"},
        },
        "required": ["machine_name", "oc" ,"cpu" , "memory"]
        }
    


    try:

        validate(instance={ "machine_name" : machine_name , "oc" : oc, "cpu" : cpu , "memory" : memory }, schema=schema)

        new_machine = Machine(machine_name,oc,cpu,memory)
        machines_list.append(new_machine)
        Handle_Logging_Info("New machine created successfully")
        return True
    
    # raised when data doesn't conform to a specified JSON schema
    except jsonschema.exceptions.ValidationError as ex:
        Handle_Logging_Error("The new machine was not added to the database. Please check what is wrong with the function --> config_JSON_File")
        Handle_Logging_Error(f"Data validation failed: {ex.message}") 
    

    # Catch unexpected errors
    except Exception as ex:
        Handle_Logging_Error(f"An unexpected error occurred: {str(ex)}")
        return False




# This function takes an object (obj) and returns its __dict__, which is a dictionary of the object's attributes. '
# This is needed because json.dumps() can't directly convert custom objects into JSON. 
# So, we first change them into a dictionary that json.dumps() can handle.
def obj_dict(obj):
    return obj.__dict__


# json.dumps(list_name, default=obj_dict) is used to convert Python objects into JSON strings. 
# By default, json.dumps() can only handle basic types like strings, numbers, lists, and dictionaries. 
# To convert custom objects, you use the default argument and pass the obj_dict function. 
# This function changes the object into a dictionary, which json.dumps() can process.
def Write_To_JSON_File():

    try:

        # Specify the path to the file outside the current directory
        file_path = os.path.join("configs","instances.json")

        # Make sure the directory exists, create it if it doesn't
        os.makedirs(os.path.dirname(file_path), exist_ok=True)


        # The indent=4 argument ensures that the output is formatted nicely with an indentation level of 4 spaces.
        json_string = json.dumps(machines_list, default=obj_dict, indent=4)


        with open(file_path , 'w') as file:
            file.write(json_string)
        
        Handle_Logging_Info("The new machine has been added to the database.")


    except Exception as ex:
        Handle_Logging_Error(f"Error: {ex}")
        return False



def Run_Bash_Script():

    try:

        # Run the bash script
        result = subprocess.run(['bash', 'scripts/config_json.sh'], check=True, text=True, capture_output=True)
        # Print the output of the script
        print(f"Output: {result.stdout}")
        Handle_Logging_Info("Script executed successfully.")

    except subprocess.CalledProcessError as ex:
        # If the script fails, print the error message
        Handle_Logging_Error(f"Error occurred while executing the script: {ex}")
        Handle_Logging_Error(f"Error Output: {ex.stderr}")
        sys.exit(1)
    

    # Catch unexpected errors
    except Exception as ex:
        Handle_Logging_Error(f"An unexpected error occurred: {str(ex)}")
        sys.exit(1)




if __name__ == "__main__":

    Define_logging()
    machine_name = ""

    while machine_name != "exit":

        Prompt_Users_For_Input()

        machine_name = input("machine name: ")
        if machine_name.lower() == "exit":
            break
        
        oc = input("OS: ")
        try:
            cpu = int(input("CPU: "))
            memory = int(input("Memory: "))
        except ValueError:
            cpu = -1
            memory = -1



        if create_new_machine(machine_name,oc,cpu,memory) is False:
            continue

        
        Handle_Logging_Info("The new machine has been added to the list of existing systems.")
        Write_To_JSON_File() 



Run_Bash_Script()















