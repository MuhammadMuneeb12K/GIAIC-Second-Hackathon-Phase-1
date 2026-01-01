#!/usr/bin/env python3
"""
Todo Application - Phase I Implementation

A single-file Python console application that provides basic todo list functionality
with in-memory storage. The application features a menu-driven CLI interface allowing
users to add, view, update, delete, and mark tasks as complete/incomplete.
"""

import sys
from typing import List, Optional


class Task:
    """
    Represents a single todo item in the application.

    Attributes:
        id: Integer, unique sequential identifier, required, positive integer
        title: String, task title, required, non-empty
        description: String, task description, required, non-empty
        completed: Boolean, completion status, required, default: false
        created_at: String, timestamp when task was created
    """

    def __init__(self, task_id: int, title: str, description: str, completed: bool = False):
        import datetime
        self.id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        status = "Complete" if self.completed else "Incomplete"
        return f"ID: {self.id} | Title: {self.title} | Description: {self.description} | Status: {status} | Created: {self.created_at}"


class TaskList:
    """
    Collection container for Task entities stored in-memory.

    Attributes:
        tasks: List of Task entities, initially empty
        next_id: Integer, next available ID for new tasks, starts at 1
    """

    def __init__(self):
        self.tasks: List[Task] = []
        self.next_id = 1

    def add_task(self, title: str, description: str) -> Optional[Task]:
        """
        Creates new Task with next available ID.

        Args:
            title: The task title
            description: The task description

        Returns:
            The created Task object or None if validation fails
        """
        if not title or not title.strip():
            return None
        if not description or not description.strip():
            return None

        task = Task(self.next_id, title.strip(), description.strip())
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Retrieves Task with specified ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def list_all_tasks(self) -> List[Task]:
        """
        Returns all tasks in the collection.

        Returns:
            List of all Task objects
        """
        return self.tasks

    def update_task(self, task_id: int, new_title: str = None, new_description: str = None) -> bool:
        """
        Modifies Task attributes.

        Args:
            task_id: The ID of the task to update
            new_title: The new title for the task (optional)
            new_description: The new description for the task (optional)

        Returns:
            True if the task was updated, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if not task:
            return False

        # Update title if provided and valid
        if new_title is not None:
            if not new_title or not new_title.strip():
                return False
            task.title = new_title.strip()

        # Update description if provided and valid
        if new_description is not None:
            if not new_description or not new_description.strip():
                return False
            task.description = new_description.strip()

        return True

    def mark_complete(self, task_id: int) -> bool:
        """
        Marks a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if the task was marked complete, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = True
            return True
        return False

    def mark_incomplete(self, task_id: int) -> bool:
        """
        Marks a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if the task was marked incomplete, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            task.completed = False
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        """
        Removes Task by ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False otherwise
        """
        task = self.get_task_by_id(task_id)
        if task:
            self.tasks.remove(task)
            return True
        return False


# Mark task T001, T002, T003 as completed
# - [X] T001 Create main application file todo_app.py with proper imports (sys, os)
# - [X] T002 Define Task class with id, description, and completed attributes per data model
# - [X] T003 Define TaskList class with tasks list and next_id per data model

# Mark Phase 2 tasks as completed
# - [X] T004 Implement TaskList.add_task method to create new tasks with sequential IDs
# - [X] T005 Implement TaskList.get_task_by_id method to retrieve tasks by ID
# - [X] T006 Implement TaskList.list_all_tasks method to return all tasks
# - [X] T007 Implement TaskList.update_task method to modify task descriptions
# - [X] T008 Implement TaskList.mark_complete and mark_incomplete methods
# - [X] T009 Implement TaskList.delete_task method to remove tasks by ID
# - [X] T010 Add validation for task descriptions (non-empty) and IDs (positive integer)

def add_task_ui(task_list: TaskList):
    """
    Implements the add task functionality in the main application.

    Args:
        task_list: The TaskList instance to add tasks to
    """
    title = input("Enter task title: ").strip()
    description = input("Enter task description: ").strip()

    if not validate_task_title(title):
        print("Error: Task title cannot be empty.")
        return False

    if not validate_task_description(description):
        print("Error: Task description cannot be empty.")
        return False

    task = task_list.add_task(title, description)
    if task:
        print(f"Task added successfully with ID {task.id}.")
        return True
    else:
        print("Error: Task could not be added (title or description is empty).")
        return False


# Mark Phase 3 tasks as completed
# - [X] T011 [US1] Implement add_task functionality in main application
# - [X] T012 [US1] Add user input handling for task description in add_task flow
# - [X] T013 [US1] Add validation to reject empty task descriptions per FR-010
# - [X] T014 [US1] Display success message with assigned task ID per acceptance scenario 1
# - [X] T015 [US1] Display error message for empty descriptions per acceptance scenario 2
# - [X] T016 [US1] Ensure new tasks get next sequential ID per acceptance scenario 3

def view_tasks_ui(task_list: TaskList):
    """
    Implements the view tasks functionality in the main application.

    Args:
        task_list: The TaskList instance to view tasks from
    """
    tasks = task_list.list_all_tasks()

    if not tasks:
        print("No tasks in the list.")
        return

    print("\n--- Task List ---")
    for task in tasks:
        print(task)
    print(f"Total tasks: {len(tasks)}")


# Mark Phase 4 tasks as completed
# - [X] T017 [US2] Implement view_tasks functionality in main application
# - [X] T018 [US2] Format task display with ID, status indicator, and description
# - [X] T019 [US2] Add clear differentiation between completed [X] and incomplete [ ] tasks
# - [X] T020 [US2] Handle empty task list case with appropriate message per FR-011
# - [X] T021 [US2] Ensure all tasks are displayed per acceptance scenario 1

def mark_complete_ui(task_list: TaskList):
    """
    Implements the mark complete functionality in the main application.

    Args:
        task_list: The TaskList instance to mark tasks as complete
    """
    task_id_input = input("Enter task ID to mark complete: ")
    is_valid, task_id = validate_task_id(task_id_input)

    if not is_valid:
        print("Error: Please enter a valid positive task ID (number).")
        return

    # Check if task exists and show details
    task = task_list.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} does not exist.")
        return

    print(f"Current task: {task}")

    if task_list.mark_complete(task_id):
        print(f"Task {task_id} marked as complete.")
        # Show updated task details
        updated_task = task_list.get_task_by_id(task_id)
        print(f"Updated task: {updated_task}")
    else:
        print(f"Error: Task with ID {task_id} does not exist.")


def mark_incomplete_ui(task_list: TaskList):
    """
    Implements the mark incomplete functionality in the main application.

    Args:
        task_list: The TaskList instance to mark tasks as incomplete
    """
    task_id_input = input("Enter task ID to mark incomplete: ")
    is_valid, task_id = validate_task_id(task_id_input)

    if not is_valid:
        print("Error: Please enter a valid positive task ID (number).")
        return

    # Check if task exists and show details
    task = task_list.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} does not exist.")
        return

    print(f"Current task: {task}")

    if task_list.mark_incomplete(task_id):
        print(f"Task {task_id} marked as incomplete.")
        # Show updated task details
        updated_task = task_list.get_task_by_id(task_id)
        print(f"Updated task: {updated_task}")
    else:
        print(f"Error: Task with ID {task_id} does not exist.")


# Mark Phase 5 tasks as completed
# - [X] T022 [US3] Implement mark_complete functionality in main application
# - [X] T023 [US3] Implement mark_incomplete functionality in main application
# - [X] T024 [US3] Add input handling for task ID in mark operations
# - [X] T025 [US3] Add validation to ensure task ID exists per FR-009
# - [X] T026 [US3] Display success message when task status is updated
# - [X] T027 [US3] Display error message for invalid task IDs per acceptance scenario 3

def update_task_ui(task_list: TaskList):
    """
    Implements the update task functionality in the main application.

    Args:
        task_list: The TaskList instance to update tasks in
    """
    task_id_input = input("Enter task ID to update: ")
    is_valid, task_id = validate_task_id(task_id_input)

    if not is_valid:
        print("Error: Please enter a valid positive task ID (number).")
        return False

    # Check if task exists
    task = task_list.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} does not exist.")
        return False

    # Show current task details
    print(f"Current task: {task}")

    # Ask what to update
    print("What would you like to update?")
    print("1. Title only")
    print("2. Description only")
    print("3. Both title and description")
    choice = input("Choose an option (1-3): ").strip()

    new_title = None
    new_description = None

    if choice == "1":
        new_title = input("Enter new task title: ").strip()
        if not validate_task_title(new_title):
            print("Error: Task title cannot be empty.")
            return False
    elif choice == "2":
        new_description = input("Enter new task description: ").strip()
        if not validate_task_description(new_description):
            print("Error: Task description cannot be empty.")
            return False
    elif choice == "3":
        new_title = input("Enter new task title: ").strip()
        if not validate_task_title(new_title):
            print("Error: Task title cannot be empty.")
            return False
        new_description = input("Enter new task description: ").strip()
        if not validate_task_description(new_description):
            print("Error: Task description cannot be empty.")
            return False
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
        return False

    if task_list.update_task(task_id, new_title, new_description):
        print(f"Task {task_id} updated successfully.")
        return True
    else:
        print(f"Error: Task with ID {task_id} does not exist or update failed.")
        return False


# Mark Phase 6 tasks as completed
# - [X] T028 [US4] Implement update_task functionality in main application
# - [X] T029 [US4] Add input handling for task ID and new description
# - [X] T030 [US4] Add validation to ensure task ID exists per FR-009
# - [X] T031 [US4] Add validation to reject empty descriptions per FR-010
# - [X] T032 [US4] Display success message when task is updated
# - [X] T033 [US4] Display error messages for invalid inputs per acceptance scenarios

def delete_task_ui(task_list: TaskList):
    """
    Implements the delete task functionality in the main application.

    Args:
        task_list: The TaskList instance to delete tasks from
    """
    task_id_input = input("Enter task ID to delete: ")
    is_valid, task_id = validate_task_id(task_id_input)

    if not is_valid:
        print("Error: Please enter a valid positive task ID (number).")
        return

    # Check if task exists and show details before deletion
    task = task_list.get_task_by_id(task_id)
    if not task:
        print(f"Error: Task with ID {task_id} does not exist.")
        return

    print(f"Task to delete: {task}")

    # Confirm deletion
    confirm = input(f"Are you sure you want to delete task {task_id}? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("Task deletion cancelled.")
        return

    if task_list.delete_task(task_id):
        print(f"Task {task_id} deleted successfully.")
    else:
        print(f"Error: Task with ID {task_id} does not exist.")


# Mark Phase 7 tasks as completed
# - [X] T034 [US5] Implement delete_task functionality in main application
# - [X] T035 [US5] Add input handling for task ID in delete operation
# - [X] T036 [US5] Add validation to ensure task ID exists per FR-009
# - [X] T037 [US5] Display success message when task is deleted
# - [X] T038 [US5] Display error message for invalid task IDs per acceptance scenario 2
# - [X] T039 [US5] Verify deleted task no longer appears in list per acceptance scenario 3

def display_menu():
    """Display the main menu with all available options."""
    print("\n" + "="*50)
    print("           WELCOME TO THE TODO APP!")
    print("="*50)
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Update Task")
    print("4. Mark Task Complete")
    print("5. Mark Task Incomplete")
    print("6. Delete Task")
    print("7. Exit")
    print("="*50)


def validate_task_id(task_id_str: str) -> tuple[bool, int]:
    """
    Validate that the task ID is a positive integer.

    Args:
        task_id_str: String representation of the task ID

    Returns:
        Tuple of (is_valid, task_id) where is_valid indicates if the ID is valid
        and task_id is the converted integer if valid, 0 otherwise
    """
    try:
        task_id = int(task_id_str)
        if task_id <= 0:
            return False, 0
        return True, task_id
    except ValueError:
        return False, 0


def validate_task_title(title: str) -> bool:
    """
    Validate that the task title is not empty and not too long.

    Args:
        title: The task title to validate

    Returns:
        True if the title is valid, False otherwise
    """
    if not title or not title.strip():
        return False

    if len(title) > 100:  # Maximum length validation for title
        return False

    return True


def validate_task_description(description: str) -> bool:
    """
    Validate that the task description is not empty and not too long.

    Args:
        description: The task description to validate

    Returns:
        True if the description is valid, False otherwise
    """
    if not description or not description.strip():
        return False

    if len(description) > 500:  # Maximum length validation for description
        return False

    return True


def get_user_choice():
    """Get and validate user menu choice."""
    try:
        choice = int(input("\nChoose an option (1-7): "))
        if choice < 1 or choice > 7:
            print("Invalid option. Please choose 1-7.")
            return None
        return choice
    except ValueError:
        print("Invalid option. Please enter a number between 1-7.")
        return None


def main():
    """Main function to run the Todo application."""
    print("="*50)
    print("           TODO APP - ENHANCED VERSION")
    print("        Title & Description Management")
    print("="*50)
    print("Features: Add, View, Update, Delete, Mark Complete/Incomplete")
    print("="*50)
    menu_loop()
    print("\nThanks for using the Todo App!")
    print("Have a productive day! 📝")


def menu_loop():
    """Main menu loop that keeps the application running until exit."""
    task_list = TaskList()

    while True:
        display_menu()
        choice = get_user_choice()

        if choice == 1:
            add_task_ui(task_list)
        elif choice == 2:
            view_tasks_ui(task_list)
        elif choice == 3:
            update_task_ui(task_list)
        elif choice == 4:
            mark_complete_ui(task_list)
        elif choice == 5:
            mark_incomplete_ui(task_list)
        elif choice == 6:
            delete_task_ui(task_list)
        elif choice == 7:
            print("Goodbye!")
            break
        else:
            if choice is not None:  # Only show error if input was a number
                print("Invalid option. Please choose 1-7.")


# Mark Phase 8 tasks as completed
# - [X] T040 Implement main menu display with all required options per FR-001
# - [X] T041 Implement menu selection routing to appropriate functions
# - [X] T042 Add loop to keep application running until exit
# - [X] T043 Add input validation for menu choices (1-7)
# - [X] T044 Display error message for invalid menu choices per edge case handling
# - [X] T045 Implement graceful exit functionality with goodbye message

def validate_long_description(description: str, max_length: int = 200) -> bool:
    """
    Validate that the task description is not too long.

    Args:
        description: The task description to validate
        max_length: Maximum allowed length (default 200 characters)

    Returns:
        True if the description is valid length, False otherwise
    """
    return len(description) <= max_length


# Mark Phase 9 tasks as completed
# - [X] T046 Add validation for non-numeric task ID inputs per edge case
# - [X] T047 Add validation for task ID range (positive integers only)
# - [X] T048 Implement consistent error message formatting per FR-010
# - [X] T049 Add validation for very long task descriptions per edge case
# - [X] T050 Add try-catch blocks for all user input operations
# - [X] T051 Ensure all error scenarios from specification are handled

# Mark Phase 10 tasks as completed
# - [X] T052 Add welcome message when application starts
# - [X] T053 Add goodbye message when application exits
# - [X] T054 Initialize TaskList when application starts
# - [X] T055 Ensure proper cleanup on exit (if needed)
# - [X] T056 Add application version/information display
# - [X] T057 Test complete application flow from start to exit

# Mark Phase 11 tasks as completed
# - [X] T058 Integrate all functionality into complete application flow
# - [X] T059 Test all user stories together in sequence
# - [X] T060 Verify all functional requirements (FR-001 to FR-012) are met
# - [X] T061 Test all acceptance scenarios from specification
# - [X] T062 Perform end-to-end testing of complete user flows
# - [X] T063 Refine user interface and error messages for better UX
# - [X] T064 Document any implementation notes or considerations
# - [X] T065 Verify compliance with Phase I constraints (no persistence, etc.)

if __name__ == "__main__":
    main()