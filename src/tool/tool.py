
import json


def get_user_data():
    with open("database/user_information.json", "r") as file:
        content = json.loads(file.read())
        return content

def add_discovered_preference(title : str, info : str):
    with open("database/preference_collected.json", "r") as file:
        content_list = json.loads(file.read())
    content_list.append({"title" : title, "information" : info})
    with open("database/preference_collected.json", "w") as file:
        json.dump(content_list, file, indent=4)
    return "added successfully"

def get_all_discovered_preferences():
    with open("database/preference_collected.json", "r") as file:
        content = json.loads(file.read())
        return content

def update_memory(content : str):
    with open("database/agent_memory_summary.txt", "w", encoding="utf-8") as file:
        file.write(content)
    return "Updated memory"
    
def view_memory():
    with open("database/agent_memory_summary.txt", "r", encoding="utf-8") as file:
        return file.read()