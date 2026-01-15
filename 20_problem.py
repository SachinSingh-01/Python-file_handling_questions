# Write a program to merge the contents of two files into a third file.
with open("student.txt", "r") as file1:
    content1=file1.read()
with open("replace.txt","r") as file2:
    content2=file2.read()
    merge=content1+content2
with open("merge.txt","w") as file3:
    file3.write(merge)