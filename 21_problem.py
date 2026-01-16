'''Write a program to replace every occurrence of the word "Java" with "Python" in a file.'''
with open("replacees.txt","r") as file:
    content=file.read()
    content=content.replace("java","Python")
with open("replacees.txt","w") as file:
    file.write(content)