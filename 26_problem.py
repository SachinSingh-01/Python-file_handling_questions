# Write a program to read a file and find the top 5 most frequent words.
from collections import Counter
with open("more_word.txt","r") as file:
    content=file.read()
words=content.lower().split()
word_count=Counter(words)
frequent_words=word_count.most_common(5)
for word,count in frequent_words:
    if count>1:
        print(word,"-",count)

