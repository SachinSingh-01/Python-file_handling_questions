# Write a program that removes all spaces from a file and saves the result into another file.
with open("copy.txt","r") as file:
    content=file.read()
    content=content.replace(" ","")
with open("without_space.txt","w") as file:
    file.write(content)