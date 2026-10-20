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

    def add_task(self, user_name, project_title, task_title):
        user = self.find_user(user_name)

        project = None
        for p in user.projects:
            if p.title == project_title:
                project = p
                break

        if project is None:
            raise TrackerError("Project not found.")

        task = Task(task_title)
        project.add_task(task)
        return task
