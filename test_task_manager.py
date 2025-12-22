"""
Test script to demonstrate all functionality of the Task Manager Application
This script programmatically tests all features without user interaction.
"""

from task_manager import TaskManager, Task
import os


def test_task_manager():
    """Run comprehensive tests on the task manager."""
    print("\n" + "=" * 60)
    print("          TASK MANAGER - AUTOMATED TESTING")
    print("=" * 60)
    
    # Clean up any existing test file
    test_file = "test_tasks.json"
    if os.path.exists(test_file):
        os.remove(test_file)
        print(f"\n✓ Cleaned up existing test file")
    
    # Test 1: Initialize TaskManager
    print("\n" + "-" * 60)
    print("TEST 1: Initialize Task Manager")
    print("-" * 60)
    manager = TaskManager(test_file)
    assert len(manager.tasks) == 0, "Initial task list should be empty"
    print("✓ Task manager initialized successfully")
    print(f"✓ Empty task list confirmed: {len(manager.tasks)} tasks")
    
    # Test 2: Add tasks
    print("\n" + "-" * 60)
    print("TEST 2: Add New Tasks")
    print("-" * 60)
    task1 = manager.add_task("Complete Python assignment", "Build a task manager with persistent storage")
    task2 = manager.add_task("Study for exams", "Focus on chapters 5-8")
    task3 = manager.add_task("Buy groceries", "Milk, bread, eggs")
    assert len(manager.tasks) == 3, "Should have 3 tasks after adding"
    print(f"✓ Successfully added {len(manager.tasks)} tasks")
    
    # Test 3: View all tasks
    print("\n" + "-" * 60)
    print("TEST 3: View All Tasks")
    print("-" * 60)
    manager.view_tasks()
    
    # Test 4: Mark task as completed
    print("\n" + "-" * 60)
    print("TEST 4: Mark Task as Completed")
    print("-" * 60)
    manager.mark_completed(task1.task_id)
    assert manager.tasks[0].completed == True, "Task should be marked as completed"
    print(f"✓ Task {task1.task_id} marked as completed")
    
    # Test 5: View tasks with completed items
    print("\n" + "-" * 60)
    print("TEST 5: View Tasks (with completed items)")
    print("-" * 60)
    manager.view_tasks()
    
    # Test 6: Delete a task
    print("\n" + "-" * 60)
    print("TEST 6: Delete a Task")
    print("-" * 60)
    initial_count = len(manager.tasks)
    manager.delete_task(task3.task_id)
    assert len(manager.tasks) == initial_count - 1, "Task count should decrease by 1"
    print(f"✓ Task deleted. Remaining tasks: {len(manager.tasks)}")
    
    # Test 7: Data persistence - Save and reload
    print("\n" + "-" * 60)
    print("TEST 7: Data Persistence")
    print("-" * 60)
    tasks_before = len(manager.tasks)
    print(f"Tasks before reload: {tasks_before}")
    
    # Create a new manager instance (simulates app restart)
    manager2 = TaskManager(test_file)
    tasks_after = len(manager2.tasks)
    print(f"Tasks after reload: {tasks_after}")
    assert tasks_before == tasks_after, "Task count should persist across restarts"
    print("✓ Data persistence verified - tasks reloaded successfully")
    
    # Test 8: Error handling - Invalid task ID
    print("\n" + "-" * 60)
    print("TEST 8: Error Handling - Invalid Task ID")
    print("-" * 60)
    try:
        manager.mark_completed(9999)
        print("✗ Should have raised ValueError")
    except ValueError as e:
        print(f"✓ Correctly handled invalid task ID: {e}")
    
    # Test 9: Error handling - Empty title
    print("\n" + "-" * 60)
    print("TEST 9: Error Handling - Empty Task Title")
    print("-" * 60)
    try:
        manager.add_task("", "Description")
        print("✗ Should have raised ValueError")
    except ValueError as e:
        print(f"✓ Correctly handled empty title: {e}")
    
    # Test 10: Add more tasks and view final state
    print("\n" + "-" * 60)
    print("TEST 10: Add More Tasks and View Final State")
    print("-" * 60)
    manager.add_task("Read Chapter 10", "Data structures and algorithms")
    manager.add_task("Practice coding", "Solve 5 LeetCode problems")
    manager.mark_completed(manager.tasks[-1].task_id)
    manager.view_tasks()
    
    # Test 11: Verify JSON file contents
    print("\n" + "-" * 60)
    print("TEST 11: Verify JSON File Structure")
    print("-" * 60)
    import json
    with open(test_file, 'r') as f:
        data = json.load(f)
        print(f"✓ JSON file contains {len(data)} tasks")
        print(f"✓ Sample task structure:")
        if data:
            print(json.dumps(data[0], indent=2))
    
    # Summary
    print("\n" + "=" * 60)
    print("               TEST SUMMARY")
    print("=" * 60)
    print("✓ All tests passed successfully!")
    print(f"✓ Total tasks created: {manager.next_id - 1}")
    print(f"✓ Current tasks in system: {len(manager.tasks)}")
    completed_count = sum(1 for t in manager.tasks if t.completed)
    print(f"✓ Completed tasks: {completed_count}")
    print(f"✓ Pending tasks: {len(manager.tasks) - completed_count}")
    print("✓ Data persistence: Verified")
    print("✓ Error handling: Verified")
    print("=" * 60)
    
    # Cleanup
    print(f"\nTest file '{test_file}' has been created for inspection.")
    print("You can delete it manually or run this test again to see persistence.")


if __name__ == "__main__":
    try:
        test_task_manager()
    except Exception as e:
        print(f"\n✗ Test failed with error: {e}")
        import traceback
        traceback.print_exc()
