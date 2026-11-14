from datetime import datetime


class Task:
    id = 0

    def __init__(
        self,
        task_name,
        task_created_at,
        task_due_date,
        task_priority,
        task_completed,
        task_id=None,
    ):
        if task_id is None:
            Task.id += 1
            self.id = Task.id
        else:
            self.id = task_id
            Task.id = max(Task.id, task_id)

        self.task_name = task_name
        self.task_created_at = task_created_at
        self.task_due_date = task_due_date
        self.task_priority = task_priority
        self.task_completed = task_completed

    def to_dict(self):
        return {
            "id": self.id,
            "task_name": self.task_name,
            "task_created_at": self.task_created_at.isoformat(),
            "task_due_date": self.task_due_date,
            "task_priority": self.task_priority,
            "task_completed": self.task_completed,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            task_name=data["task_name"],
            task_created_at=datetime.fromisoformat(data["task_created_at"]),
            task_due_date=data["task_due_date"],
            task_priority=data["task_priority"],
            task_completed=data["task_completed"],
            task_id=data["id"],
        )
