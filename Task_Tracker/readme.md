# Task Tracker CLI

The Task Tracker CLI is a simple command-line interface application that allows you to manage your tasks. With this tool, you can add, update, delete, and track the status of your tasks.

## Features

- Add new tasks
- Update existing tasks
- Delete tasks
- Mark tasks as "in progress" or "done"
- List all tasks
- List tasks by status (todo, in progress, done)

## Usage

To use the Task Tracker CLI, follow these steps:

1. Ensure you have Python 3 installed on your system.
2. Save the `task_tracker.py` file to your desired directory.
3. Open a terminal or command prompt and navigate to the directory containing the `task_tracker.py` file.
4. Run the script using the following command:

   ```
   python task_tracker.py
   ```

   This will display the usage instructions.

5. Use the following commands to interact with the Task Tracker:

   ```
   # Add a new task
   python task_tracker.py add "Buy groceries"

   # Update an existing task
   python task_tracker.py update 1 "Buy groceries and cook dinner"

   # Mark a task as in progress
   python task_tracker.py mark-in-progress 1

   # Mark a task as done
   python task_tracker.py mark-done 1

   # List all tasks
   python task_tracker.py list

   # List tasks by status
   python task_tracker.py list todo
   python task_tracker.py list done
   python task_tracker.py list in-progress

   # Delete a task
   python task_tracker.py delete 1
   ```

## Implementation Details

The Task Tracker CLI is implemented using Python 3. It stores the tasks in a JSON file named `tasks.json` in the same directory as the `task_tracker.py` script.

The script uses the following functions to manage the tasks:

- `create_task(description)`: Adds a new task to the list.
- `update_task(task_id, new_description)`: Updates the description of an existing task.
- `delete_task(task_id)`: Removes a task from the list.
- `mark_task_in_progress(task_id)`: Marks a task as "in progress".
- `mark_task_done(task_id)`: Marks a task as "done".
- `list_tasks(status=None)`: Lists all tasks or tasks by a specific status.
- `load_tasks()`: Loads the tasks from the JSON file.
- `save_tasks(tasks)`: Saves the tasks to the JSON file.

The script uses the `datetime` module to track the creation and update timestamps for each task.

## Contributing

If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/your-username/task-tracker-cli).

## License

This project is licensed under the [MIT License](LICENSE).
