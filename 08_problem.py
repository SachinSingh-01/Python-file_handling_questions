# Write a program that reads a file character by character and counts how many times the letter 'e' appears.
with open ("count.txt","r") as f:
    count=0
    data=f.read()
    for ch in data:
        if ch=="e": 
            count+=1
print("No. of e present in count.txt:",count)
