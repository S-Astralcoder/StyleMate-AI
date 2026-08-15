
import json


def get_user_data():
    with open("database/user_information.json", "r") as file:
        content = json.loads(file.read())
        return content

def add_discovered_preference(title : str, info : str):
    with open("database/preference_collected.json", "a") as file:
        json.dump({"title" : title, "information" : info}, file, indent=4)
    return "added successfully"

def get_all_discovered_preferences():
    with open("database/preference_collected.json", "r") as file:
        content = json.loads(file.read())
        return content