# Write a program to remove duplicate words from a file and save the cleaned text into another file.
with open("input.txt","r") as file:
    dup=file.read().split()
    success=set(dup)
with open("duplicate.txt","w") as file2:
    file2.write("".join(success))