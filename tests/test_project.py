from models.project import Project
from models.task import Task
import pytest

def test_project_creation():
    p = Project("My Project")
    assert p.title == "My Project"
    assert p.description == ""

def test_project_add_task():
    p = Project("My Project")
    t = Task("Do something")
    p.add_task(t)
    assert len(p.tasks) == 1
    assert p.tasks[0].title == "Do something"

def test_project_invalid_title():
    with pytest.raises(ValueError):
        Project("")
