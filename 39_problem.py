# Write a program to monitor a file and print a message whenever the file content changes (hint: store previous state).
import time
def monitor_file(filename):
    with open(filename, "r") as file:
        old_data = file.read()
    while True:
        with open(filename, "r") as file:
            new_data = file.read()
        if new_data != old_data:
            print("Something has changed")
            old_data = new_data   
        time.sleep(1)   
monitor_file("monitor.txt")
