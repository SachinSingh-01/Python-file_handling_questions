# Write a program to copy only even numbers from one file into another file.
with open("number.txt","r") as f:
    data=f.read().split()
even_number=[]
for n in data:
    if int(n)%2==0:
        even_number.append(n)
with open("even.txt","w") as e:
        e.write(" ".join(even_number))
print("successful")
