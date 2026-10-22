import pytest

from models.tracker import Tracker
from models.user import User
from models.errors import StorageError, TrackerError
from utils.storage import save_tracker, load_tracker


def make_tracker():
    tr = Tracker()
    tr.add_user("Alex", "alex@example.com")
    tr.add_project("Alex", "CLI Tool", "A tracker", "2026-12-01")
    tr.add_task("Alex", "CLI Tool", "Implement add-task")
    return tr


def test_storage_error_is_a_tracker_error():
    assert issubclass(StorageError, TrackerError)


def test_user_keeps_projects_after_round_trip():
    tr = make_tracker()
    user = User.from_dict(tr.find_user("Alex").to_dict())
    assert len(user.projects) == 1
    assert user.projects[0].tasks[0].title == "Implement add-task"


def test_tracker_round_trip():
    original = make_tracker()
    again = Tracker.from_dict(original.to_dict())
    assert again.to_dict() == original.to_dict()


def test_new_id_continues_after_loading():
    tr = Tracker.from_dict(make_tracker().to_dict())
    old_id = tr.find_project("Alex", "CLI Tool").id
    new_project = tr.add_project("Alex", "Second")
    assert new_project.id == old_id + 1


def test_save_and_load(tmp_path):
    path = str(tmp_path / "tracker.json")
    save_tracker(make_tracker(), path)
    loaded = load_tracker(path)
    assert loaded.find_user("Alex").email == "alex@example.com"
    assert loaded.find_project("Alex", "CLI Tool").tasks[0].title == "Implement add-task"


def test_load_missing_file_gives_empty_tracker(tmp_path):
    tr = load_tracker(str(tmp_path / "missing.json"))
    assert tr.users == []


def test_load_bad_json(tmp_path):
    path = tmp_path / "tracker.json"
    path.write_text("this is not json")
    with pytest.raises(StorageError):
        load_tracker(str(path))


def test_load_wrong_structure(tmp_path):
    path = tmp_path / "tracker.json"
    path.write_text('{"users": [{"email": "no name here"}]}')
    with pytest.raises(StorageError):
        load_tracker(str(path))


def test_find_project_not_found():
    tr = make_tracker()
    with pytest.raises(TrackerError):
        tr.find_project("Alex", "Nope")