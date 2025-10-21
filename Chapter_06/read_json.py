import os
import json


def read_json_file(filename):
    """Reads and returns JSON data from a file."""
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            data = json.load(file)
            return data
    except FileNotFoundError:
        print(f"Error: File '{filename}' not found.")
    except json.JSONDecodeError as e:
        print(f"Error reading JSON: {e}")


def get_all_names(data):
    """Extracts and returns all user names from the JSON data."""
    names = []
    try:
        users = data.get("users", [])
        for user in users:
            if "name" in user:
                names.append(user["name"])
    except AttributeError:  # occurs when you attempt to access a method or attribute that isn't defined for the object in question
        print("Error: Invalid JSON structure.")
    return names


def add_user_to_json(filename, new_user):
    """Adds a new user to the JSON file and saves the update."""
    data = read_json_file(filename)
    if not data:
        print("Error: No data found in JSON file.")
        return

    # Ensure 'users' key exists
    if "users" not in data:
        data["users"] = []

    # Add the new user
    data["users"].append(new_user)

    # Write back to file
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4)
        print(f"\nNew user '{new_user['name']}' added successfully!")
    except Exception as e:
        print(f"Error writing to file: {e}")


if __name__ == "__main__":
    filename = "Chapter_06/data.json"
    data = read_json_file(filename)
    if data:
        print("JSON data loaded successfully:\n")
        print(json.dumps(data, indent=4))

        # Print all names
        names = get_all_names(data)
        print("\nList of all user names:")
        for name in names:
            print("-", name)

        # Add new user Rainer
        new_user = {
            "id": 4,
            "name": "Rainer",
            "email": "rainer@example.com",
            "active": True
        }

        add_user_to_json(filename, new_user)
