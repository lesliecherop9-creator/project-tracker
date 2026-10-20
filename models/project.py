from models.base import Identified
from utils.validators import parse_date
from models.task import Task

class Project(Identified):
    def __init__(self, title, description="", due_date=None, project_id=None):
        if not isinstance(title, str) or title.strip() == "":
            raise ValueError("Project title must be a non-empty string.")

        self.title = title.strip()
        self.description = description.strip() if isinstance(description, str) else ""

        # parse the date if provided
        self.due_date = None
        if due_date:
            self.due_date = parse_date(due_date)

        self.tasks = []  # list of Task objects
        self.id = self._allocate_id(project_id)

    def add_task(self, task):
        self.tasks.append(task)

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "description": self.description,
            "due_date": self.due_date.isoformat() if self.due_date else None,
            "tasks": [t.to_dict() for t in self.tasks]
        }

    @classmethod
    def from_dict(cls, data):
        proj = cls(
            title=data["title"],
            description=data.get("description", ""),
            due_date=data.get("due_date"),
            project_id=data.get("id")
        )
        for t in data.get("tasks", []):
            proj.tasks.append(Task.from_dict(t))
        return proj

    def __str__(self):
        return f"Project #{self.id}: {self.title} ({len(self.tasks)} tasks)"
