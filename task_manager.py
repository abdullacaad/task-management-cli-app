"""
Task Management Application
A command-line task manager with persistent storage using JSON.
"""

import json
import os
from datetime import datetime


class Task:
    """Represents a single task with title, description, status, and timestamp."""
    
    def __init__(self, task_id, title, description="", completed=False, created_at=None):
        """
        Initialize a new task.
        
        Args:
            task_id (int): Unique identifier for the task
            title (str): Task title
            description (str): Optional task description
            completed (bool): Task completion status
            created_at (str): ISO format timestamp of creation
        """
        self.task_id = task_id
        self.title = title
        self.description = description
        self.completed = completed
        self.created_at = created_at or datetime.now().isoformat()
    
    def to_dict(self):
        """Convert task to dictionary for JSON serialization."""
        return {
            'task_id': self.task_id,
            'title': self.title,
            'description': self.description,
            'completed': self.completed,
            'created_at': self.created_at
        }
    
    @staticmethod
    def from_dict(data):
        """Create a Task object from dictionary data."""
        return Task(
            task_id=data['task_id'],
            title=data['title'],
            description=data.get('description', ''),
            completed=data.get('completed', False),
            created_at=data.get('created_at')
        )
    
    def __str__(self):
        """String representation of the task."""
        status = "✓" if self.completed else "✗"
        return f"[{status}] {self.task_id}. {self.title}"


class TaskManager:
    """Manages all task operations including CRUD and file persistence."""
    
    def __init__(self, filename='tasks.json'):
        """
        Initialize the task manager.
        
        Args:
            filename (str): Path to the JSON file for persistent storage
        """
        self.filename = filename
        self.tasks = []
        self.next_id = 1
        self.load_tasks()
    
    def load_tasks(self):
        """Load tasks from JSON file. Creates file if it doesn't exist."""
        try:
            if os.path.exists(self.filename):
                with open(self.filename, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                    self.tasks = [Task.from_dict(task_data) for task_data in data]
                    # Calculate next_id based on existing tasks
                    if self.tasks:
                        self.next_id = max(task.task_id for task in self.tasks) + 1
                print(f"✓ Loaded {len(self.tasks)} task(s) from {self.filename}")
            else:
                print(f"✓ Starting fresh - no existing tasks file found")
        except json.JSONDecodeError:
            print(f"⚠ Warning: {self.filename} is corrupted. Starting with empty task list.")
            self.tasks = []
        except Exception as e:
            print(f"⚠ Error loading tasks: {e}")
            self.tasks = []
    
    def save_tasks(self):
        """Save all tasks to JSON file with error handling."""
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                json.dump(
                    [task.to_dict() for task in self.tasks],
                    file,
                    indent=2,
                    ensure_ascii=False
                )
            return True
        except Exception as e:
            print(f"✗ Error saving tasks: {e}")
            return False
    
    def add_task(self, title, description=""):
        """
        Add a new task to the list.
        
        Args:
            title (str): Task title
            description (str): Optional task description
        
        Returns:
            Task: The newly created task object
        """
        if not title or not title.strip():
            raise ValueError("Task title cannot be empty")
        
        task = Task(self.next_id, title.strip(), description.strip())
        self.tasks.append(task)
        self.next_id += 1
        
        if self.save_tasks():
            print(f"✓ Task added successfully: '{task.title}'")
            return task
        else:
            # Rollback if save fails
            self.tasks.pop()
            self.next_id -= 1
            raise Exception("Failed to save task")
    
    def view_tasks(self):
        """Display all tasks with formatting."""
        if not self.tasks:
            print("\n📋 No tasks found. Add your first task to get started!")
            return
        
        print(f"\n📋 Your Tasks ({len(self.tasks)} total):")
        print("=" * 60)
        
        # Separate completed and pending tasks
        pending = [t for t in self.tasks if not t.completed]
        completed = [t for t in self.tasks if t.completed]
        
        if pending:
            print("\n⏳ Pending Tasks:")
            for task in pending:
                self._display_task(task)
        
        if completed:
            print("\n✓ Completed Tasks:")
            for task in completed:
                self._display_task(task)
        
        print("=" * 60)
    
    def _display_task(self, task):
        """Helper method to display a single task with details."""
        print(f"\n{task}")
        if task.description:
            print(f"   Description: {task.description}")
        # Format the timestamp
        try:
            created = datetime.fromisoformat(task.created_at)
            print(f"   Created: {created.strftime('%Y-%m-%d %H:%M')}")
        except:
            pass
    
    def mark_completed(self, task_id):
        """
        Mark a task as completed.
        
        Args:
            task_id (int): ID of the task to mark as completed
        
        Raises:
            ValueError: If task_id is not found
        """
        task = self._find_task(task_id)
        if task.completed:
            print(f"⚠ Task '{task.title}' is already completed")
            return
        
        task.completed = True
        if self.save_tasks():
            print(f"✓ Task marked as completed: '{task.title}'")
        else:
            task.completed = False
            raise Exception("Failed to save changes")
    
    def delete_task(self, task_id):
        """
        Delete a task from the list.
        
        Args:
            task_id (int): ID of the task to delete
        
        Raises:
            ValueError: If task_id is not found
        """
        task = self._find_task(task_id)
        title = task.title
        self.tasks.remove(task)
        
        if self.save_tasks():
            print(f"✓ Task deleted: '{title}'")
        else:
            # Rollback if save fails
            self.tasks.append(task)
            raise Exception("Failed to delete task")
    
    def _find_task(self, task_id):
        """
        Find a task by ID.
        
        Args:
            task_id (int): ID of the task to find
        
        Returns:
            Task: The found task object
        
        Raises:
            ValueError: If task not found
        """
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        raise ValueError(f"Task with ID {task_id} not found")


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 60)
    print("           📝 TASK MANAGEMENT SYSTEM 📝")
    print("=" * 60)
    print("1. ➕ Add a new task")
    print("2. 📋 View all tasks")
    print("3. ✓ Mark task as completed")
    print("4. 🗑 Delete a task")
    print("5. 🚪 Exit")
    print("=" * 60)


