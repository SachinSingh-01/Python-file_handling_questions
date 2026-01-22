# Write a program that reads a file and creates another file where
# each word is replaced by its length.
with open("input.txt","r") as file:
    content=file.read().split()
length=[]
for word in content:
    length.append(str(len(word)))
with open("length.txt","w") as file1:
    file1.write("".join(length))