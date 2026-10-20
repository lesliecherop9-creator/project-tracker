from models.base import Identified

TASK_STATUSES = ["pending", "done"]

class Task(Identified):
    def __init__(self, title, status="pending", assigned_to=None, task_id=None):
        # basic title check
        if not isinstance(title, str) or title.strip() == "":
            raise ValueError("Task title must be a non-empty string.")

        self.title = title.strip()
        self.status = status
        self.assigned_to = assigned_to  # this will be a user name or None

        self.id = self._allocate_id(task_id)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, value):
        if value not in TASK_STATUSES:
            raise ValueError("Status must be 'pending' or 'done'.")
        self._status = value

    def complete(self):
        self.status = "done"

    def is_done(self):
        return self.status == "done"

    def to_dict(self):
        # convert to a simple dict for saving to JSON
        return {
            "id": self.id,
            "title": self.title,
            "status": self.status,
            "assigned_to": self.assigned_to
        }

    @classmethod
    def from_dict(cls, data):
        # rebuild a Task from a dict
        return cls(
            title=data["title"],
            status=data.get("status", "pending"),
            assigned_to=data.get("assigned_to"),
            task_id=data.get("id")
        )

    def __str__(self):
        mark = "x" if self.status == "done" else " "
        assigned = f" (assigned to {self.assigned_to})" if self.assigned_to else ""
        return f"[{mark}] Task #{self.id}: {self.title}{assigned}"
