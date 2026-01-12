'''Write a program to read a text file and count
number of characters
number of words
number of lines'''
file=open("example.txt","r")
data=file.read()
word=len(data.split())
character=len(data)
line=len(data.split())
print("No. of word:",word)
print("No. of character:",character)
print("No. of line:",line)

