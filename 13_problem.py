# Write a program to read all numbers from a file and find their sum.
file=open("sum.txt","r")
add=0
data=file.read().split()
for d in data:
    add+=int(d)
print("Total sum:",add)