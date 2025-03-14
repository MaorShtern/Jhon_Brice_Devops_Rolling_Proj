
import logging
import re
from Virtual_Machine import Virtual_Machine
import json
import os
import jsonschema
from jsonschema import validate





# def validate_vriables():

#     # Define the schema for validation
    # schema = {
    # "type": "array",
    # "items": {
    #     "type": "object",
    #     "properties": {
    #         "machine_name": {"type": "string"},
    #         "oc": {"type": "string"},
    #         "cpu": {"type": "integer"},
    #         "memory": {"type": "integer"},
    #         },
    #     "required": ["machine_name", "oc","cpu","memory"]
    #     }
    # }

#     try:
#         validate(instance=list_name, schema=schema)
#         print("Data is valid.")
#         return True
#     except jsonschema.exceptions.ValidationError as e:
#         print(f"Data validation failed: {e.message}")
#         return False






logging.basicConfig(
    level=logging.INFO,  # Log level
    format="%(asctime)s - %(levelname)s - %(message)s",  # Log format
    handlers=[
        logging.StreamHandler()  # Output to stdout
    ]
)



def Prompt_Users_For_Input():
    print(" ---------------------------------------------------------------------------------- ")
    print("Please enter the machine details as specified.")
    print("Enter virtual machine name: (enter 'exit' to finish)")
    print("What system would you like the machine to run on? ( Ubuntu / Windows / CentOS )")
    print("What number of CPU cores allocated to the machine? ( 1 - 16 )")
    print("How much memory int GB would you like to allocate? ( 1 - 64 )")
    print(" ---------------------------------------------------------------------------------- ")




# Check whether the name the user entered into the system is correct.
def validate_name(vm_name):

    # Is the machine name between 3 and 50 characters?
    if len(vm_name) < 3 or len(vm_name) > 50:
        print()
        logging.error("the machine name must be between 3 and 50 characters.")
        print()
        return False
    
    # Does the machine name contain spaces?
    elif vm_name.count(" ") > 0:
        print()
        logging.error("no spaces are allowed.")
        print()
        return False

    # Check that the name recognizes numbers, letters, and specific characters.
    # checking if a variable name matches a specific pattern using a regular expression (regex).
    elif not re.match("^[a-zA-Z0-9_-]+$", vm_name):
        print()
        logging.error("VM name can only contain letters, numbers, hyphens, and underscores.")
        print()
        return False
    
    # Notify that the name meets the criteria
    return True



# Check whether the system the user entered into the system is correct.
def validate_OC(oc):

    supported_os = ["ubuntu", "windows", "centos"]
    if oc.lower() not in supported_os:
        print()
        logging.error("Invalid OS choice. Supported OS are: Ubuntu / Windows / CentOS")
        print()
        return False
    return True



def validate_CPU(cpu):

    # Check whether the value the user entered into the system is a number between 1 - 16.
    if 1 <= cpu <= 16:
        return True
    print()
    logging.error("CPU cores must be an integer between 1 and 16.")
    print()
    return False



def validated_Memory(memory):
    if 1 <= memory <= 64:
        return True
    print()
    logging.error("Memory size  must be an integer between 1 and 64.")
    print()
    return False


# A function that checks the validity of the values ​​that the user entered into the system.
def validated_user_machine(vm_name,oc,cpu,memory):
    if validate_name(vm_name) and validate_OC(oc) and validate_CPU(cpu) and validated_Memory(memory):
        return True
    return False



 


def create_new_machine(vm_name,oc,cpu,memory):

    if not validated_user_machine(vm_name,oc,cpu,memory):
        return None

    new_machine = Virtual_Machine(vm_name,oc,cpu,memory)
    print("New machine created successfully")
    return new_machine



# This function takes an object (obj) and returns its __dict__, which is a dictionary of the object's attributes. '
# This is needed because json.dumps() can't directly convert custom objects into JSON. 
# So, we first change them into a dictionary that json.dumps() can handle.
def obj_dict(obj):
    return obj.__dict__


# json.dumps(list_name, default=obj_dict) is used to convert Python objects into JSON strings. 
# By default, json.dumps() can only handle basic types like strings, numbers, lists, and dictionaries. 
# To convert custom objects, you use the default argument and pass the obj_dict function. 
# This function changes the object into a dictionary, which json.dumps() can process.
def config_JSON_File(machines_list):

    schema = {
        "type": "array",
        "items": {
            "type": "object",
            "properties": {
                "machine_name": {"type": "string"},
                "oc": {"type": "string"},
                "cpu": {"type": "integer"},
                "memory": {"type": "integer"},
                },
            "required": ["machine_name", "oc","cpu","memory"]
            }
        }


    try:
        validate(instance=machines_list, schema=schema)
        print("Data is valid.")
        json_string = json.dumps(machines_list, default=obj_dict)
        # print("Json List:", json_string)

        # Specify the path to the file outside the current directory
        file_path = os.path.join("..","scripts","instances.json")

        # Make sure the directory exists, create it if it doesn't
        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        with open(file_path , 'w') as file:
            file.write(json_string)
        
        print("The new machine has been added to the database.")
    except jsonschema.exceptions.ValidationError as e:
        print(f"Data validation failed: {e.message}")
        return False



if __name__ == "__main__":


    machines_list = []

    vm_name = ""

    while vm_name != "exit":

        Prompt_Users_For_Input()

        vm_name = input("machine name: ")
        if vm_name.lower() == "exit":
            break
        
        oc = input("OS: ")
        try:
            cpu = int(input("CPU: "))
            memory = int(input("Memory: "))
        except ValueError:
            cpu = -1
            memory = -1


        new_machine = create_new_machine(vm_name,oc,cpu,memory)

        if new_machine != None:
            machines_list.append(new_machine)
            print("The new machine has been added to the list of existing systems.")
        if config_JSON_File(machines_list) is False:
            print("The new machine was not added to the database.\nPlease check what is wrong with the function --> config_JSON_File")


        # print(chr(27) + "[2J")












