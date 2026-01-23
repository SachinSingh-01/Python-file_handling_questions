'''Write a program to build a simple password-protected file locker:
Ask for password
If correct, allow reading file
If wrong, deny access.'''
your_password="Sachinss1@"
password=input("Enter your password:")
if password==your_password:
    with open("duplicate.txt","r") as file:
        content=file.read()
        print(content)
else:
    print("Sorry incorrect password try again")

# _________________________X___________________________________

# Advance method
import getpass

your_password = "Sachinss1@"
max_attempts = 3

for attempt in range(max_attempts):
    password = getpass.getpass("Enter your password: ")

    if password == your_password:
        print("\nAccess granted.\n")
        try:
            with open("duplicate.txt", "r") as file:
                content = file.read()
                print(content)
        except FileNotFoundError:
            print("File not found.")
        break
    else:
        print("Wrong password.\n")

else:
    print("Too many wrong attempts. Access denied.")
