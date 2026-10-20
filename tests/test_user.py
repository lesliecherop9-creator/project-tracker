from models.user import User
from models.project import Project

def test_user_creation():
    u = User("Alex", "alex@example.com")
    assert u.name == "Alex"
    assert u.email == "alex@example.com"

def test_user_add_project():
    u = User("Alex")
    p = Project("Proj1")
    u.add_project(p)
    assert len(u.projects) == 1
    assert u.projects[0].title == "Proj1"
