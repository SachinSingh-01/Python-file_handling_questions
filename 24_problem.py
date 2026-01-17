# Write a program to ask the user for a filename and handle errors properly using try-except if the file does not exist.
user=input("Enter the file name:")
try:
    with open(user,"r") as file:
        content=file.read()
        print("File exist below is the file content\n")
        print(content)
except FileNotFoundError:
    print("File not found")