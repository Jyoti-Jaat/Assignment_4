import os


# file name with extension
file_name = os.path.basename('/Users/navdeepbhall/Desktop/python/assignment_4/output.txt')

# file name without extension
# print(os.path.splitext(file_name)[0])


file1 = open('/Users/navdeepbhall/Desktop/python/assignment_4/output.txt', 'w')
text1 = input("Enter text to write to the file:")
write_text = file1.write(text1+"\n")
file1.close()
print("Data successfully written to", (os.path.splitext(file_name)[0]),".txt")


file2 = open('/Users/navdeepbhall/Desktop/python/assignment_4/output.txt','a')
text2 = input("Enter additional text to append:")
file2.write(text2 +"\n")
file2.close()
print("Data successfully appended.")

    
    

file1 = open('/Users/navdeepbhall/Desktop/python/assignment_4/output.txt','r')
print("\nFinal content of the file:\n")
reading_file = file1.read()
  
print(reading_file)
    

file1.close()
