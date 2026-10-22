import json
import os
from models.tracker import Tracker
from models.errors import StorageError

def save_tracker(tracker, filename="project_data.json"):
    """Saves the Tracker instance to a JSON file."""
    try:
        data = tracker.to_dict() if hasattr(tracker, "to_dict") else tracker
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except Exception as e:
        if isinstance(e, StorageError):
            raise e
        raise StorageError(f"Error saving tracker: {e}")

def load_tracker(filename="project_data.json"):
    """Loads tracker data from a JSON file and returns a Tracker instance."""
    if not os.path.exists(filename):
        return Tracker()
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        raise StorageError(f"Invalid JSON format: {e}")
    except Exception as e:
        raise StorageError(f"Error reading file: {e}")
        
    if not isinstance(data, dict):
        raise StorageError("Invalid data structure: Root must be a dictionary.")
        
    if "users" in data:
        for user in data["users"]:
            if not isinstance(user, dict) or "name" not in user:
                raise StorageError("Invalid user structure: missing 'name'.")

    tracker = Tracker()
    if hasattr(tracker, "from_dict"):
        tracker = Tracker.from_dict(data)
    else:
        if hasattr(tracker, "users") and "users" in data:
            tracker.users = data["users"]
            
    return tracker