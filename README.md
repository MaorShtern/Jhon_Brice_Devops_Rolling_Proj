DevOps Infrastructure Provisioning & Configuration Automation Project

Overview:

The DevOps Infrastructure Provisioning & Configuration Automation Project aims to build a modular Python-based tool to automate infrastructure provisioning. The current version of the tool simulates infrastructure provisioning and service configuration without interacting with real cloud resources.

The project is designed to evolve by integrating cloud services such as AWS and Terraform in future enhancements, allowing for real infrastructure provisioning. The current iteration focuses on automating virtual machine (VM) creation, service installation, and configuration simulation.

Project Objective:
The goal of this project is to develop a modular Python automation tool that simulates infrastructure provisioning and service configuration. Key features include:

* Dynamic virtual machine provisioning: Accepts user input for defining VMs.
* Input validation: Ensures correctness of user inputs (e.g., VM configuration).
* Object-oriented design: Utilizes Python classes and modular code structure.
* Bash scripts for service configuration: Automates the installation and configuration of services (e.g., Nginx).
* Logging and error handling: Implements logging and proper error handling in both Python and Bash scripts.

Project Structure
The repository is organized as follows:


infra-automation/           # This will by use as the main.py
|-- scripts/                # Contains Bash scripts for provisioning and service configuration
|-- configs/                # Stores configuration files (e.g., VM definitions)
|-- logs/                   # Logs for tracking the provisioning process
|-- src/                    # Contains Python source code and classes
|-- README.md               # Project documentation


Setup & Repository Initialization

Clone the repository to your local machine:
git clone https://github.com/yourusername/infra-automation.git
cd infra-automation

Set up a virtual environment to manage Python dependencies:
python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required Python packages:
pip install -r requirements.txt


Simulating Infrastructure Provisioning

1. Accepting User Input
This tool lets users define virtual machines (VMs) dynamically by entering basic information like:

* VM name
* Operating System (OS)
* CPU cores
* RAM size
We validate the input to ensure it's correct (e.g., ensuring the number of CPU cores is a positive integer). The validated configurations are stored in a JSON file located in configs/instances.json.

Example instances.json:
{
    "name": "VM1",
    "os": "Ubuntu",
    "cpu": 2,
    "ram": 4096
}


2. Building a Modular Python Application
The tool uses Python classes to represent virtual machines. The main class is Machine, which handles the details of a VM (e.g., name, OS, CPU, RAM) and provides methods for converting this data into a dictionary.


3. Automating Service Installation with Bash
Once a VM is provisioned, we use Bash scripts to automate the installation of services like Nginx. The Python script runs the Bash script using subprocess to install Nginx on the VM.


Logging & Error Handling
Both Python and Bash scripts implement logging to track the provisioning and service configuration process:

* Python Logging: The logging module writes logs to logs/provisioning.log.
* Bash Logging: Logs are written to the terminal (stdout) and to logs/provisioning.log.

Example Logging:
2025-03-17 09:52:30,370 - INFO - Script executed successfully.


Final Notes
* This tool is a simulation and currently doesn't provision real virtual machines or services.
* In future versions, we plan to integrate with cloud platforms (like AWS) and automation tools (like Terraform).

We hope you find this project useful and encourage you to explore, contribute, or use it as a foundation for your own infrastructure automation tools.


