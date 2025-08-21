# lesson - 8

# 1. Handle ZeroDivisionError when dividing a number by zero
try:
    a = int(input("Enter any number: "))
    b = int(input("Enter any number: "))

    result = a / b   # use division instead of modulus for clarity
    print("Result:", result)
except ZeroDivisionError:
    print("Error: Number cannot be divided by zero!")

# 2. Handle ValueError if input is not a valid integer
try: 
    number = int(input("Enter an integer: "))
    print("Number is:", number)
except ValueError:
    print("Error: Please enter a valid integer!")

# 3. Handle FileNotFoundError if the file does not exist
try:
    filename = input("Enter file name: ")
    with open(filename, "r") as file:
        content = file.read()
        print("Content:\n", content)
except FileNotFoundError:
    print("Error: No such file found!")

# 4. Raise TypeError if inputs are not numerical
try:
    num1 = input("Enter first number: ")
    num2 = input("Enter second number: ")

    # Validate input manually
    if not (num1.isdigit() and num2.isdigit()):
        raise TypeError("Inputs must be numbers!")

    # Convert to integers
    num1 = int(num1)
    num2 = int(num2)

    print(f"Number1 is: {num1}, Number2 is: {num2}")

except TypeError as e:
    print("Error:", e)

# 5. Handle PermissionError if access to file is restricted
try: 
    filename = input("Enter file name: ")
    with open(filename, "r") as file:
        content = file.read()
        print("Content:\n", content)
except PermissionError:
    print("Error: You do not have permission to access this file!")

# 6. Write a Python program that executes an operation on a list and handles an IndexError 
# exception if the index is out of range.
# Sample list
numbers = [10,20,30,40,50,60]

try:
    index = int(input("Enter the index of the element you want to access: "))
    
    value = numbers[index] # Here i have accessed to the numbers list and found each element's index. 
    print(f'The number with the index of {index} is {value} ')
    print(f'Square of the element is {value **2}')

except IndexError: # Handles if IndexError happens
    print('Error: Index is out of range!')
except ValueError: # Handles if ValueError happens
    print('Error: Please enter a valid integer index.')

# 7. Write a Python program that prompts the user to input a number and handles a 
# KeyboardInterrupt exception if the user cancels the input.
try: 
    passcode = int(input('Enter the passcode: '))
    print(f'the passcode you entered is: {passcode}')
except KeyboardInterrupt:
    print('passcode has been canceled by the user')
except ValueError:
    print("Please enter a valid integer.")

# 8. Write a Python program that executes division and handles an ArithmeticError exception 
# if there is an arithmetic error.
number_1 = int(input('Enter numerator'))

number_2 = int(input('Enter denomenator'))

try: 
    print(number_1 / number_2)
except ValueError:
    print('Error: Please enter valid numbers!')
except ArithmeticError:
    print('Error: ArithmeticError occured')

# 9. Write a Python program that opens a file and handles a UnicodeDecodeError exception 
# if there is an encoding issue.
try:
    # Ask the user for a file name
    filename = input("Enter the name of the file: ")

    # Try opening the file with default encoding (UTF-8)
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
        print("File content:\n", content)

# Handle encoding problems
except UnicodeDecodeError:
    print("Error: Could not decode the file content. Please check the file encoding.")

# Handle missing file case
except FileNotFoundError:
    print("Error: The file does not exist. Please check the filename and try again.")

# Handle permission issues
except PermissionError:
    print("Error: You do not have permission to access this file.")

# 10. Write a Python program that executes a list operation and handles an AttributeError
#  exception if the attribute does not exist.
# Example list
fruits = ["apple", "banana", "cherry"]

try:
    # Try to call a method that does NOT exist for lists
    fruits.upper()   # lists don’t have an 'upper' method → AttributeError
except AttributeError:
    print("Error: That attribute or method does not exist for lists.")

# Python File Input Output: Exercises, Practice, Solution
# 1. Write a Python program to read an entire text file.
filename = input('Enter file name: ')

