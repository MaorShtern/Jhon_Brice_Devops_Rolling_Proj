

Jhon_Brice_Devops_Rolling_Proj


Introduction
This repository contains the code for Project Name. Follow the steps below to get started by cloning this repository and setting up the necessary environment for development.


Requirements
Python 3.x
Git
pip (for Python package management)


Step 1: Clone the Git Repository
code: Clone the repository to your local machine by running the following command in your terminal:
git clone https://github.com/username/repository-name.git
Replace username and repository-name with the actual GitHub username and repository name.


Step 2: Navigate into the Project Directory
Once the repository is cloned, navigate to the project directory:
code: cd repository-name


Step 3: Create a Virtual Environment
Now, create a virtual environment for managing the project dependencies.
Using venv (Built-in for Python 3.3+):
code: python3 -m venv venv
This will create a directory called venv that contains the isolated environment for the project.


Step 4: Activate the Virtual Environment
Activate the virtual environment to start working within it.
code: source venv/bin/activate
Once activated, you should see (venv) at the beginning of your terminal prompt.


Step 5: Install the Project Dependencies
With the virtual environment activated, install the required dependencies listed in the requirements.txt file by running:
pip install -r requirements.txt
This will install all the necessary packages for the project.


Step 6: Requirements.txt
file that contains a list of all the installed Python packages and their versions in the current environment.
code: pip freeze > requirements.txt
This will create a requirements.txt file containing all the installed packages in the virtual


Step 7: Deactivate the Virtual Environment
When you're done working, deactivate the virtual environment by running:
code: deactivate
This will return you to your system’s default Python environment.


Git Workflow
To keep your repository up to date with the remote, follow these steps:
Pull Latest Changes
Before starting work, make sure your local copy is up to date with the latest changes from the 
main branch: git pull origin main
Commit Changes : git add .
Commit Changes : git commit -m "Your commit message here"
Push Changes to the repository : git push origin main 

