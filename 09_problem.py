# Write a program that creates a new file and writes numbers from 1 to 100, each on a new line.
file=open("number.txt","x")
file2=open("number.txt","w")
for i in range(1,101):
    file2.write(str(i)+  "\n")
file2.close()