import pytest
from main import main
from utils.storage import load_tracker



def test_add_user_is_saved(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    main(["add-user", "Sam", "--email", "sam@example.com"])
    assert load_tracker().find_user("Sam").email == "sam@example.com"


def test_add_project_and_task_are_saved(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    main(["add-user", "Sam"])
    main(["add-project", "Sam", "CLI Tool", "--due", "2026-12-01"])
    main(["add-task", "Sam", "CLI Tool", "Write tests"])
    project = load_tracker().find_project("Sam", "CLI Tool")
    assert project.due_date.year == 2026
    assert project.tasks[0].title == "Write tests"


def test_complete_task(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    main(["add-user", "Sam"])
    main(["add-project", "Sam", "CLI Tool"])
    main(["add-task", "Sam", "CLI Tool", "Write tests"])
    task_id = load_tracker().find_project("Sam", "CLI Tool").tasks[0].id
    main(["complete-task", "Sam", "CLI Tool", str(task_id)])
    assert load_tracker().find_project("Sam", "CLI Tool").tasks[0].is_done()


def test_list_shows_everything(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    main(["add-user", "Sam"])
    main(["add-project", "Sam", "CLI Tool"])
    main(["add-task", "Sam", "CLI Tool", "Write tests"])
    capsys.readouterr()  # throw away the output from the lines above
    main(["list"])
    out = capsys.readouterr().out
    assert "Sam" in out
    assert "CLI Tool" in out
    assert "Write tests" in out


def test_list_with_no_data(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    main(["list"])
    assert "No users yet." in capsys.readouterr().out


def test_duplicate_user_gives_error(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    main(["add-user", "Sam"])
    with pytest.raises(SystemExit):
        main(["add-user", "Sam"])
    assert "Error: User name already exists." in capsys.readouterr().out


def test_unknown_user_gives_error(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    with pytest.raises(SystemExit):
        main(["add-project", "Nobody", "Anything"])
    assert "Error: User not found." in capsys.readouterr().out


def test_bad_date_gives_error(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    main(["add-user", "Sam"])
    with pytest.raises(SystemExit):
        main(["add-project", "Sam", "CLI Tool", "--due", "not a date"])
    assert "Error: Date format not understood." in capsys.readouterr().out


def test_complete_missing_task_gives_error(tmp_path, monkeypatch, capsys):
    monkeypatch.chdir(tmp_path)
    main(["add-user", "Sam"])
    main(["add-project", "Sam", "CLI Tool"])
    with pytest.raises(SystemExit):
        main(["complete-task", "Sam", "CLI Tool", "999"])
    assert "Error: Task not found." in capsys.readouterr().out