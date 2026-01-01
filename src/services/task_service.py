"""
Services module for the Todo Application.

Contains business logic and service layer functionality.
"""

from typing import List, Optional
from src.models.task import Task, TaskList


class TaskService:
    """
    Service layer for task management operations.
    Handles business logic and validation for task operations.
    """

    def __init__(self):
        self.task_list = TaskList()

    def add_task(self, description: str) -> Optional[Task]:
        """
        Add a new task with validation.

        Args:
            description: The task description

        Returns:
            The created Task object or None if validation fails
        """
        if not self._validate_task_description(description):
            return None
        return self.task_list.add_task(description)

    def get_task_by_id(self, task_id: int) -> Optional[Task]:
        """
        Get a task by its ID.

        Args:
            task_id: The ID of the task to retrieve

        Returns:
            The Task object if found, None otherwise
        """
        return self.task_list.get_task_by_id(task_id)

    def list_all_tasks(self) -> List[Task]:
        """
        Get all tasks.

        Returns:
            List of all Task objects
        """
        return self.task_list.list_all_tasks()

    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Update a task's description with validation.

        Args:
            task_id: The ID of the task to update
            new_description: The new description for the task

        Returns:
            True if the task was updated, False otherwise
        """
        if not self._validate_task_description(new_description):
            return False
        return self.task_list.update_task(task_id, new_description)

    def mark_task_complete(self, task_id: int) -> bool:
        """
        Mark a task as complete.

        Args:
            task_id: The ID of the task to mark complete

        Returns:
            True if the task was marked complete, False otherwise
        """
        return self.task_list.mark_complete(task_id)

    def mark_task_incomplete(self, task_id: int) -> bool:
        """
        Mark a task as incomplete.

        Args:
            task_id: The ID of the task to mark incomplete

        Returns:
            True if the task was marked incomplete, False otherwise
        """
        return self.task_list.mark_incomplete(task_id)

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task by ID.

        Args:
            task_id: The ID of the task to delete

        Returns:
            True if the task was deleted, False otherwise
        """
        return self.task_list.delete_task(task_id)

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

    def _validate_task_id(self, task_id: int) -> bool:
        """
        Validate that the task ID is a positive integer.

        Args:
            task_id: The task ID to validate

        Returns:
            True if the ID is valid, False otherwise
        """
        return task_id > 0