try:
    with open(filename, 'r') as file:
        content = file.read()
        print('content of the file\n', content)
except FileNotFoundError:
    print('Error: there is no such a file')
except PermissionError:
    print('Error: No permisson to access to this file ')
except OSError:
    print('Error:enter valid file path please')

# 2. Write a Python program to read first n lines of a file.

filename = input('Enter filename:')
n = int(input('Enter number of lines to read:'))

try:
    with open(filename,'r') as file:
        for i in range(n):
            line = file.readline()
            if not line: 
                break
            print(line, end="")
except FileNotFoundError:
    print('Error: Ther is not such a file')

# 3.Write a Python program to append text to a file and display the text.
filename = input("Enter file name: ")
text_to_append = input("Enter text to append: ")

# Open file in append mode
with open(filename, "a") as file:
    file.write(text_to_append + "\n")

# Display file content after appending
with open(filename, "r") as file:
    content = file.read()
    print("Updated file content:\n", content)

# 4. Write a Python program to read last n lines of a file.
filename = input("Enter file name: ")
text_to_append = input("Enter text to append: ")

# Open file in append mode
with open(filename, "a", encoding="utf-8") as file:
    file.write(text_to_append + "\n")

# Display file content after appending
with open(filename, "r", encoding="utf-8") as file:
    content = file.read()
    print("Updated file content:\n", content)

# 5. Write a Python program to read a file line by line and store it into a list.
filename = input("Enter file name: ")

lines = []   # empty list to store lines

with open(filename, "r", encoding="utf-8") as file:
    for line in file:                 # read file line by line
        lines.append(line.strip())    # remove \n and add to list

print("File content as list:")
print(lines)

# 6. Write a Python program to read a file line by line and store it into a variable.
filename = input("Enter file name: ")

with open(filename, "r", encoding="utf-8") as file:
    content = file.readlines()   # stores all lines in a list

print("File content stored in variable (list):")
print(content)

# 7. Write a Python program to read a file line by line and store it into an array.
filename = input("Enter file name: ")

# Initialize empty list (array)
lines_array = []

with open(filename, "r", encoding="utf-8") as file:
    for line in file:
        lines_array.append(line.strip())  # strip removes \n

print("File content stored in array (list):")
print(lines_array)

#8. Write a Python program to find the longest words.
filename = input("Enter file name: ")

with open(filename, "r", encoding="utf-8") as file:
    words = file.read().split()   # split file content into words

# Find the maximum word length
max_len = max(len(word) for word in words)

# Get all words that have this length
longest_words = [word for word in words if len(word) == max_len]

print("Longest word(s):", longest_words)
print("Length:", max_len)

# 9. Write a Python program to count the number of lines in a text file.
filename = input("Enter file name: ")

with open(filename, "r", encoding="utf-8") as file:
    line_count = sum(1 for line in file)

print("Number of lines in the file:", line_count)

# 10.Write a Python program to count the frequency of words in a file. 
from collections import Counter

filename = input("Enter file name: ")

with open(filename, "r", encoding="utf-8") as file:
    text = file.read().lower()  # read all and make lowercase

# Split text into words (basic split on whitespace)
words = text.split()

# Count word frequencies
word_count = Counter(words)

# Display result
print("Word Frequencies:")
for word, count in word_count.items():
    print(f"{word}: {count}")

# 11. Write a Python program to get the file size of a plain file.
import os

filename = input("Enter file name: ")

# Get file size in bytes
file_size = os.path.getsize(filename)

print(f"File size: {file_size} bytes")

# 12. Write a Python program to write a list to a file.
# Sample list
my_list = ["Apple", "Banana", "Cherry", "Mango"]

filename = input("Enter file name: ")

# Open file in write mode
with open(filename, "w", encoding="utf-8") as file:
    for item in my_list:
        file.write(item + "\n")   # each item on a new line

print("List has been written to the file successfully!")

# 13. Write a Python program to copy the contents of a file to another file.
# Ask user for source and destination file names
source_file = input("Enter the source file name: ")
destination_file = input("Enter the destination file name: ")

