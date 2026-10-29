# Project Tracker CLI

A command-line tool for managing users, projects and tasks. Data is saved in a JSON file, so it is still there the next time you run the program.

Built for the Moringa School SDF-PT15M4 Python module.

## Description

Project Tracker is a small project management system you use from the terminal. Each **user** can have many **projects**, and each project can have many **tasks**.

Features:

- Add users (with an optional email)
- Add projects to a user (with an optional description and due date)
- Add tasks to a project
- Mark tasks as complete
- List everyone, or just one user, with their projects and tasks
- Saves and loads everything from a JSON file

The goal of the project is to practise object-oriented programming, CLI design with `argparse`, file I/O with JSON, and testing with `pytest`.

## Requirements

- Python 3.9 or newer
- The packages in `requirements.txt`: `rich`, `python-dateutil`, `pytest`

## Installation

1. Clone the repository and go into the folder:

```bash
git clone https://github.com/lesliecherop9-creator/project-tracker.git
cd project-tracker
```

2. Create and activate a virtual environment:

```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS / Linux
source .venv/bin/activate
```

3. Install the dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run every command from the project folder with `python main.py <command>`.
Names with spaces must be in quotes. Arguments are positional (no `--name` or `--title` flags), except the ones marked `--optional`.

### Add a user

```bash
python main.py add-user "Leslie"
python main.py add-user "Leslie" --email leslie@gmail.com
```

### Add a project to a user

```bash
python main.py add-project "Leslie" "Read bookclub book"
python main.py add-project "Leslie" "Read bookclub book" --description "A thousand splendid suns" --due 2026-11-01
```

### Add a task to a project

```bash
python main.py add-task "Leslie" "Read bookclub book" "Analyze chapter 1"
```

### Mark a task as complete

Use the task's number (its ID), which you can see with the `list` command.

```bash
python main.py complete-task "Leslie" "Read bookclub book" 1
```

### List users, projects and tasks

```bash
# everyone
python main.py list

# one user only
python main.py list --user "Leslie"
```

### Help

```bash
python main.py --help
python main.py add-project --help
```

### Errors

If something goes wrong (for example, the user or project does not exist), the program prints a message starting with `Error:` and exits with code 1.

## Project Structure

```
project-tracker/
├── models/             # User, Project, Task classes and custom errors
├── utils/              # saving and loading JSON data
├── tests/              # pytest tests
├── main.py             # entry point (argparse commands)
├── conftest.py         # lets pytest find the project modules
├── project_data.json   # saved data
├── requirements.txt
└── README.md
```

## Running the Tests

Make sure the virtual environment is active and you are in the project folder, then run:

```bash
pytest -v
```

## Support

If you find a bug or have a question, open an issue on the [GitHub repository](https://github.com/lesliecherop9-creator/project-tracker/issues).

## Contributing

Pull requests are welcome. For bigger changes, please open an issue first to discuss what you would like to change. Please make sure the tests still pass (`pytest -v`) and add tests for new features.

## Authors and Acknowledgment

Created by Leslie Cherop Kibor as part of the Moringa School Python module.

## Project Status

Finished as a course project. No further development is planned.