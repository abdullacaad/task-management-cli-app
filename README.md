# 📝 Task Management Application

A command-line task management system with persistent storage built in Python. This application allows you to create, view, complete, and delete tasks with all data automatically saved to a JSON file.

## ✨ Features

- ➕ **Add Tasks**: Create new tasks with titles and optional descriptions
- 📋 **View Tasks**: Display all tasks organized by status (pending/completed)
- ✓ **Mark Complete**: Mark tasks as completed when done
- 🗑️ **Delete Tasks**: Remove tasks you no longer need
- 💾 **Persistent Storage**: All tasks are automatically saved to `tasks.json`
- 🔄 **Data Persistence**: Tasks reload automatically when you restart the application
- 🛡️ **Error Handling**: Robust error handling for all operations
- 🎨 **User-Friendly Interface**: Clean, menu-driven CLI with visual indicators

## 🎯 What This App Does

This Task Management Application helps you organize your daily tasks efficiently. You can:
- Keep track of your to-do items
- Add detailed descriptions to tasks
- Monitor which tasks are completed
- Maintain a persistent list that survives program restarts
- Easily manage your workload through a simple menu interface

## 📋 Requirements

- **Python Version**: Python 3.6 or higher
- **Dependencies**: No external libraries required (uses only Python standard library)
  - `json` - for data persistence
  - `os` - for file operations
  - `datetime` - for timestamps

## 🚀 How to Run

### Step 1: Clone or Download the Repository

```bash
git clone <repository-url>
cd project
```

### Step 2: Verify Python Installation

```bash
python --version
```

Make sure you have Python 3.6 or higher installed.

### Step 3: Run the Application

```bash
python task_manager.py
```

### Step 4: Use the Menu

Once the application starts, you'll see a menu with the following options:

```
1. ➕ Add a new task
2. 📋 View all tasks
3. ✓ Mark task as completed
4. 🗑 Delete a task
5. 🚪 Exit
```

Simply enter the number corresponding to your choice and follow the prompts.

## 💡 Usage Examples

### Adding a Task

```
Enter your choice (1-5): 1

➕ Add New Task
------------------------------------------------------------
Task title: Complete Python assignment
Task description (optional): Build a task manager with persistent storage
✓ Task added successfully: 'Complete Python assignment'
```

### Viewing All Tasks

```
Enter your choice (1-5): 2

📋 Your Tasks (3 total):
============================================================

⏳ Pending Tasks:

[✗] 1. Complete Python assignment
   Description: Build a task manager with persistent storage
   Created: 2025-12-22 14:30

[✗] 2. Study for exams
   Created: 2025-12-22 14:32

✓ Completed Tasks:

[✓] 3. Buy groceries
   Description: Milk, bread, eggs
   Created: 2025-12-22 13:15
============================================================
```

### Marking a Task as Completed

```
Enter your choice (1-5): 3

[Shows task list]

✓ Mark Task as Completed
------------------------------------------------------------
Enter task ID to mark as completed: 1
✓ Task marked as completed: 'Complete Python assignment'
```

### Deleting a Task

```
Enter your choice (1-5): 4

[Shows task list]

🗑 Delete Task
------------------------------------------------------------
Enter task ID to delete: 3
Are you sure you want to delete task 3? (yes/no): yes
✓ Task deleted: 'Buy groceries'
```

## 📁 Project Structure

```
project/
│
├── task_manager.py      # Main application file
├── tasks.json           # Auto-generated data storage file
├── README.md            # This file
└── .gitignore          # Git ignore rules
```

## 🔧 Technical Details

### Data Structure

Tasks are stored as JSON objects with the following structure:

```json
{
  "task_id": 1,
  "title": "Task title",
  "description": "Optional description",
  "completed": false,
  "created_at": "2025-12-22T14:30:00.123456"
}
```

### Classes

- **Task**: Represents a single task with properties and methods for serialization
- **TaskManager**: Handles all CRUD operations and file I/O with error handling

### Error Handling

The application handles:
- ✓ Invalid menu choices
- ✓ Empty task lists
- ✓ Invalid task IDs
- ✓ File not found errors
- ✓ JSON corruption
- ✓ Empty input validation
- ✓ File save failures with rollback

All errors display clear, user-friendly messages with emoji indicators (⚠, ✗).

## 🎨 Code Quality

- **PEP 8 Compliant**: Follows Python naming conventions and formatting standards
- **Object-Oriented**: Uses classes for clean code organization
- **Documented**: Comprehensive docstrings for all classes and methods
- **Type Hints**: Parameter types documented in docstrings
- **Error Recovery**: Automatic rollback on save failures

## 💾 Data Persistence

All tasks are automatically saved to `tasks.json` after every operation:
- Adding a task
- Marking a task as completed
- Deleting a task

When you restart the application, all your tasks are automatically loaded from the file.

## 🧪 Testing Checklist

- [x] Add new tasks with and without descriptions
- [x] View tasks when list is empty
- [x] View tasks with multiple items
- [x] Mark tasks as completed
- [x] Delete tasks with confirmation
- [x] Restart application and verify data persistence
- [x] Test invalid menu choices
- [x] Test invalid task IDs
- [x] Test empty input handling
- [x] Test file corruption recovery

## 🤝 Contributing

This is a student project for learning purposes. Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 📝 Assignment Requirements

This project fulfills all requirements for the Python Task Management Application:

✅ **Core Features**: Add, view, complete, delete tasks with menu-based CLI  
✅ **Data Handling**: Uses dictionaries/lists with JSON file persistence  
✅ **Code Quality**: Object-oriented with PEP 8 compliance  
✅ **Error Handling**: Comprehensive try/except blocks with clear messages  
✅ **Documentation**: Complete README and inline comments  
✅ **Version Control**: Git repository with multiple commits  
✅ **Testing**: All functionality tested and verified  

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Author

Created as part of Python programming coursework.

---

**Submission Date**: January 26, 2026 - 4:30 PM
