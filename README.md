PROJECT TRACKER CLI TOOL 

A command-line application for managing users, projects, and tasks.  
This tool allows administrators to create users, assign projects, add tasks, and persist all data using JSON.  
It is built as part of the Moringa School SDF-PT15M4 Python module.

This is a Python-based CLI tool that simulates a simple project management system.  


It supports:
CREATING USERS
ASSIGNING PROJECTS TO USERS
ADDING TASKS TO PROJECTS
MARKING TASKS AS COMPLETE  
VIEWING USERS, PROJECTS AND TASKS 
SAVING AND LOADING DATA FROM JSON FILES


The goal is to practice object-oriented programming, CLI design, file I/O, and testing.


This project demonstates 

Object oriented design 
Use of mode and classes
CLI development with argparse 
JSON persistence 
Testing with pytest 
Clean project structure
Git workflow and documentation 


How to use the CLI tool
git clone 
cd Project-tracker
Install dependencies; python -m venv .venv 
.venv\Scripts\activate #windows
pip install -r requirements.txt 

USAGE 


ADD A USER 
python main.py add-user --name "Leslie"

ADD A PROJECT 
python main.py add-project --user "Leslie" --title "Website Redesign"

ADD A TASK 
python main.py add-task --project "Website Redesign" --title "Create wireframes"

MARK A TASK COMPLETE 
python main.py complete-task --project "Website Redesign" --task "Create wireframes"

LIST USERS 
python main.py list-users

LIST PROJECTS FOR A USER 
python main.py list-projects --user "Alex"

PROJECT STRUCTURE 
PROJECT-TRACKER/
├── data/
│   └── storage.json
├── models/
├── utils/
├── tests/
├── main.py
└── README.md

RUNNING TESTS 
pytest -v
