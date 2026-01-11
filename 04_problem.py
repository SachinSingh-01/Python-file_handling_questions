# Make a program that counts the number of lines in a file.
file=open("count.txt","r")
data=len(file.readlines())
print("No. of line present in count.txt:",data)