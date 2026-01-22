# Write a program to scan a folder and print total number of files total number of folders
import os
path=input("Enter folder path")
file_count = 0
folder_count = 0
for item in os.listdir(path):
    full_path = os.path.join(path, item)
    if os.path.isfile(full_path):
        file_count += 1
    elif os.path.isdir(full_path):
        folder_count += 1
print("Files:", file_count)
print("Folders:", folder_count)