'''Build a file-based To-Do app
Add task
View tasks
Delete task
Data must persist using a text or JSON file'''
import json
import os
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as file:
        tasks = json.load(file)
else:
    tasks = []
