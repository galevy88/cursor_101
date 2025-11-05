# Task Manager

A simple command-line task management application built with Python.

## Features

- ✅ Add new tasks
- 📋 List all tasks with completion status
- ✓ Mark tasks as completed
- 🗑️ Delete tasks
- 🧹 Clear all completed tasks
- 💾 Persistent storage (tasks saved to JSON file)

## Setup

1. Create a virtual environment:
   ```bash
   python3 -m venv venv
   ```

2. Activate the virtual environment:
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Project

```bash
python main.py
```

## Usage

The application provides an interactive menu:
1. Add a new task - Enter a task description
2. List all tasks - View all tasks with their status
3. Complete a task - Mark a task as done by ID
4. Delete a task - Remove a task by ID
5. Clear completed tasks - Remove all completed tasks at once
6. Exit - Quit the application

## Project Structure

```
.
├── main.py           # Main application code
├── requirements.txt  # Python dependencies
├── .gitignore       # Git ignore rules
├── .python-version  # Python version specification
├── README.md        # Project documentation
└── tasks.json       # Task storage (created automatically)
```

## Notes

- Tasks are automatically saved to `tasks.json`
- The application uses standard Python libraries (no external dependencies required)
- Press Ctrl+C to exit at any time

