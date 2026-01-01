# Todo App - Enhanced Console Application

A feature-rich, console-based todo application written in Python that allows users to manage tasks with titles, descriptions, and comprehensive status tracking.

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
git clone <repository-url>
cd <repository-directory>
```

### 2. Verify Python Installation
```bash
python --version
# or
python3 --version
```

### 3. Run the Application
```bash
python todo_app.py
```

### 4. Alternative: Run with Python 3 (if needed)
```bash
python3 todo_app.py
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
todo_app/
├── todo_app.py          # Main application file
├── test_todo_app.py     # Test script for functionality verification
├── README.md           # This file
└── specs/              # Specification documents (if any)
```

## 🔍 Key Components

### Task Class
- **id**: Unique sequential identifier
- **title**: Task title (up to 100 characters)
- **description**: Task description (up to 500 characters)
- **completed**: Boolean status (True/False)
- **created_at**: Timestamp of when task was created

### TaskList Class
- **tasks**: List of Task objects
- **next_id**: Next available ID for new tasks
- **Methods**: add_task, get_task_by_id, update_task, mark_complete, mark_incomplete, delete_task, list_all_tasks

## 🧪 Testing

A test script is included to verify all functionality:

```bash
python test_todo_app.py
```

This will run through all major functionality and confirm that everything works correctly.

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

This project was developed as part of a Phase I Todo Application specification with the following constraints:
- In-memory storage only (no persistence)
- Single-user console application
- No external dependencies
- Menu-driven interface
- No authentication required

## 🤝 Contributing

1. Fork the repository
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