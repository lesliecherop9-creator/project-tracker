import argparse
import sys

from models.errors import TrackerError, StorageError
from utils.storage import load_tracker, save_tracker


def make_parser():
    parser = argparse.ArgumentParser(description="Project tracker")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("add-user", help="add a new user")
    p.add_argument("name")
    p.add_argument("--email", default="")

    p = sub.add_parser("add-project", help="add a project to a user")
    p.add_argument("user")
    p.add_argument("title")
    p.add_argument("--description", default="")
    p.add_argument("--due", default=None)

    p = sub.add_parser("add-task", help="add a task to a project")
    p.add_argument("user")
    p.add_argument("project")
    p.add_argument("title")

    p = sub.add_parser("complete-task", help="mark a task as done")
    p.add_argument("user")
    p.add_argument("project")
    p.add_argument("task_id", type=int)

    p = sub.add_parser("list", help="show users, projects and tasks")
    p.add_argument("--user", default=None)

    return parser


def complete_task(tracker, user_name, project_title, task_id):
    project = tracker.find_project(user_name, project_title)
    for task in project.tasks:
        if task.id == task_id:
            task.complete()
            print(f"Completed {task}")
            return
    raise TrackerError("Task not found.")


def show_list(tracker, user_name):
    # show one user if a name was given, otherwise show everyone
    if user_name:
        users = [tracker.find_user(user_name)]
    else:
        users = tracker.users

    if len(users) == 0:
        print("No users yet.")

    for user in users:
        print(user)
        for project in user.projects:
            if project.due_date:
                print(f"  {project}, due {project.due_date.date()}")
            else:
                print(f"  {project}")
            for task in project.tasks:
                print(f"    {task}")


def main(argv=None):
    parser = make_parser()
    args = parser.parse_args(argv)

    try:
        tracker = load_tracker()

        if args.command == "add-user":
            user = tracker.add_user(args.name, args.email)
            print(f"Added {user}")
            save_tracker(tracker)

        elif args.command == "add-project":
            project = tracker.add_project(args.user, args.title, args.description, args.due)
            print(f"Added {project} for {args.user}")
            save_tracker(tracker)

        elif args.command == "add-task":
            task = tracker.add_task(args.user, args.project, args.title)
            print(f"Added {task}")
            save_tracker(tracker)

        elif args.command == "complete-task":
            complete_task(tracker, args.user, args.project, args.task_id)
            save_tracker(tracker)

        elif args.command == "list":
            show_list(tracker, args.user)

    except (TrackerError, StorageError, ValueError) as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()