try:
    # Open the source file in read mode
    with open(source_file, "r", encoding="utf-8") as src:
        content = src.read()

    # Open the destination file in write mode and copy contents
    with open(destination_file, "w", encoding="utf-8") as dest:
        dest.write(content)

    print(f"Contents of '{source_file}' copied to '{destination_file}' successfully!")

except FileNotFoundError:
    print("Error: The source file does not exist.")
except Exception as e:
    print("An error occurred:", e)

# 14. Write a Python program to combine each line from the first file with the corresponding line in the second file.
# Ask user for two file names and output file name
file1 = input("Enter the first file name: ")
file2 = input("Enter the second file name: ")
output_file = input("Enter the output file name: ")

try:
    with open(file1, "r", encoding="utf-8") as f1, open(file2, "r", encoding="utf-8") as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    # Combine corresponding lines
    combined_lines = [line1.strip() + " " + line2 for line1, line2 in zip(lines1, lines2)]

    # Write to output file
    with open(output_file, "w", encoding="utf-8") as out:
        out.write("\n".join(combined_lines))

    print(f"Combined lines written to '{output_file}' successfully!")

except FileNotFoundError:

# 15. Write a Python program to read a random line from a file.
import random

filename = input("Enter the file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        lines = file.readlines()

    if lines:  # check if file is not empty
        random_line = random.choice(lines).strip()
        print("Random line:", random_line)
    else:
        print("The file is empty.")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# 16. Write a Python program to assess if a file is closed or not.
filename = input("Enter the file name: ")

try:
    # Open the file
    file = open(filename, "r", encoding="utf-8")
    print("File opened.")
    print("Is the file closed?", file.closed)

    # Close the file
    file.close()
    print("File closed.")
    print("Is the file closed now?", file.closed)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# 17. Write a Python program to remove newline characters from a file.
filename = input("Enter the file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        # Read all lines and strip newline characters
        lines = [line.strip() for line in file]

    print("File content without newline characters:")
    print(" ".join(lines))   # joins all lines with space

    # (Optional) Write back to another file
    with open("cleaned_" + filename, "w", encoding="utf-8") as outfile:
        outfile.write(" ".join(lines))

    print(f"\nCleaned file saved as cleaned_{filename}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# 18. Write a Python program that takes a text file as input and returns the number of words in a given text file.
import re

filename = input("Enter the file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()
        # Find all words (sequence of letters/numbers), ignoring punctuation
        words = re.findall(r"\b\w+\b", text)
        word_count = len(words)

    print(f"The number of words in '{filename}' is: {word_count}")

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# 19. Write a Python program to extract characters from various text files and put them into a list.
filename = input("Enter the file name: ")

try:
    with open(filename, "r", encoding="utf-8") as file:
        text = file.read()        # read the entire file
        char_list = list(text)    # convert string into a list of characters

    print("Characters in the file:")
    print(char_list)

except FileNotFoundError:
    print("Error: File not found.")
except Exception as e:
    print("An error occurred:", e)

# 20.Write a Python program to generate 26 text files named A.txt, B.txt, and so on up to Z.txt.
import string

# Loop through all uppercase letters
for letter in string.ascii_uppercase:  # 'A' to 'Z'
    filename = f"{letter}.txt"
    with open(filename, "w", encoding="utf-8") as file:
        file.write(f"This is file {filename}\n")  # optional content

print("26 text files (A.txt to Z.txt) created successfully!")

# 21. Write a Python program to create a file where all letters of the English alphabet are listed with a specified number of letters on each line.
import string

filename = input("Enter the output file name: ")
letters_per_line = int(input("Enter the number of letters per line: "))

alphabet = string.ascii_uppercase  # 'A' to 'Z'

with open(filename, "w", encoding="utf-8") as file:
    for i in range(0, len(alphabet), letters_per_line):
        line = alphabet[i:i+letters_per_line]  # slice letters
        file.write(line + "\n")                # write line to file

print(f"File '{filename}' created successfully!")




