# write a program that reads a file and creates a copy of that file but with all text converted to uppercase.
with open("example.txt", "r") as f1:
    data = f1.read()
    data=data.upper()
with open("copy.txt", "w") as f2:
    f2.write(data)
