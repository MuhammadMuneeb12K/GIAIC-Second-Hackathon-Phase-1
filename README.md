# GIAIC Second Hackathon - Phase I Todo App

A professional, feature-rich Python console application that provides comprehensive todo list functionality with in-memory storage. The application features a menu-driven CLI interface allowing users to add, view, update, delete, and mark tasks as complete/incomplete with both titles and descriptions.

## 🌟 Features

- **Add Tasks** with both title and description
- **View All Tasks** with detailed information (ID, Title, Description, Status, Creation Time)
- **Update Tasks** (title, description, or both)
- **Mark Tasks Complete/Incomplete**
- **Delete Tasks** with confirmation
- **In-Memory Storage** (no persistence beyond runtime)
- **Comprehensive Validation** for inputs
- **User-Friendly Menu Interface**

## 🛠️ Tech Stack

- **Language**: Python 3.8+
- **Architecture**: Console-based, single-file application
- **Storage**: In-memory (no external databases or files)
- **Pattern**: Object-oriented design with Task and TaskList classes

## 📋 Requirements

- Python 3.8 or higher
- No external dependencies required

## 🚀 Setup Instructions

### 1. Clone or Download the Repository
```bash
git clone https://github.com/MuhammadMuneeb12K/GIAIC-Second-Hackathon-Phase-1.git
cd GIAIC-Second-Hackathon-Phase-1
```

### 2. Verify Python Installation
```bash
python --version
# or
python3 --version
```

### 3. Run the Enhanced Application
```bash
python todo_app.py
```

### 4. Alternative: Run with Python 3 (if needed)
```bash
python3 todo_app.py
```

### 5. For Development: Run from src directory (if needed)
```bash
python src/main.py
```

## 🎯 How to Use

### Main Menu Options:
1. **Add Task** - Create a new task with title and description
2. **View All Tasks** - Display all tasks with detailed information
3. **Update Task** - Modify task title, description, or both
4. **Mark Task Complete** - Change task status to complete
5. **Mark Task Incomplete** - Change task status to incomplete
6. **Delete Task** - Remove a task with confirmation
7. **Exit** - Close the application

### Example Workflow:
1. Run `python todo_app.py`
2. Choose option 1 to add a task
3. Enter a title (e.g., "Buy groceries")
4. Enter a description (e.g., "Milk, bread, eggs, fruits")
5. Use other options to manage your tasks
6. Exit when done

## 🏗️ Project Structure

```
GIAIC-Second-Hackathon-Phase-1/
├── todo_app.py                    # Main enhanced application file with title/description functionality
├── test_todo_app.py              # Test script for functionality verification
├── README.md                     # Project documentation
├── CLAUDE.md                     # Claude Code rules and configuration
├── PROJECT_STRUCTURE.md          # Project structure documentation
├── pyproject.toml               # Python project configuration
├── requirements.txt             # Python dependencies
├── setup.py                     # Setup configuration
├── __pycache__/                 # Python cache directory
├── .claude/                     # Claude Code configuration
├── .specify/                    # Specification framework files
├── history/                     # Prompt history records
│   └── prompts/                 # History of prompts and interactions
│       ├── constitution/        # Constitution-related prompts
│       └── phase-i-todo/        # Todo app implementation prompts
├── specs/                       # Project specifications
│   └── 1-phase-i-todo/         # Phase I todo app specifications
│       ├── spec.md             # Feature specification
│       ├── plan.md             # Implementation plan
│       ├── tasks.md            # Implementation tasks
│       ├── data-model.md       # Data model specification
│       ├── research.md         # Research documentation
│       ├── quickstart.md       # Quick start guide
│       └── checklists/         # Checklists and requirements
│           └── requirements.md
└── src/                        # Source code directory
    ├── __init__.py
    ├── main.py                 # Alternative main application entry point
    ├── models/                 # Data models
    │   ├── __init__.py
    │   ├── task.py            # Task model definition
    │   └── __pycache__/       # Python cache
    ├── services/               # Business logic services
    │   ├── __init__.py
    │   ├── task_service.py    # Task service implementation
    │   └── __pycache__/       # Python cache
    ├── cli/                    # Command-line interface
    │   ├── __init__.py
    │   ├── menu.py            # Menu interface implementation
    │   └── __pycache__/       # Python cache
    └── tests/                  # Test suite
        ├── __init__.py
        ├── unit/               # Unit tests
        │   ├── __init__.py
        │   ├── test_models.py
        │   ├── test_services.py
        │   ├── test_cli.py
        │   └── __pycache__/
        └── integration/        # Integration tests
            ├── __init__.py
            ├── test_integration.py
            └── __pycache__/
```

