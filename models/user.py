from models.person import Person
from models.base import Identified

class User(Person, Identified):
    def __init__(self, name, email="", user_id=None):
        super().__init__(name, email)
        self.id = self._allocate_id(user_id)
        self.projects = []  # list of Project objects

    def add_project(self, project):
        self.projects.append(project)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "projects": [p.to_dict() for p in self.projects]
        }

    @classmethod
    def from_dict(cls, data):
        user = cls(
            name=data["name"],
            email=data.get("email", ""),
            user_id=data.get("id")
        )
        return user

    def __str__(self):
        return f"User #{self.id}: {self.name}"
