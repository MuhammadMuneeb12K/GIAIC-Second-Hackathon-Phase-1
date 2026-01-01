"""
Integration tests for the Todo Application.
Tests the interaction between different modules/components.
"""

import unittest
from src.models.task import Task, TaskList
from src.services.task_service import TaskService
from src.cli.menu import TaskCLI


class TestIntegration(unittest.TestCase):
    """Integration tests for the Todo Application."""

    def test_full_task_lifecycle(self):
        """Test the complete lifecycle of a task through all layers."""
        service = TaskService()

        # Add a task
        task = service.add_task("Integration test task")
        self.assertIsNotNone(task)
        self.assertEqual(task.id, 1)
        self.assertEqual(task.description, "Integration test task")
        self.assertFalse(task.completed)

        # Verify task exists in the list
        tasks = service.list_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], task)

        # Update the task
        update_result = service.update_task(1, "Updated integration test task")
        self.assertTrue(update_result)
        updated_task = service.get_task_by_id(1)
        self.assertEqual(updated_task.description, "Updated integration test task")

        # Mark as complete
        complete_result = service.mark_task_complete(1)
        self.assertTrue(complete_result)
        completed_task = service.get_task_by_id(1)
        self.assertTrue(completed_task.completed)

        # Mark as incomplete
        incomplete_result = service.mark_task_incomplete(1)
        self.assertTrue(incomplete_result)
        incomplete_task = service.get_task_by_id(1)
        self.assertFalse(incomplete_task.completed)

        # Delete the task
        delete_result = service.delete_task(1)
        self.assertTrue(delete_result)
        deleted_task = service.get_task_by_id(1)
        self.assertIsNone(deleted_task)

        # Verify task list is empty
        final_tasks = service.list_all_tasks()
        self.assertEqual(len(final_tasks), 0)

    def test_multiple_tasks_lifecycle(self):
        """Test lifecycle with multiple tasks."""
        service = TaskService()

        # Add multiple tasks
        task1 = service.add_task("First task")
        task2 = service.add_task("Second task")
        task3 = service.add_task("Third task")

        self.assertIsNotNone(task1)
        self.assertIsNotNone(task2)
        self.assertIsNotNone(task3)

        # Verify all tasks exist
        all_tasks = service.list_all_tasks()
        self.assertEqual(len(all_tasks), 3)

        # Verify IDs are sequential
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)

        # Update middle task
        update_result = service.update_task(2, "Updated second task")
        self.assertTrue(update_result)
        updated_task = service.get_task_by_id(2)
        self.assertEqual(updated_task.description, "Updated second task")

        # Mark one as complete
        service.mark_task_complete(1)
        completed_task = service.get_task_by_id(1)
        self.assertTrue(completed_task.completed)

        # Delete a task and verify others remain
        delete_result = service.delete_task(2)
        self.assertTrue(delete_result)

        remaining_tasks = service.list_all_tasks()
        self.assertEqual(len(remaining_tasks), 2)

        # Verify the right task was deleted
        self.assertIsNone(service.get_task_by_id(2))
        self.assertIsNotNone(service.get_task_by_id(1))
        self.assertIsNotNone(service.get_task_by_id(3))

    def test_model_service_integration(self):
        """Test that models and services work together correctly."""
        task_list = TaskList()

        # Add task directly to model
        task = task_list.add_task("Direct model task")
        self.assertIsNotNone(task)

        # Verify it's in the list
        tasks = task_list.list_all_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0], task)

        # Update via model
        update_result = task_list.update_task(1, "Updated direct model task")
        self.assertTrue(update_result)
        self.assertEqual(task.description, "Updated direct model task")

        # Mark complete via model
        complete_result = task_list.mark_complete(1)
        self.assertTrue(complete_result)
        self.assertTrue(task.completed)

    def test_cli_service_integration(self):
        """Test that CLI and service layers work together."""
        service = TaskService()

        # Add a task using service
        task = service.add_task("Service task")
        self.assertIsNotNone(task)

        # Verify CLI can access it through service
        cli = TaskCLI()
        cli.task_service = service  # Inject the same service instance

        # The CLI's service should have the same task
        cli_task = cli.task_service.get_task_by_id(1)
        self.assertEqual(cli_task, task)
        self.assertEqual(cli_task.description, "Service task")

    def test_sequential_id_assignment_after_deletion(self):
        """Test that IDs are properly managed after deletions."""
        service = TaskService()

        # Add several tasks
        task1 = service.add_task("Task 1")
        task2 = service.add_task("Task 2")
        task3 = service.add_task("Task 3")
        task4 = service.add_task("Task 4")

        # Verify IDs
        self.assertEqual(task1.id, 1)
        self.assertEqual(task2.id, 2)
        self.assertEqual(task3.id, 3)
        self.assertEqual(task4.id, 4)

        # Delete middle tasks
        service.delete_task(2)
        service.delete_task(3)

        # Add new tasks - they should continue the sequence
        task5 = service.add_task("Task 5")
        task6 = service.add_task("Task 6")

        # Verify new IDs continue the sequence
        self.assertEqual(task5.id, 5)
        self.assertEqual(task6.id, 6)

        # Verify remaining tasks still have their original IDs
        remaining_task = service.get_task_by_id(1)
        self.assertEqual(remaining_task, task1)

        # Verify deleted tasks are gone
        self.assertIsNone(service.get_task_by_id(2))
        self.assertIsNone(service.get_task_by_id(3))

    def test_validation_consistency_across_layers(self):
        """Test that validation is consistent across models, services, and CLI."""
        service = TaskService()
        cli = TaskCLI()
        cli.task_service = service

        # Test empty description at service level
        empty_task = service.add_task("")
        self.assertIsNone(empty_task)

        # Test long description at service level
        long_description = "x" * 201  # Exceeds 200 char limit
        long_task = service.add_task(long_description)
        self.assertIsNone(long_task)

        # Test validation methods consistency
        service_validation = service._validate_task_description("Valid task")
        cli_validation = cli._validate_task_description("Valid task")
        self.assertEqual(service_validation, cli_validation)
        self.assertTrue(service_validation)

        # Test invalid validation consistency
        service_invalid = service._validate_task_description("")
        cli_invalid = cli._validate_task_description("")
        self.assertEqual(service_invalid, cli_invalid)
        self.assertFalse(service_invalid)


if __name__ == '__main__':
    unittest.main()