def get_user_input(prompt, input_type=str, allow_empty=False):
    """
    Get and validate user input.
    
    Args:
        prompt (str): Input prompt to display
        input_type (type): Expected type (str or int)
        allow_empty (bool): Whether to allow empty string input
    
    Returns:
        User input converted to the specified type
    
    Raises:
        ValueError: If input cannot be converted to specified type
    """
    while True:
        user_input = input(prompt).strip()
        
        if not allow_empty and not user_input:
            print("⚠ Input cannot be empty. Please try again.")
            continue
        
        if allow_empty and not user_input:
            return ""
        
        if input_type == int:
            try:
                return int(user_input)
            except ValueError:
                print("⚠ Please enter a valid number.")
                continue
        
        return user_input


def main():
    """Main application loop."""
    print("\n" + "=" * 60)
    print("     Welcome to Task Management System!")
    print("=" * 60)
    
    manager = TaskManager()
    
    while True:
        try:
            display_menu()
            choice = get_user_input("\nEnter your choice (1-5): ", int)
            
            if choice == 1:
                # Add a new task
                print("\n➕ Add New Task")
                print("-" * 60)
                title = get_user_input("Task title: ")
                description = get_user_input("Task description (optional): ", allow_empty=True)
                manager.add_task(title, description)
            
            elif choice == 2:
                # View all tasks
                manager.view_tasks()
            
            elif choice == 3:
                # Mark task as completed
                manager.view_tasks()
                if not manager.tasks:
                    continue
                
                print("\n✓ Mark Task as Completed")
                print("-" * 60)
                task_id = get_user_input("Enter task ID to mark as completed: ", int)
                manager.mark_completed(task_id)
            
            elif choice == 4:
                # Delete a task
                manager.view_tasks()
                if not manager.tasks:
                    continue
                
                print("\n🗑 Delete Task")
                print("-" * 60)
                task_id = get_user_input("Enter task ID to delete: ", int)
                confirm = get_user_input(f"Are you sure you want to delete task {task_id}? (yes/no): ")
                
                if confirm.lower() in ['yes', 'y']:
                    manager.delete_task(task_id)
                else:
                    print("⚠ Deletion cancelled")
            
            elif choice == 5:
                # Exit
                print("\n👋 Thank you for using Task Management System!")
                print("=" * 60)
                break
            
            else:
                print("⚠ Invalid choice. Please enter a number between 1 and 5.")
        
        except ValueError as e:
            print(f"⚠ Error: {e}")
        except Exception as e:
            print(f"✗ An unexpected error occurred: {e}")
        
        # Pause before showing menu again
        if choice != 5:
            input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
