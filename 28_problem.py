'''Write a program that reads a text file and creates a dictionary where
keys = words
values = frequency of each word'''
with open("frequent.txt","r") as file:
    content=file.read().split()
    dic={}
for word in content:
    if word in dic:
        dic[word]+=1
    else:
        dic[word]=1
print(dic)