
import json


def get_user_data():
    with open("database/user_information.json", "r") as file:
        content = json.loads(file.read())
        return content

def add_discovered_preference(title : str, info : str):
    with open("database/preference_collected.json", "a") as file:
        file.write(json.dumps({"title" : title, "information" : info}))
    return "added successfully"