"""
CLI module for the Todo Application.

Contains user interface and command-line interaction logic.
"""

from typing import Optional
from src.services.task_service import TaskService


class TaskCLI:
    """
    Command-Line Interface for the Todo Application.
    Handles user interaction and menu navigation.
    """

    def __init__(self):
        self.task_service = TaskService()

    def display_menu(self):
        """Display the main menu with all available options."""
        print("\nWelcome to the Todo App!")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Complete")
        print("5. Mark Incomplete")
        print("6. Delete Task")
        print("7. Exit")

    def get_user_choice(self) -> Optional[int]:
        """Get and validate user menu choice."""
        try:
            choice = int(input("Choose an option: "))
            if choice < 1 or choice > 7:
                print("Invalid option. Please choose 1-7.")
                return None
            return choice
        except ValueError:
            print("Invalid option. Please choose 1-7.")
            return None

    def add_task_ui(self):
        """
        Implements the add task functionality in the CLI.

        Returns:
            True if task was added successfully, False otherwise
        """
        description = input("Enter task description: ").strip()

        if not self._validate_task_description(description):
            print("Error: Task description cannot be empty.")
            return False

        task = self.task_service.add_task(description)
        if task:
            print(f"Task added successfully with ID {task.id}.")
            return True
        else:
            print("Error: Task description cannot be empty.")
            return False

    def view_tasks_ui(self):
        """Implements the view tasks functionality in the CLI."""
        tasks = self.task_service.list_all_tasks()

        if not tasks:
            print("No tasks in the list.")
            return

        for task in tasks:
            print(task)

    def mark_complete_ui(self):
        """Implements the mark complete functionality in the CLI."""
        task_id_input = input("Enter task ID to mark complete: ")
        is_valid, task_id = self._validate_task_id(task_id_input)

        if not is_valid:
            print("Error: Please enter a valid positive task ID (number).")
            return

        if self.task_service.mark_task_complete(task_id):
            print(f"Task {task_id} marked as complete.")
        else:
            print(f"Error: Task with ID {task_id} does not exist.")

    def mark_incomplete_ui(self):
        """Implements the mark incomplete functionality in the CLI."""
        task_id_input = input("Enter task ID to mark incomplete: ")
        is_valid, task_id = self._validate_task_id(task_id_input)

        if not is_valid:
            print("Error: Please enter a valid positive task ID (number).")
            return

        if self.task_service.mark_task_incomplete(task_id):
            print(f"Task {task_id} marked as incomplete.")
        else:
            print(f"Error: Task with ID {task_id} does not exist.")

    def update_task_ui(self):
        """
        Implements the update task functionality in the CLI.

        Returns:
            True if task was updated successfully, False otherwise
        """
        task_id_input = input("Enter task ID to update: ")
        is_valid, task_id = self._validate_task_id(task_id_input)

        if not is_valid:
            print("Error: Please enter a valid positive task ID (number).")
            return False

        new_description = input("Enter new task description: ").strip()

        if not self._validate_task_description(new_description):
            print("Error: Task description cannot be empty.")
            return False

        if self.task_service.update_task(task_id, new_description):
            print(f"Task {task_id} updated successfully.")
            return True
        else:
            print(f"Error: Task with ID {task_id} does not exist.")
            return False

    def delete_task_ui(self):
        """Implements the delete task functionality in the CLI."""
        task_id_input = input("Enter task ID to delete: ")
        is_valid, task_id = self._validate_task_id(task_id_input)

        if not is_valid:
            print("Error: Please enter a valid positive task ID (number).")
            return

        if self.task_service.delete_task(task_id):
            print(f"Task {task_id} deleted successfully.")
        else:
            print(f"Error: Task with ID {task_id} does not exist.")

    def _validate_task_id(self, task_id_str: str) -> tuple[bool, int]:
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

    def _validate_task_description(self, description: str) -> bool:
        """
        Validate that the task description is not empty and not too long.

        Args:
            description: The task description to validate

        Returns:
            True if the description is valid, False otherwise
        """
        if not description or not description.strip():
            return False

        if len(description) > 200:  # Maximum length validation
            return False

        return True

    def run(self):
        """Main application loop that keeps the application running until exit."""
        print("Welcome to the Todo App!")
        print("Version 1.0 - Phase I Implementation")

        while True:
            self.display_menu()
            choice = self.get_user_choice()

            if choice == 1:
                self.add_task_ui()
            elif choice == 2:
                self.view_tasks_ui()
            elif choice == 3:
                self.update_task_ui()
            elif choice == 4:
                self.mark_complete_ui()
            elif choice == 5:
                self.mark_incomplete_ui()
            elif choice == 6:
                self.delete_task_ui()
            elif choice == 7:
                print("Goodbye!")
                print("Thanks for using the Todo App!")
                break
            else:
                if choice is not None:  # Only show error if input was a number
                    print("Invalid option. Please choose 1-7.")