# Write a small utility that asks the user for a filename, then opens that file and displays its size in bytes.
import os

filename = input("Enter filename: ")
size = os.path.getsize(filename)
print("File size:", size, "bytes")
