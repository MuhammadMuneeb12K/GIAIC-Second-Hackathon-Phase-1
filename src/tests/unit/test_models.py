"""
Unit tests for the models module of the Todo Application.
"""

import unittest
from src.models.task import Task, TaskList


class TestTask(unittest.TestCase):
    """Unit tests for the Task model."""

    def test_task_creation(self):
        """Test creating a Task instance."""
        task = Task(id=1, description="Test task", completed=False)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)

    def test_task_str_representation(self):
        """Test the string representation of a Task."""
        task_incomplete = Task(id=1, description="Test task", completed=False)
        self.assertEqual(str(task_incomplete), "1. [ ] Test task")

        task_complete = Task(id=1, description="Test task", completed=True)
        self.assertEqual(str(task_complete), "1. [X] Test task")


class TestTaskList(unittest.TestCase):
    """Unit tests for the TaskList model."""

    def setUp(self):
        """Set up a fresh TaskList for each test."""
        self.task_list = TaskList()

    def test_add_task_success(self):
        """Test adding a task successfully."""
        task = self.task_list.add_task("Test task")
        self.assertIsNotNone(task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)
        self.assertEqual(len(self.task_list.tasks), 1)

    def test_add_task_empty_description(self):
        """Test adding a task with empty description."""
        task = self.task_list.add_task("")
        self.assertIsNone(task)
        self.assertEqual(len(self.task_list.tasks), 0)

    def test_add_task_whitespace_description(self):
        """Test adding a task with whitespace-only description."""
        task = self.task_list.add_task("   ")
        self.assertIsNone(task)
        self.assertEqual(len(self.task_list.tasks), 0)

    def test_get_task_by_id_found(self):
        """Test getting a task that exists."""
        task = self.task_list.add_task("Test task")
        retrieved_task = self.task_list.get_task_by_id(1)
        self.assertEqual(task, retrieved_task)

    def test_get_task_by_id_not_found(self):
        """Test getting a task that doesn't exist."""
        retrieved_task = self.task_list.get_task_by_id(999)
        self.assertIsNone(retrieved_task)

    def test_list_all_tasks(self):
        """Test listing all tasks."""
        task1 = self.task_list.add_task("Task 1")
        task2 = self.task_list.add_task("Task 2")
        tasks = self.task_list.list_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn(task1, tasks)
        self.assertIn(task2, tasks)

    def test_update_task_success(self):
        """Test updating a task successfully."""
        task = self.task_list.add_task("Original task")
        result = self.task_list.update_task(1, "Updated task")
        self.assertTrue(result)
        self.assertEqual(task.description, "Updated task")

    def test_update_task_not_found(self):
        """Test updating a task that doesn't exist."""
        result = self.task_list.update_task(999, "Updated task")
        self.assertFalse(result)

    def test_update_task_empty_description(self):
        """Test updating a task with empty description."""
        task = self.task_list.add_task("Original task")
        result = self.task_list.update_task(1, "")
        self.assertFalse(result)
        self.assertEqual(task.description, "Original task")

    def test_mark_complete(self):
        """Test marking a task as complete."""
        task = self.task_list.add_task("Test task")
        result = self.task_list.mark_complete(1)
        self.assertTrue(result)
        self.assertTrue(task.completed)

    def test_mark_incomplete(self):
        """Test marking a task as incomplete."""
        task = self.task_list.add_task("Test task")
        task.completed = True  # First mark as complete
        result = self.task_list.mark_incomplete(1)
        self.assertTrue(result)
        self.assertFalse(task.completed)

    def test_delete_task_success(self):
        """Test deleting a task successfully."""
        task = self.task_list.add_task("Test task")
        self.assertEqual(len(self.task_list.tasks), 1)
        result = self.task_list.delete_task(1)
        self.assertTrue(result)
        self.assertEqual(len(self.task_list.tasks), 0)

    def test_delete_task_not_found(self):
        """Test deleting a task that doesn't exist."""
        result = self.task_list.delete_task(999)
        self.assertFalse(result)
        self.assertEqual(len(self.task_list.tasks), 0)

    def test_sequential_id_assignment(self):
        """Test that tasks get sequential IDs."""
        task1 = self.task_list.add_task("Task 1")
        task2 = self.task_list.add_task("Task 2")
        task3 = self.task_list.add_task("Task 3")

        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)

    def test_next_id_after_deletion(self):
        """Test that IDs continue to increment even after deletion."""
        task1 = self.task_list.add_task("Task 1")
        task2 = self.task_list.add_task("Task 2")
        self.task_list.delete_task(1)  # Delete first task
        task3 = self.task_list.add_task("Task 3")

        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)  # Should be 3, not 2


if __name__ == '__main__':
    unittest.main()