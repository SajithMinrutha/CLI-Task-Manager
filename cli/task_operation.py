import json
from datetime import datetime

from rich.console import Console
from rich.panel import Panel

from .task import Task


class TaskOperation:
    def __init__(self):
        self.tasks = []
        self.console = Console()
        self.load_tasks()

    def add_task(self):
        task_name = input("Enter The Name Of The Task: ")
        task_due_date = input("Enter The Due Date: ")
        task_priority_input = input("Enter The Priority(Low,Medium,High): ")
        task_created_at = datetime.now()
        task_completed = False
        task_priority = TaskOperation.check_priority(task_priority_input)

        new_task = Task(
            task_name, task_created_at, task_due_date, task_priority, task_completed
        )
        self.tasks.append(new_task)
        self.save_task()

    def view_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                loaded_json = json.load(f)

            self.tasks = [Task.from_dict(item) for item in loaded_json]

        except FileNotFoundError:
            self.tasks = []
            self.save_task()

        except json.JSONDecodeError:
            self.console.print("[red]Invalid JSON file![/red]")
            return

        self.console.print(
            Panel(
                f"Total tasks: {len(self.tasks)}",
                title="[bold]View Tasks[/bold]",
                border_style="blue",
                padding=(1, 2),
            )
        )

    def save_task(self):
        with open("tasks.json", "w") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

        print("Task Adding Success")

    def load_tasks(self):
        try:
            with open("tasks.json", "r") as f:
                loaded_json = json.load(f)

            self.tasks = [Task.from_dict(item) for item in loaded_json]

        except FileNotFoundError:
            self.tasks = []

        except json.JSONDecodeError:
            self.console.print("[red]Invalid JSON file![/red]")
            self.tasks = []

    # def edit_tasks(self):
    #     self.view_tasks()
    #     print("Which one would you like to edit (enter the ID)")
    #     user_input = input(":")
    #     if 0 < user_input <= len(self.tasks):
    #         correct_id = self.tasks[user_input - 1]
    #         task_name = input("Enter The Name Of The Task: ")
    #         task_due_date = input("Enter The Due Date: ")
    #         task_priority_input = input("Enter The Priority(Low,Medium,High): ")
    #         task_created_at = datetime.now()
    #         task_completed = False
    #         task_priority = TaskOperation.check_priority(task_priority_input)
    #     else:
    #         print("Invalid Input")

    def delete_tasks(self):
        self.view_tasks()
        print("Which one would you like to delete (enter the ID)")
        user_input = input(":")
        if 0 < user_input <= len(self.tasks):
            del self.tasks[user_input - 1]
        else:
            print("Invalid Input")

    @staticmethod
    def check_priority(task_priority_input):
        task_priority_list = ["Low", "Medium", "High"]
        match task_priority_input.lower():
            case "low":
                return task_priority_list[0]
            case "medium":
                return task_priority_list[1]
            case "high":
                return task_priority_list[2]
            case _:
                return "Invalid Priority"
