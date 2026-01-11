# Create a program that opens a file and replaces every occurrence of a specific word, like "old," with another word, like "new."
with open("replace.txt","r") as f:
    data=f.read()
data=data.replace("Old","new")
print(data)


    