"""
Unit tests for the services module of the Todo Application.
"""

import unittest
from src.services.task_service import TaskService


class TestTaskService(unittest.TestCase):
    """Unit tests for the TaskService."""

    def setUp(self):
        """Set up a fresh TaskService for each test."""
        self.service = TaskService()

    def test_add_task_success(self):
        """Test adding a task successfully."""
        task = self.service.add_task("Test task")
        self.assertIsNotNone(task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)

    def test_add_task_empty_description(self):
        """Test adding a task with empty description."""
        task = self.service.add_task("")
        self.assertIsNone(task)
        self.assertEqual(len(self.service.list_all_tasks()), 0)

    def test_add_task_long_description(self):
        """Test adding a task with description that's too long."""
        long_description = "x" * 201  # 201 characters, which exceeds the limit
        task = self.service.add_task(long_description)
        self.assertIsNone(task)
        self.assertEqual(len(self.service.list_all_tasks()), 0)

    def test_get_task_by_id_found(self):
        """Test getting a task that exists."""
        task = self.service.add_task("Test task")
        retrieved_task = self.service.get_task_by_id(1)
        self.assertEqual(task, retrieved_task)

    def test_get_task_by_id_not_found(self):
        """Test getting a task that doesn't exist."""
        retrieved_task = self.service.get_task_by_id(999)
        self.assertIsNone(retrieved_task)

    def test_list_all_tasks(self):
        """Test listing all tasks."""
        task1 = self.service.add_task("Task 1")
        task2 = self.service.add_task("Task 2")
        tasks = self.service.list_all_tasks()
        self.assertEqual(len(tasks), 2)
        self.assertIn(task1, tasks)
        self.assertIn(task2, tasks)

    def test_update_task_success(self):
        """Test updating a task successfully."""
        task = self.service.add_task("Original task")
        result = self.service.update_task(1, "Updated task")
        self.assertTrue(result)
        self.assertEqual(task.description, "Updated task")

    def test_update_task_not_found(self):
        """Test updating a task that doesn't exist."""
        result = self.service.update_task(999, "Updated task")
        self.assertFalse(result)

    def test_update_task_empty_description(self):
        """Test updating a task with empty description."""
        task = self.service.add_task("Original task")
        result = self.service.update_task(1, "")
        self.assertFalse(result)
        self.assertEqual(task.description, "Original task")

    def test_update_task_long_description(self):
        """Test updating a task with description that's too long."""
        task = self.service.add_task("Original task")
        long_description = "x" * 201  # 201 characters, which exceeds the limit
        result = self.service.update_task(1, long_description)
        self.assertFalse(result)
        self.assertEqual(task.description, "Original task")

    def test_mark_task_complete(self):
        """Test marking a task as complete."""
        task = self.service.add_task("Test task")
        result = self.service.mark_task_complete(1)
        self.assertTrue(result)
        self.assertTrue(task.completed)

    def test_mark_task_incomplete(self):
        """Test marking a task as incomplete."""
        task = self.service.add_task("Test task")
        task.completed = True  # First mark as complete
        result = self.service.mark_task_incomplete(1)
        self.assertTrue(result)
        self.assertFalse(task.completed)

    def test_delete_task_success(self):
        """Test deleting a task successfully."""
        task = self.service.add_task("Test task")
        self.assertEqual(len(self.service.list_all_tasks()), 1)
        result = self.service.delete_task(1)
        self.assertTrue(result)
        self.assertEqual(len(self.service.list_all_tasks()), 0)

    def test_delete_task_not_found(self):
        """Test deleting a task that doesn't exist."""
        result = self.service.delete_task(999)
        self.assertFalse(result)
        self.assertEqual(len(self.service.list_all_tasks()), 0)

    def test_validate_task_description_valid(self):
        """Test validation with a valid task description."""
        # This test checks the internal validation indirectly
        task = self.service.add_task("Valid task description")
        self.assertIsNotNone(task)

    def test_validate_task_description_empty(self):
        """Test validation with an empty task description."""
        task = self.service.add_task("")
        self.assertIsNone(task)

    def test_validate_task_description_whitespace(self):
        """Test validation with a whitespace-only task description."""
        task = self.service.add_task("   ")
        self.assertIsNone(task)

    def test_validate_task_description_too_long(self):
        """Test validation with a task description that's too long."""
        long_description = "x" * 201  # Exceeds 200 character limit
        task = self.service.add_task(long_description)
        self.assertIsNone(task)


if __name__ == '__main__':
    unittest.main()