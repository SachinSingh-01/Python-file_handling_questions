# Write a program to reverse the content of a file and save it into another file.
with open("replace.txt","r") as file:
    content=file.read()
    content=content[::-1]
    # print(content)
with open("reverse.txt","w") as file:
    file.write(content)