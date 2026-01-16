# Write a program to store 5 student names and marks in a file, then read the file and display only students who scored above 70.
with open("student_detail.txt","r") as file:
    for line in file:
        name,marks=line.split()
        marks=int(marks)
        if marks>70:
            print(name, marks)
