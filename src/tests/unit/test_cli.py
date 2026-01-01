"""
Unit tests for the CLI module of the Todo Application.
"""

import unittest
from unittest.mock import patch, MagicMock
from io import StringIO
from src.cli.menu import TaskCLI


class TestTaskCLI(unittest.TestCase):
    """Unit tests for the TaskCLI."""

    def setUp(self):
        """Set up a fresh TaskCLI for each test."""
        self.cli = TaskCLI()

    def test_display_menu(self):
        """Test that display_menu method runs without error."""
        # This test verifies the method can be called without errors
        with patch('sys.stdout', new=StringIO()):
            self.cli.display_menu()
        # If no exception is raised, the test passes

    def test_validate_task_id_valid_positive(self):
        """Test validating a valid positive task ID."""
        is_valid, task_id = self.cli._validate_task_id("5")
        self.assertTrue(is_valid)
        self.assertEqual(task_id, 5)

    def test_validate_task_id_invalid_negative(self):
        """Test validating a negative task ID."""
        is_valid, task_id = self.cli._validate_task_id("-5")
        self.assertFalse(is_valid)
        self.assertEqual(task_id, 0)

    def test_validate_task_id_invalid_zero(self):
        """Test validating a zero task ID."""
        is_valid, task_id = self.cli._validate_task_id("0")
        self.assertFalse(is_valid)
        self.assertEqual(task_id, 0)

    def test_validate_task_id_invalid_non_numeric(self):
        """Test validating a non-numeric task ID."""
        is_valid, task_id = self.cli._validate_task_id("abc")
        self.assertFalse(is_valid)
        self.assertEqual(task_id, 0)

    def test_validate_task_description_valid(self):
        """Test validating a valid task description."""
        is_valid = self.cli._validate_task_description("Valid task description")
        self.assertTrue(is_valid)

    def test_validate_task_description_empty(self):
        """Test validating an empty task description."""
        is_valid = self.cli._validate_task_description("")
        self.assertFalse(is_valid)

    def test_validate_task_description_whitespace(self):
        """Test validating a whitespace-only task description."""
        is_valid = self.cli._validate_task_description("   ")
        self.assertFalse(is_valid)

    def test_validate_task_description_too_long(self):
        """Test validating a task description that's too long."""
        long_description = "x" * 201  # Exceeds 200 character limit
        is_valid = self.cli._validate_task_description(long_description)
        self.assertFalse(is_valid)

    @patch('builtins.input', side_effect=['Test task'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task_ui_success(self, mock_stdout, mock_input):
        """Test adding a task through the UI successfully."""
        result = self.cli.add_task_ui()
        self.assertTrue(result)
        output = mock_stdout.getvalue()
        self.assertIn("Task added successfully", output)

    @patch('builtins.input', side_effect=[''])
    @patch('sys.stdout', new_callable=StringIO)
    def test_add_task_ui_empty_description(self, mock_stdout, mock_input):
        """Test adding a task with empty description through the UI."""
        result = self.cli.add_task_ui()
        self.assertFalse(result)
        output = mock_stdout.getvalue()
        self.assertIn("Error: Task description cannot be empty", output)

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_view_tasks_ui_empty_list(self, mock_stdout, mock_input):
        """Test viewing tasks when the list is empty."""
        self.cli.view_tasks_ui()
        output = mock_stdout.getvalue()
        self.assertIn("No tasks in the list", output)

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_mark_complete_ui_not_found(self, mock_stdout, mock_input):
        """Test marking a task complete when it doesn't exist."""
        self.cli.mark_complete_ui()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Task with ID 1 does not exist", output)

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_mark_incomplete_ui_not_found(self, mock_stdout, mock_input):
        """Test marking a task incomplete when it doesn't exist."""
        self.cli.mark_incomplete_ui()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Task with ID 1 does not exist", output)

    @patch('builtins.input', side_effect=['1', 'Updated task'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_update_task_ui_not_found(self, mock_stdout, mock_input):
        """Test updating a task when it doesn't exist."""
        result = self.cli.update_task_ui()
        self.assertFalse(result)
        output = mock_stdout.getvalue()
        self.assertIn("Error: Task with ID 1 does not exist", output)

    @patch('builtins.input', side_effect=['1'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_delete_task_ui_not_found(self, mock_stdout, mock_input):
        """Test deleting a task when it doesn't exist."""
        self.cli.delete_task_ui()
        output = mock_stdout.getvalue()
        self.assertIn("Error: Task with ID 1 does not exist", output)

    @patch('builtins.input', side_effect=['999'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_invalid_range(self, mock_stdout, mock_input):
        """Test getting user choice with invalid range."""
        choice = self.cli.get_user_choice()
        output = mock_stdout.getvalue()
        self.assertIsNone(choice)
        self.assertIn("Invalid option", output)

    @patch('builtins.input', side_effect=['abc'])
    @patch('sys.stdout', new_callable=StringIO)
    def test_get_user_choice_invalid_input(self, mock_stdout, mock_input):
        """Test getting user choice with invalid input."""
        choice = self.cli.get_user_choice()
        output = mock_stdout.getvalue()
        self.assertIsNone(choice)
        self.assertIn("Invalid option", output)


if __name__ == '__main__':
    unittest.main()