import os
import json
from datetime import datetime

TASK_FILE = "tasks.json"

def create_task(description): # Create a new task
    tasks = load_tasks()
    task_id = len(tasks) + 1
    new_task = {
        "id": task_id,
        "description": description,
        "status": "todo",
        "createdAt": datetime.now().isoformat(),
        "updatedAt": datetime.now().isoformat()
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task added successfully (ID: {task_id})")

def update_task(task_id, new_description): # Update a task
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} updated successfully")
            return
    print(f"Task {task_id} not found")

def delete_task(task_id): # Delete a task
    tasks = load_tasks()
    for i, task in enumerate(tasks):
        if task["id"] == task_id:
            del tasks[i]
            save_tasks(tasks)
            print(f"Task {task_id} deleted successfully")
            return
    print(f"Task {task_id} not found")

def mark_task_in_progress(task_id): # Mark a task as in-progress
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "in-progress"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as in-progress")
            return
    print(f"Task {task_id} not found")

def mark_task_done(task_id): # Mark a task as done
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["status"] = "done"
            task["updatedAt"] = datetime.now().isoformat()
            save_tasks(tasks)
            print(f"Task {task_id} marked as done")
            return
    print(f"Task {task_id} not found")

def list_tasks(status=None): # List all tasks
    tasks = load_tasks()
    if status:
        tasks = [task for task in tasks if task["status"] == status]
    for task in tasks:
        print(f"{task['id']}. {task['description']} - Status: {task['status']}")

def load_tasks(): # Load tasks from file
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    else:
        return []

def save_tasks(tasks):  # Save tasks to file
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f, indent=2)

if __name__ == "__main__": # Command-line interface
    import sys

    if len(sys.argv) < 2:
        print("Usage: task-cli <command> [arguments]")
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    if command == "add": 
        if len(args) < 1:  # Check if the user has provided a description
            print("Usage: task-cli add <description>") 
        else:
            create_task(args[0])
    elif command == "update":
        if len(args) < 2:
            print("Usage: task-cli update <id> <new_description>")
        else:
            update_task(int(args[0]), args[1])
    elif command == "delete":
        if len(args) < 1:
            print("Usage: task-cli delete <id>")
        else:
            delete_task(int(args[0]))
    elif command == "mark-in-progress":
        if len(args) < 1:
            print("Usage: task-cli mark-in-progress <id>")
        else:
            mark_task_in_progress(int(args[0]))
    elif command == "mark-done":
        if len(args) < 1:
            print("Usage: task-cli mark-done <id>")
        else:
            mark_task_done(int(args[0]))
    elif command == "list":
        if len(args) < 1:
            list_tasks()
        else:
            list_tasks(args[0])
    else:
        print("Unknown command")