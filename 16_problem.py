# Write a program to search for a word in a file and print how many times it appears.
with open("word.txt","r") as file:
    word=file.read()
write=input("Enter the words here:")
count=word.count(write)
if count>0:
    print("Yes it present")
    print("Word appear:",count)
else:
    print("Not present")