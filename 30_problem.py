# Write a program to write a list of dictionaries (student data) into a JSON file.
import json
students = [
    {"name": "Rahul", "marks": 85},
    {"name": "Anita", "marks": 90},
    {"name": "Sachin", "marks": 88}
]
with open("students.json","w") as file:
    json.dump(students,file)

