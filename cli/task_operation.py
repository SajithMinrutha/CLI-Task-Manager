import json
import os
from datetime import datetime

from rich.console import Console
from rich.panel import Panel

from .task import Task


class TaskOperation:
    def __init__(self):
        self.tasks = []
        self.console = Console()
        if os.path.exists("tasks.json"):
            try:
                with open("tasks.json", "r") as f:
                    self.tasks = json.load(f)

                print("File Loading Success!")
            except OSError as e:
                print(f"File Loading Error: {e}")

        else:
            try:
                with open("tasks.json", "w") as f:
                    json.dump([], f, indent=4)
                print("File Creating Success!")

            except OSError as e:
                print(f"File Creation Error: {e}")

    def add_task(self):
        task_priority_list = ["Low", "Medium", "High"]
        task_priority = None
        task_name = input("Enter The Name Of The Task: ")
        task_due_date = input("Enter The Due Date: ")
        task_priority_input = input("Enter The Priority(Low,Medium,High): ")
        task_created_at = datetime.now()
        task_completed = False

        match task_priority_input.lower():
            case "low":
                task_priority = task_priority_list[0]
            case "medium":
                task_priority = task_priority_list[1]
            case "high":
                task_priority = task_priority_list[2]
            case _:
                return "Invalid Priority"

        new_task = Task(
            task_name, task_created_at, task_due_date, task_priority, task_completed
        )
        self.tasks.append(new_task)
        self.save_task()

    def view_tasks(self):
        self.console.print(
            Panel(
                f"Total due {len(self.tasks)}",
                title="[bold]Add Task[/bold]",
                border_style="blue",
                padding=(1, 2),
            )
        )

        with open("tasks.json", "r", encoding="utf-8") as f:
            json_content = json.load(f)
            for items in json_content:
                print(items)

    def save_task(self):
        with open("tasks.json", "w", encoding="utf-8") as f:
            json.dump([task.to_dict() for task in self.tasks], f, indent=4)

    print("Task Adding Success")

    @staticmethod
    def edit_tasks(
        new_task_name,
        new_task_created_at,
        new_task_due_date,
        new_task_completed,
        new_task_priority,
    ):
        pass

    @staticmethod
    def delete_tasks(task_name):
        pass

    @staticmethod
    def handle_date():
        pass
