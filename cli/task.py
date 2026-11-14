class Task:
    def __init__(
        self, task_name, task_created_at, task_due_date, task_completed, task_priority
    ):
        self.task_name = task_name
        self.task_created_at = task_created_at
        self.task_due_date = task_due_date
        self.task_completed = task_completed
        self.task_priority = task_priority
