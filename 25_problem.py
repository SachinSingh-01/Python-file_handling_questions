# Write a program to read a file and extract all mobile numbers (10-digit) and store them in another file.
with open("phone_number.txt","r") as file:
    content=file.read()
number=content.split()
valid_number=[]
for word in number:
    if word.isdigit() and len(word)==10:
        valid_number.append(word)
with open("correct_phone.txt","w") as file2:
    for num in valid_number:
        file2.write(num + "\n")