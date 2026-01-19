# Write a program to compare two files and print whether their content is exactly the same or not.
with open("copy.txt","r") as file:
    content1=file.read()
with open("count.txt","r") as file:
    content2=file.read()
if content1==content2:
    print("Yes both file are same")
else:
    print("No both file are not same")
    