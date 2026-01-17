# Write a program to load all file content into a list and then write only the unique lines into a new file.
with open("first.txt","r") as file:
    content=file.readlines()
    unique=set(content)
with open("second.txt","w") as file2:
    file2.writelines(unique)