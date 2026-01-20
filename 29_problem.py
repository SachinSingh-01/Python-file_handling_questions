'''Write a program to read a CSV file of student marks and calculate
average marks
highest marks
lowest marks'''
with open("student.csv","r") as file:
    content=file.read().split()
marks=list(map(int,content))
print(f"Highest marks={max(marks)}")
print(f"Lowest marks={min(marks)}")
print(f"Average marks={sum(marks)/len(marks)}")