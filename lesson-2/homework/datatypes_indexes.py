# Lesson - 2

# 1) Age Calculator
# Ask for user's name and year of birth, then calculate and display their age.
from datetime import date

name = input("1) Enter your name: ")
birth_year = int(input("   Enter your birth year (e.g., 2005): "))
current_year = date.today().year  # get current year automatically
age = current_year - birth_year
print(f"   Hello {name}, you are {age} years old.\n")

# 2) Extract Car Names (from txt = 'LMaasleitbtui')
# Use slicing with step: even indices (0::2) and odd indices (1::2)
txt2 = 'LMaasleitbtui'
car_even = txt2[0::2]  # take 0,2,4,...  -> expected to read like 'Lacetti' (string-specific)
car_odd  = txt2[1::2]  # take 1,3,5,...  -> 'Malibu'
print("2) From txt = 'LMaasleitbtui'")
print("   Even slice (0::2):", car_even)  # simple slicing
print("   Odd  slice (1::2):", car_odd, "\n")

# 3) Extract Car Names (from txt = 'MsaatmiazD')
# Even slice gives 'Matiz'; odd slice gives 'samaD' -> reverse to get 'Damas'
txt3 = 'MsaatmiazD'
car_even2 = txt3[0::2]          # 'Matiz'
car_odd2  = txt3[1::2][::-1]    # reverse to get 'Damas'
print("3) From txt = 'MsaatmiazD'")
print("   Even slice (0::2):", car_even2)   # Matiz
print("   Odd  slice (1::2) reversed:", car_odd2, "\n")  # Damas

# 4) Extract Residence Area
# Extract the area after the word "from" in the sentence.
txt4 = "I'am John. I am from London"
# Split on 'from ' and take the last part, then strip spaces
area = txt4.split("from")[-1].strip()
print("4) Residence Area:", area, "\n")

# 5) Reverse String
# Take a user input string and print it reversed using slicing [::-1]
s = input("5) Enter a string to reverse: ")
print("   Reversed:", s[::-1], "\n")

# 6) Count Vowels
# Count vowels in a given string using a simple membership check
vowel_text = input("6) Enter text to count vowels: ")
vowels = "aeiouAEIOU"
vowel_count = sum(1 for ch in vowel_text if ch in vowels)
print("   Number of vowels:", vowel_count, "\n")

# 7) Find Maximum Value
# Read numbers separated by space and print the maximum
nums = list(map(int, input("7) Enter numbers separated by space: ").split()))
print("   Maximum value:", max(nums), "\n")

# 8) Check Palindrome
# A word is a palindrome if it equals its reverse
w = input("8) Enter a word to check palindrome: ")
print("   Palindrome" if w == w[::-1] else "   Not a palindrome", "\n")

# 9) Extract Email Domain
# Split at '@' and take the part after it
email = input("9) Enter your email: ")
domain = email.split("@")[-1]
print("   Domain:", domain, "\n")

# 10) Generate Random Password
# Build a password from letters, digits, and punctuation
import random
import string

length = int(input("10) Enter desired password length (e.g., 12): "))
chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))
print("   Generated password:", password)

