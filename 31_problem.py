# Write a program to read a JSON file and display only students whose marks are greater than 80.
import json
with open("mark.json","r") as file:
    content=json.load(file)
for student in content:
    if student["marks"]>80:
        print(student)