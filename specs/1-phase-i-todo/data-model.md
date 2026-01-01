# Data Model: Phase I Todo Application

## Task Entity

**Definition**: Represents a single todo item in the application

**Attributes**:
- `id`: Integer, unique sequential identifier, required, positive integer
- `description`: String, task description, required, non-empty
- `completed`: Boolean, completion status, required, default: false

**Validation Rules**:
- ID must be a positive integer
- Description must be non-empty string
- Completed status must be boolean value
- ID must be unique within the TaskList

**State Transitions**:
- New Task: `completed = false` (default)
- Mark Complete: `completed = true`
- Mark Incomplete: `completed = false`

## TaskList Entity

**Definition**: Collection container for Task entities stored in-memory

**Attributes**:
- `tasks`: List of Task entities, initially empty
- `next_id`: Integer, next available ID for new tasks, starts at 1

**Operations**:
- Add Task: Creates new Task with next available ID
- Get Task by ID: Retrieves Task with specified ID
- Update Task: Modifies Task attributes
- Delete Task: Removes Task by ID
- List All Tasks: Returns all tasks in the collection

**Validation Rules**:
- All contained elements must be valid Task entities
- IDs must remain unique across all tasks
- Next available ID must increment properly

## Data Relationships

- TaskList contains zero or more Task entities
- Each Task has exactly one parent TaskList (conceptual, in-memory only)