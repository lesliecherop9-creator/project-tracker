from models.user import User
from models.project import Project
from models.task import Task
from models.errors import TrackerError

class Tracker:
    def __init__(self):
        self.users = []

    def add_user(self, name, email=""):
        for u in self.users:
            if u.name == name:
                raise TrackerError("User name already exists.")
        new_user = User(name, email)
        self.users.append(new_user)
        return new_user

    def find_user(self, name):
        for u in self.users:
            if u.name == name:
                return u
        raise TrackerError("User not found.")

    def add_project(self, user_name, title, description="", due_date=None):
        user = self.find_user(user_name)

        for p in user.projects:
            if p.title == title:
                raise TrackerError("Project title already exists for this user.")

        proj = Project(title, description, due_date)
        user.add_project(proj)
        return proj

    def find_project(self, user_name, project_title):
        user = self.find_user(user_name)
        for p in user.projects:
            if p.title == project_title:
                return p
        raise TrackerError("Project not found.")

    def add_task(self, user_name, project_title, task_title):
        project = self.find_project(user_name, project_title)
        task = Task(task_title)
        project.add_task(task)
        return task

    def to_dict(self):
        # turn every user (with their projects and tasks) into plain dicts
        return {"users": [u.to_dict() for u in self.users]}

    @classmethod
    def from_dict(cls, data):
        # build a Tracker back from the dict we loaded from JSON
        tracker = cls()
        for user_data in data.get("users", []):
            tracker.users.append(User.from_dict(user_data))
        return tracker