## 🔍 Key Components

### Main Application (todo_app.py)
- **Task Class**: Represents individual tasks with id, title, description, completion status, and creation timestamp
  - **id**: Unique sequential identifier
  - **title**: Task title (up to 100 characters)
  - **description**: Task description (up to 500 characters)
  - **completed**: Boolean status (True/False)
  - **created_at**: Timestamp of when task was created
- **TaskList Class**: Manages collection of tasks in memory
  - **tasks**: List of Task objects
  - **next_id**: Next available ID for new tasks
  - **Methods**: add_task, get_task_by_id, update_task, mark_complete, mark_incomplete, delete_task, list_all_tasks
- **UI Functions**: Interactive menu system with add, view, update, delete, and mark operations

### Source Code Structure (src/)
- **models/task.py**: Task model definition
- **services/task_service.py**: Business logic for task operations
- **cli/menu.py**: Command-line interface implementation
- **tests/**: Comprehensive unit and integration tests

## 🧪 Testing

Two testing approaches are available:

### 1. Enhanced Test Script
Run the dedicated test script that verifies all enhanced functionality:

```bash
python test_todo_app.py
```

This will run through all major functionality with titles and descriptions and confirm that everything works correctly.

### 2. Unit Tests
Run the comprehensive unit test suite:

```bash
# Run all tests
python -m unittest discover src/tests/ -v

# Run specific test modules
python -m unittest src.tests.unit.test_models -v
python -m unittest src.tests.unit.test_services -v
python -m unittest src.tests.unit.test_cli -v
python -m unittest src.tests.integration.test_integration -v
```

All tests validate both the original functionality and the enhanced features with titles and descriptions.

## 📖 Functionality Details

### Adding Tasks
- Requires both title and description
- Validates that inputs are not empty
- Assigns unique sequential IDs
- Sets completion status to incomplete by default
- Records creation timestamp

### Viewing Tasks
- Displays all tasks with comprehensive details
- Shows ID, title, description, status, and creation time
- Displays total count of tasks
- Clean, formatted output

### Updating Tasks
- Choose to update title, description, or both
- Validates new inputs before updating
- Shows current task details before update
- Provides clear feedback on success/failure

### Marking Complete/Incomplete
- Shows current task details before changing status
- Updates status and displays the change
- Validates that the task exists before updating

### Deleting Tasks
- Shows task details before deletion
- Requires confirmation before deleting
- Provides feedback on success/failure

## 🛡️ Validation & Error Handling

- **Task Title**: Must be 1-100 characters, non-empty
- **Task Description**: Must be 1-500 characters, non-empty
- **Task ID**: Must be a positive integer
- **Input Validation**: Handles invalid menu choices and non-numeric inputs
- **Error Messages**: Clear, actionable feedback for all error scenarios

## 📝 Development Notes

This project was developed as part of a Second Hackathon - Phase I Todo Application with the following characteristics:
- **Enhanced Functionality**: Added title and description fields to tasks
- **In-Memory Storage**: No persistence beyond runtime
- **Single-User Console Application**: Menu-driven interface
- **No External Dependencies**: Pure Python implementation
- **Comprehensive Validation**: Input validation for all fields
- **Professional Structure**: Organized codebase with models, services, CLI, and tests
- **Specification Driven**: Built following detailed specifications in the specs/ directory

## 🤝 Contributing

1. Fork the repository at [https://github.com/MuhammadMuneeb12K/GIAIC-Second-Hackathon-Phase-1](https://github.com/MuhammadMuneeb12K/GIAIC-Second-Hackathon-Phase-1)
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is available for educational and personal use.

## 🆘 Support

If you encounter any issues:
1. Ensure you're using Python 3.8+
2. Check that you're running the script from the correct directory
3. Verify that the `todo_app.py` file exists in the current directory
4. Run the test script to verify functionality: `python test_todo_app.py`
5. Visit the repository: [https://github.com/MuhammadMuneeb12K/GIAIC-Second-Hackathon-Phase-1](https://github.com/MuhammadMuneeb12K/GIAIC-Second-Hackathon-Phase-1)

## 🚀 Future Enhancements

Potential features for future phases could include:
- Data persistence (file or database storage)
- User authentication
- Web interface
- Task categories/priorities
- Due dates and reminders
- Export functionality

---

Made with ❤️ for productive task management!