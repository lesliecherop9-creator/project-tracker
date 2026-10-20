from models.tracker import Tracker
from models.errors import TrackerError

def test_add_user():
    tr = Tracker()
    u = tr.add_user("Alex")
    assert u.name == "Alex"
    assert len(tr.users) == 1

def test_add_duplicate_user():
    tr = Tracker()
    tr.add_user("Alex")
    try:
        tr.add_user("Alex")
        assert False  # should not reach here
    except TrackerError:
        assert True

def test_add_project():
    tr = Tracker()
    tr.add_user("Alex")
    p = tr.add_project("Alex", "Proj1")
    assert p.title == "Proj1"

def test_add_task():
    tr = Tracker()
    tr.add_user("Alex")
    tr.add_project("Alex", "Proj1")
    t = tr.add_task("Alex", "Proj1", "Task1")
    assert t.title == "Task1"
