# # Task 1: Read a File and Handle Errors 
# # Problem Statement:  Write a Python program that:
# # 1.   Opens and reads a text file named sample.txt.
# # 2.   Prints its content line by line.
# # 3.   Handles errors gracefully if the file does not exist.
import os

# file name with extension
file_name = os.path.basename('/Users/navdeepbhall/Desktop/python/assignment_4/sample.txt')

# file name without extension
name= (os.path.splitext(file_name)[0])

try:
    
    file1 = open('/Users/navdeepbhall/Desktop/python/assignment_4/sample1.txt', 'r')
    reading_line = file1.readlines()
    print("Reading file content:")
    for i, line in enumerate(reading_line):
        print("Line",i, ":", line.rstrip("\n"))
    file1.close()
# except NameError:
#     print("")
except FileNotFoundError:
    print(f"Error: The file {name}.txt was not found.")
    
    
