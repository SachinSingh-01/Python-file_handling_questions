# Write a program to write integers entered by the user into a file until the user enters -1.
with open("negative.txt","w") as f:
    while True:
        num=int(input("Enter the number:"))
        if num==-1:
            print("program terminated")
            break
        f.write(str(num)+ "\n")
print("All number saved to negative.txt")