from models.task import Task
import pytest

def test_task_creation():
    t = Task("Write code")
    assert t.title == "Write code"
    assert t.status == "pending"

def test_task_complete():
    t = Task("Write code")
    t.complete()
    assert t.status == "done"

def test_task_invalid_title():
    with pytest.raises(ValueError):
        Task("")

def test_task_invalid_status():
    with pytest.raises(ValueError):
        Task("Test", status="unknown")
