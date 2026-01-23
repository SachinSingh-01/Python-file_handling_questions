# Write a program to read a file and create a new file containing only
# lines starting with a vowel.
with open("first.txt","r") as file:
    selected_line=[]
    content=file.readlines()
    for vowel in content:
        if vowel.lower().startswith(('a','e','i','o','u')):
            selected_line.append(vowel)
with open("only_vowel.txt","w") as file2:
    file2.writelines(selected_line)