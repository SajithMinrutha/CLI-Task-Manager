import json
import os


class TaskOperation:
    def __init__(self):
        if os.path.exists("tasks.json"):
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
                print("File Loading Success!")
        else:
            with open("tasks.json", "r") as f:
                self.tasks = json.load(f)
                print("File Creating Success!")

    def add_task(
        self, task_name, task_created_at, task_due_date, task_completed, task_priority
    ):

        pass

    def view_tasks(self):
        pass

    def edit_tasks(
        new_task_name,
        new_task_created_at,
        new_task_due_date,
        new_task_completed,
        new_task_priority,
    ):
        pass

    def remove_tasks(self, task_name):
        pass

    def handle_date():
        pass
