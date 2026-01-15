# Write a program that reads a file and prints the longest word present in the file.
with open("longest.txt","r") as file:
    content=file.read()
    word=content.split()
    longest=""
    for w in word:
        if len(w)>len(longest):
            longest=w
    print("Longest word:",longest)
