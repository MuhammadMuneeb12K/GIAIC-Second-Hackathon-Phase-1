#!/usr/bin/env python3
"""
Test script for the enhanced todo app with title and description functionality
"""
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from todo_app import Task, TaskList

def test_task_creation():
    """Test creating tasks with title and description"""
    print("Testing Task Creation...")

    # Create a TaskList instance
    task_list = TaskList()

    # Add a task with title and description
    task = task_list.add_task("Buy groceries", "Buy milk, bread, eggs, and fruits from the supermarket")

    if task:
        print(f"[PASS] Task created successfully with ID: {task.id}")
        print(f"  Title: {task.title}")
        print(f"  Description: {task.description}")
        print(f"  Status: {'Complete' if task.completed else 'Incomplete'}")
        print(f"  Created: {task.created_at}")
    else:
        print("[FAIL] Failed to create task")
        return False

    # Add another task
    task2 = task_list.add_task("Complete project", "Finish the todo app enhancement project and test all features")

    if task2:
        print(f"[PASS] Second task created successfully with ID: {task2.id}")
    else:
        print("[FAIL] Failed to create second task")
        return False

    # List all tasks
    print("\nTesting Task Listing...")
    tasks = task_list.list_all_tasks()
    print(f"Total tasks: {len(tasks)}")

    for task in tasks:
        print(f"  {task}")

    # Test updating a task
    print("\nTesting Task Update...")
    success = task_list.update_task(task.id, "Updated title", "Updated description for testing")
    if success:
        print("[PASS] Task updated successfully")
        updated_task = task_list.get_task_by_id(task.id)
        print(f"  Updated task: {updated_task}")
    else:
        print("[FAIL] Failed to update task")
        return False

    # Test marking complete/incomplete
    print("\nTesting Mark Complete...")
    success = task_list.mark_complete(task.id)
    if success:
        print("[PASS] Task marked as complete")
        updated_task = task_list.get_task_by_id(task.id)
        print(f"  Updated status: {updated_task}")
    else:
        print("[FAIL] Failed to mark task as complete")
        return False

    # Test marking incomplete
    print("\nTesting Mark Incomplete...")
    success = task_list.mark_incomplete(task.id)
    if success:
        print("[PASS] Task marked as incomplete")
        updated_task = task_list.get_task_by_id(task.id)
        print(f"  Updated status: {updated_task}")
    else:
        print("[FAIL] Failed to mark task as incomplete")
        return False

    # Test deletion
    print("\nTesting Task Deletion...")
    success = task_list.delete_task(task.id)
    if success:
        print("[PASS] Task deleted successfully")
        remaining_tasks = task_list.list_all_tasks()
        print(f"  Remaining tasks: {len(remaining_tasks)}")
    else:
        print("[FAIL] Failed to delete task")
        return False

    print("\n[SUCCESS] All tests passed! The enhanced todo app functionality works correctly.")
    return True

if __name__ == "__main__":
    print("Running tests for the enhanced todo app...")
    print("="*60)

    success = test_task_creation()

    print("="*60)
    if success:
        print("[SUCCESS] All tests completed successfully!")
    else:
        print("[ERROR] Some tests failed!")
        sys.exit(1)