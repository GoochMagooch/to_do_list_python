Hi Charles,

As part of our ongoing effort to improve utility tools for internal use, I’d like you to take ownership of a new scripting task.

Objective
Build a simple, command-line To-Do List Manager that allows users to add, view, complete, and remove tasks. The goal is to provide a lightweight and intuitive tool for quick task tracking.

Requirements

- Data Structure:
    Use a dictionary where:
      - Keys represent task names (strings)
      - Values are booleans: False for incomplete, True for complete

- Core Features:
    1. Add a Task – Prompt the user to enter a task name and store it as incomplete.
    2. Mark as Complete – Allow the user to mark any existing task as complete.
    3. View Tasks – Display all tasks with clear indicators of completion status.
    4. Remove a Task – Remove a task based on its name.
    5. Exit – Include a confirmation step before terminating the program.

- Additional Parameters:
    Input validation (e.g., prevent empty task names).
    Graceful handling of nonexistent tasks or duplicates.
    Clear output formatting (e.g., ✓ for complete, ✗ for incomplete).
    Maintain consistent user experience in the CLI.

You do not need to include any file-saving or persistence in this version — keep it in-memory for now. Focus on clean logic, modular structure, and user-friendly feedback.

Let me know if anything is unclear or if you'd like to walk through the requirements together. Looking forward to your implementation.

Best,
Kali
Team Lead, Internal Tools Development
Systems Design Consultancy LLC

## notes
- Make sure each function persists until 'back' is entered, or a valid choice is entered
- Check for duplicate check marks on completed tasks
- Add options to end function loops