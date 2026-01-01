"""
Models module for the Todo Application.

Contains data models and business entities for the application.
"""

from typing import List, Optional
from dataclasses import dataclass


@dataclass
class Task:
    """
    Represents a single todo item in the application.

    Attributes:
        id: Integer, unique sequential identifier, required, positive integer
        description: String, task description, required, non-empty
        completed: Boolean, completion status, required, default: false
    """
    id: int
    description: str
    completed: bool = False

    def __str__(self):
        status = "[X]" if self.completed else "[ ]"
        return f"{self.id}. {status} {self.description}"


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

    def add_task(self, description: str) -> Optional[Task]:
        """
        Creates new Task with next available ID.

        Args:
            description: The task description

        Returns:
            The created Task object or None if validation fails
        """
        if not description or not description.strip():
            return None

        task = Task(self.next_id, description.strip())
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

    def update_task(self, task_id: int, new_description: str) -> bool:
        """
        Modifies Task attributes.

        Args:
            task_id: The ID of the task to update
            new_description: The new description for the task

        Returns:
            True if the task was updated, False otherwise
        """
        if not new_description or not new_description.strip():
            return False

        task = self.get_task_by_id(task_id)
        if task:
            task.description = new_description.strip()
            return True
        return False

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