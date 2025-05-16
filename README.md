🧾 Simple To-Do List Manager (CLI Tool)
You’ve been asked to build a lightweight terminal-based to-do list app that lets a user manage their tasks efficiently.

🔧 Requirements:
✅ Data Structure:
Use a dict to store tasks:

Keys = Task names (strings)

Values = Booleans (False = incomplete, True = complete)

✅ Features:
Add a Task

Ask the user for a task name.

Add it to the dictionary as incomplete.

Mark Task as Complete

Ask the user to enter the task name.

Mark it as complete if it exists.

View Tasks

List all tasks.

Show whether each one is complete or incomplete.

Remove a Task

Ask the user for the task name.

Remove it from the list.

Exit Program

Graceful exit with confirmation.

💡 Additional Requirements:
Handle duplicates gracefully.

If user enters a task that doesn't exist, print a helpful message.

Validate input types where appropriate.

Format output clearly (✓ for complete, ✗ for incomplete).