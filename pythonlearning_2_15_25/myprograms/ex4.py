#!/usr/bin/env python3
"""
Simple Task Manager
A basic program to manage daily tasks with priority levels.
"""

from datetime import datetime
from typing import List, Dict

class TaskManager:
    def __init__(self):
        """Initialize an empty task list"""
        self.tasks: List[Dict] = []
    
    def add_task(self, title: str, priority: str = "medium") -> None:
        """
        Add a new task to the list
        
        Args:
            title: Task description
            priority: Priority level (low/medium/high)
        """
        task = {
            "title": title,
            "priority": priority.lower(),
            "date_added": datetime.now(),
            "completed": False
        }
        self.tasks.append(task)
        print(f"Task '{title}' added successfully!")
    
    def list_tasks(self) -> None:
        """Display all tasks with their details"""
        if not self.tasks:
            print("\nNo tasks found!")
            return
        
        print("\nCurrent Tasks:")
        print("-" * 50)
        for index, task in enumerate(self.tasks, 1):
            status = "✓" if task["completed"] else " "
            print(f"{index}. [{status}] {task['title']}")
            print(f"   Priority: {task['priority']}")
            print(f"   Added: {task['date_added'].strftime('%Y-%m-%d %H:%M')}")
            print("-" * 50)
    
    def mark_completed(self, task_index: int) -> None:
        """Mark a task as completed"""
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print("Task marked as completed!")
        else:
            print("Invalid task number!")

def main():
    """Main program function"""
    task_manager = TaskManager()
    
    while True:
        print("\n=== Task Manager ===")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Mark Task as Completed")
        print("4. Exit")
        
        try:
            choice = input("\nEnter your choice (1-4): ")
            
            if choice == "1":
                title = input("Enter task title: ")
                priority = input("Enter priority (low/medium/high): ")
                task_manager.add_task(title, priority)
                
            elif choice == "2":
                task_manager.list_tasks()
                
            elif choice == "3":
                task_manager.list_tasks()
                task_num = int(input("Enter task number to mark as completed: "))
                task_manager.mark_completed(task_num)
                
            elif choice == "4":
                print("\nThank you for using Task Manager!")
                break
                
            else:
                print("Invalid choice! Please try again.")
                
        except ValueError:
            print("Please enter a valid number!")
        except Exception as e:
            print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
