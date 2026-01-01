# Quickstart Guide: Phase I Todo Application

## Prerequisites

- Python 3.8 or higher installed
- No additional dependencies required

## Running the Application

1. Save the application code to a file named `todo_app.py`
2. Run the application using Python:
   ```bash
   python todo_app.py
   ```

## Basic Usage

### Main Menu Options
The application presents a menu with the following options:
1. Add Task - Add a new task to your list
2. View Tasks - Display all tasks with their status
3. Update Task - Modify an existing task description
4. Mark Complete - Mark a task as complete
5. Mark Incomplete - Mark a task as incomplete
6. Delete Task - Remove a task from the list
7. Exit - Quit the application

### Adding a Task
1. Select option 1 from the main menu
2. Enter your task description when prompted
3. The task will be added with a unique ID and "Incomplete" status

### Viewing Tasks
1. Select option 2 from the main menu
2. All tasks will be displayed with their ID, description, and completion status
3. Completed tasks will be marked with [X], incomplete tasks with [ ]

### Updating a Task
1. Select option 3 from the main menu
2. Enter the task ID you want to update
3. Enter the new task description
4. The task description will be updated

### Marking Tasks Complete/Incomplete
1. Select option 4 (Complete) or 5 (Incomplete) from the menu
2. Enter the task ID you want to update
3. The task status will be changed accordingly

### Deleting a Task
1. Select option 6 from the main menu
2. Enter the task ID you want to delete
3. The task will be removed from the list

## Error Handling

- Invalid task IDs will result in an error message
- Empty task descriptions are not allowed
- Empty task lists will display an appropriate message
- Invalid menu choices will prompt for valid input

## Example Session

```
Welcome to the Todo App!
1. Add Task
2. View Tasks
3. Update Task
4. Mark Complete
5. Mark Incomplete
6. Delete Task
7. Exit
Choose an option: 1
Enter task description: Buy groceries
Task added successfully with ID 1.

Choose an option: 2
1. [ ] Buy groceries

Choose an option: 4
Enter task ID to mark complete: 1
Task 1 marked as complete.

Choose an option: 2
1. [X] Buy groceries

Choose an option: 7
Goodbye!
```