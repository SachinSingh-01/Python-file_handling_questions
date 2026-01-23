# Write a program to Write a program to shuffle the lines of a file randomly and save into a new file. the lines of a file randomly and save into a new file.
import random
with open("first.txt","r") as file:
    content=file.readlines()
    random.shuffle(content)
with open("shuffle.txt","w") as file2:
    file2.writelines(content)

    