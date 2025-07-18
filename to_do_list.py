import os

# File path constant
TODO_FILE = r"C:\Users\sbada\OneDrive\Documents\python_practise\simple_projects\to_do_list\To_do_list.txt"

# Load tasks from file at startup
tasks = {}
if os.path.exists(TODO_FILE):
    with open(TODO_FILE, "r") as file:
        for line in file:
            line = line.strip()
            if line and ':' in line:
                task, status = line.split(':')
                tasks[task.strip().lower()] = status.strip().lower()

def save_tasks():
    """Save all tasks to the file"""
    with open(TODO_FILE, "w") as file:
        for task, status in tasks.items():
            file.write(f"{task}:{status}\n")

def add_task(task_name):
    """Add a new task to the list"""
    task = task_name.strip().lower()
    if not task:
        print("Error: Task name cannot be empty")
        return
    if task in tasks:
        print("Error: Task already exists")
        return
    
    while True:
        status = input("Have you completed this task? (yes/no): ").strip().lower()
        if status in ('yes', 'no'):
            tasks[task] = 'done' if status == 'yes' else 'not done'
            save_tasks()
            print(f"Task '{task_name}' added successfully!")
            break
        print("Invalid input. Please enter 'yes' or 'no'.")

def task_status(task_name):
    """Update or check task status"""
    task = task_name.strip().lower()
    if task not in tasks:
        print("Error: Task not found")
        return
    
    if tasks[task] == "done":
        print("The task is already completed")
    else:
        tasks[task] = "done"
        save_tasks()
        print("The task has been marked as complete")

def delete_task(task_name):
    """Remove a task from the list"""
    task = task_name.strip().lower()
    if task not in tasks:
        print("Error: Task not found")
        return
    
    del tasks[task]
    save_tasks()
    print("Task successfully removed")

def list_tasks():
    """Display all tasks with their status"""
    if not tasks:
        print("No tasks in your to-do list")
        return
    
    print("\nYour To-Do List:")
    for i, (task, status) in enumerate(tasks.items(), 1):
        status_display = "✓ Done" if status == 'done' else "✗ Pending"
        print(f"{i}. {task.capitalize()} - {status_display}")

# Example usage:
if __name__ == "__main__":
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Delete Task")
        print("4. View All Tasks")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            task_name = input("Enter task name: ")
            add_task(task_name)
        elif choice == '2':
            task_name = input("Enter task name to mark as done: ")
            task_status(task_name)
        elif choice == '3':
            task_name = input("Enter task name to delete: ")
            delete_task(task_name)
        elif choice == '4':
            list_tasks()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-5.")