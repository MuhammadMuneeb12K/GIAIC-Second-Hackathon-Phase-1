# CLI Operations Contract: Phase I Todo Application

## Overview
This document defines the contract for all CLI operations in the Phase I Todo Application. Each operation follows a consistent input/output pattern with standardized error handling.

## Common Response Format
- Success: Human-readable confirmation message
- Error: Human-readable error message prefixed with "Error:" or "Invalid:"

## Operation Definitions

### 1. Add Task
**Command**: User selects option 1 and enters description
**Input**: Task description string (non-empty)
**Output**: Success message with assigned task ID
**Validations**:
- Description must not be empty
- Description must be a string
**Success Example**: "Task added successfully with ID 1."
**Error Example**: "Error: Task description cannot be empty."

### 2. View Tasks
**Command**: User selects option 2
**Input**: None
**Output**: Formatted list of all tasks with ID, status, and description
**Validations**: None
**Success Example**:
```
1. [ ] Buy groceries
2. [X] Complete project
```
**Error Example**: "No tasks in the list."

### 3. Update Task
**Command**: User selects option 3 and provides task ID and new description
**Input**: Task ID (integer), new description (non-empty string)
**Output**: Success confirmation
**Validations**:
- Task ID must exist in the list
- New description must not be empty
**Success Example**: "Task 1 updated successfully."
**Error Examples**:
- "Error: Task with ID 1 does not exist."
- "Error: Task description cannot be empty."

### 4. Mark Complete
**Command**: User selects option 4 and provides task ID
**Input**: Task ID (integer)
**Output**: Success confirmation
**Validations**: Task ID must exist in the list
**Success Example**: "Task 1 marked as complete."
**Error Example**: "Error: Task with ID 1 does not exist."

### 5. Mark Incomplete
**Command**: User selects option 5 and provides task ID
**Input**: Task ID (integer)
**Output**: Success confirmation
**Validations**: Task ID must exist in the list
**Success Example**: "Task 1 marked as incomplete."
**Error Example**: "Error: Task with ID 1 does not exist."

### 6. Delete Task
**Command**: User selects option 6 and provides task ID
**Input**: Task ID (integer)
**Output**: Success confirmation
**Validations**: Task ID must exist in the list
**Success Example**: "Task 1 deleted successfully."
**Error Example**: "Error: Task with ID 1 does not exist."

### 7. Exit
**Command**: User selects option 7
**Input**: None
**Output**: Exit message and application termination
**Validations**: None
**Success Example**: "Goodbye!"

## Input Validation
- All task IDs must be positive integers
- All task descriptions must be non-empty strings
- All menu selections must be integers between 1 and 7
- Invalid inputs result in error messages and return to main menu

## Error Handling Patterns
- Invalid task ID: "Error: Task with ID X does not exist."
- Empty description: "Error: Task description cannot be empty."
- Invalid menu choice: "Invalid option. Please choose 1-7."
- Empty task list: "No tasks in the list."