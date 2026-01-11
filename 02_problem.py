# Create a program that reads the contents of a file named "input.txt" and prints each line to the console.
file=open("input.txt","r")
data=file.read()
print("Data:",data)