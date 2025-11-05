"""
Task Manager - A simple command-line task management application.
"""

import json
import os
from datetime import datetime
from typing import List, Dict


TASKS_FILE = "tasks.json"


class TaskManager:
    """Manages tasks with persistence to JSON file."""
    
    def __init__(self):
        self.tasks = self.load_tasks()
    
    def load_tasks(self) -> List[Dict]:
        """Load tasks from JSON file."""
        if os.path.exists(TASKS_FILE):
            try:
                with open(TASKS_FILE, 'r') as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                return []
        return []
    
    def save_tasks(self):
        """Save tasks to JSON file."""
        try:
            with open(TASKS_FILE, 'w') as f:
                json.dump(self.tasks, f, indent=2)
        except IOError as e:
            print(f"Error saving tasks: {e}")
    
    def add_task(self, description: str):
        """Add a new task."""
        task = {
            "id": len(self.tasks) + 1,
            "description": description,
            "completed": False,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        self.tasks.append(task)
        self.save_tasks()
        print(f"✓ Task added: {description}")
    
    def list_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("\nNo tasks found. Add some tasks to get started!")
            return
        
        print("\n" + "=" * 60)
        print("YOUR TASKS")
        print("=" * 60)
        
        for task in self.tasks:
            status = "✓" if task["completed"] else "○"
            print(f"{status} [{task['id']}] {task['description']}")
            if task["completed"]:
                print(f"    Created: {task['created_at']}")
        
        completed_count = sum(1 for t in self.tasks if t["completed"])
        total_count = len(self.tasks)
        print("=" * 60)
        print(f"Progress: {completed_count}/{total_count} completed")
        print("=" * 60 + "\n")
    
    def complete_task(self, task_id: int):
        """Mark a task as completed."""
        for task in self.tasks:
            if task["id"] == task_id:
                if task["completed"]:
                    print(f"Task [{task_id}] is already completed!")
                else:
                    task["completed"] = True
                    self.save_tasks()
                    print(f"✓ Task [{task_id}] marked as completed!")
                return
        print(f"Task [{task_id}] not found.")
    
    def delete_task(self, task_id: int):
        """Delete a task."""
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                description = task["description"]
                self.tasks.pop(i)
                self.save_tasks()
                print(f"✓ Task [{task_id}] deleted: {description}")
                return
        print(f"Task [{task_id}] not found.")
    
    def clear_completed(self):
        """Remove all completed tasks."""
        initial_count = len(self.tasks)
        self.tasks = [t for t in self.tasks if not t["completed"]]
        removed = initial_count - len(self.tasks)
        if removed > 0:
            self.save_tasks()
            print(f"✓ Removed {removed} completed task(s).")
        else:
            print("No completed tasks to remove.")
    
    def edit_task(self, task_id: int, new_description: str):
        """Edit a task's description."""
        for task in self.tasks:
            if task["id"] == task_id:
                old_description = task["description"]
                task["description"] = new_description
                self.save_tasks()
                print(f"✓ Task [{task_id}] updated:")
                print(f"  Old: {old_description}")
                print(f"  New: {new_description}")
                return
        print(f"Task [{task_id}] not found.")
    
    def show_statistics(self):
        """Display task statistics."""
        if not self.tasks:
            print("\nNo tasks to display statistics for.")
            return
        
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["completed"])
        pending = total - completed
        completion_rate = (completed / total * 100) if total > 0 else 0
        
        print("\n" + "=" * 60)
        print("TASK STATISTICS")
        print("=" * 60)
        print(f"Total tasks:        {total}")
        print(f"Completed:          {completed}")
        print(f"Pending:            {pending}")
        print(f"Completion rate:    {completion_rate:.1f}%")
        print("=" * 60 + "\n")
    
    def search_tasks(self, keyword: str):
        """Search tasks by keyword."""
        keyword_lower = keyword.lower()
        matching_tasks = [
            task for task in self.tasks
            if keyword_lower in task["description"].lower()
        ]
        

        

        if not matching_tasks:
            print(f"\nNo tasks found matching '{keyword}'.")
            return
        
        print(f"\n" + "=" * 60)
        print(f"SEARCH RESULTS: '{keyword}'")
        print("=" * 60)
        
        for task in matching_tasks:
            status = "✓" if task["completed"] else "○"
            print(f"{status} [{task['id']}] {task['description']}")
        
        print("=" * 60)
        print(f"Found {len(matching_tasks)} matching task(s).")
        print("=" * 60 + "\n")


def display_menu():
    """Display the main menu."""
    print("\n" + "=" * 60)
    print("TASK MANAGER")
    print("=" * 60)
    print("1. Add a new task")
    print("2. List all tasks")
    print("3. Complete a task")
    print("4. Delete a task")
    print("5. Clear completed tasks")
    print("6. Edit a task")
    print("7. View statistics")
    print("8. Search tasks")
    print("9. Exit")
    print("=" * 60)


def main():
    """Main application loop."""
    manager = TaskManager()
    
    print("\n" + "=" * 60)
    print("Welcome to Task Manager!")
    print("=" * 60)
    
    while True:
        display_menu()
        
        try:
            choice = input("\nEnter your choice (1-9): ").strip()
            
            if choice == "1":
                description = input("Enter task description: ").strip()
                if description:
                    manager.add_task(description)
                else:
                    print("Task description cannot be empty!")
            
            elif choice == "2":
                manager.list_tasks()
            
            elif choice == "3":
                manager.list_tasks()
                try:
                    task_id = int(input("Enter task ID to complete: ").strip())
                    manager.complete_task(task_id)
                except ValueError:
                    print("Invalid task ID. Please enter a number.")
            
            elif choice == "4":
                manager.list_tasks()
                try:
                    task_id = int(input("Enter task ID to delete: ").strip())
                    confirm = input(f"Are you sure you want to delete task [{task_id}]? (y/n): ").strip().lower()
                    if confirm == 'y':
                        manager.delete_task(task_id)
                    else:
                        print("Deletion cancelled.")
                except ValueError:
                    print("Invalid task ID. Please enter a number.")
            
            elif choice == "5":
                confirm = input("Are you sure you want to clear all completed tasks? (y/n): ").strip().lower()
                if confirm == 'y':
                    manager.clear_completed()
                else:
                    print("Operation cancelled.")
            
            elif choice == "6":
                manager.list_tasks()
                try:
                    task_id = int(input("Enter task ID to edit: ").strip())
                    new_description = input("Enter new task description: ").strip()
                    if new_description:
                        manager.edit_task(task_id, new_description)
                    else:
                        print("Task description cannot be empty!")
                except ValueError:
                    print("Invalid task ID. Please enter a number.")
            
            elif choice == "7":
                manager.show_statistics()
            
            elif choice == "8":
                keyword = input("Enter search keyword: ").strip()
                if keyword:
                    manager.search_tasks(keyword)
                else:
                    print("Search keyword cannot be empty!")
            
            elif choice == "9":
                print("\nThank you for using Task Manager! Goodbye! 👋\n")
                break
            
            else:
                print("Invalid choice. Please enter a number between 1 and 9.")
        
        except KeyboardInterrupt:
            print("\n\nExiting Task Manager. Goodbye! 👋\n")
            break
        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()
