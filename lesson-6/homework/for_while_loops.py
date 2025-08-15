#Lesson-6
#1. Modify String with Underscores
def insert_underscores(txt):
    vowels = "aeiouAEIOU"
    result = []
    count = 0  # count non-underscore characters processed

    i = 0
    while i < len(txt):
        result.append(txt[i])
        count += 1

        # Check if we've reached the 3rd character
        if count == 3:
            # Find next available spot that's not a vowel and doesn't already have an underscore after
            insert_pos = i + 1
            while insert_pos < len(txt) and (
                txt[insert_pos] in vowels or 
                (insert_pos < len(txt) and txt[insert_pos] == '_')
            ):
                result.append(txt[insert_pos])
                insert_pos += 1
                i += 1
                count += 1

            # Insert underscore if not at the very end
            if insert_pos < len(txt):
                result.append('_')
                count = 0  # reset counter after underscore
            else:


#2. Integer Squares Exercise
n = int(input('enter number '))

# here i have used range(n) which gives me the sequence of number starting fom 0 and ending before n
for i in range(n):
    print(i**2)

#3. Exercise 1: Print first 10 natural numbers using a while loop
number = 1 # start from the first natural number 
while number <= 10: # keep going until number is 10
    print(number)
    number += 1 # increase number by 10 each time 

#3. Exercise 2: Print the following pattern
rows = 5
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()  # move to the next line
    i += 1

# 3. Calculate sum of all numbers from 1 to a given number
number_3 = int(input('Enter number'))

total = 0

for num in range(1, number_3 + 1): # here to take the last element of the number_3, 1 is added.
    total += num
print(f'Sum is : {total}')

# 4. Print multiplication table of a given number
number = 2

for i in range(1, 11):
    print(number *i) # multiplies number itself

# 5. Display numbers from a list using a loop
numbers_6 = [12, 75, 150, 180, 145, 525, 50]

for i in numbers_6:
    if(i >= 500): 
        continue  # skip numbers 500 or more
    if (i > 150):
        continue  # skip numbers over 150
    if(i % 5 == 0):
        print(i)  # print if divisible by 5

# 6. Count the total number of digits in a number
number_6 = int(input('Enter number please: '))

digits_tuple = (0,1,2,3,4,5,6,7,8,9)

counter = 0

for d in str(number_6):                # loop over each digit as a string
    if int(d) in digits_tuple:         # convert to int and check in tuple
        counter += 1

print("Total digits:", counter)

# 7. Print reverse number pattern
rows = 5

for i in range(rows, 0, -1):        # i goes 5, 4, 3, 2, 1
    for j in range(i, 0, -1):       # j goes i down to 1
        print(j, end=" ")
    print()

# 8. Print list in reverse order using a loop
list1 = [10, 20, 30, 40, 50]

# for i in range(len(list1)-1,-1,-1):
#     print(list1[i])

for num in reversed(list1): # here reversed method used to start from the revevrse order
    print(num)

# 9. Display numbers from -10 to -1 using a for loop
for num in range(-10,0): # here it has been used range to start the numbers from -10 til -1
    print(num)

# 10. Display message “Done” after successful loop execution
for num in range(0,5): 
    print(num) # numbers between the range of 0 to 4 will be printed first
print('Done!') # shown after the loop finishes

# 11. Print all prime numbers within a range
start = 25
end = 50

print(f"Prime numbers between {start} and {end}:")

for num in range(start, end + 1):
    if num > 1:  # prime numbers are greater than 1
        for i in range(2, int(num ** 0.5) + 1):  # check up to square root of num
            if num % i == 0:
                break
        else:
            print(num)

# 12. Display Fibonacci series up to 10 terms
# Number of terms to display
terms = 10

# The first two numbers of the Fibonacci sequence
a, b = 0, 1

print("Fibonacci sequence:")

# Loop exactly 'terms' times
for _ in range(terms):
    print(a, end="  ")  # Print the current number, stay on the same line
    # Update values: 
    # new 'a' becomes old 'b'
    # new 'b' becomes sum of old 'a' and old 'b'
    a, b = b, a + b

# 13. Find the factorial of a given number
# Input: number for which we want to find the factorial
num = int(input('Enter number'))

# Initialize factorial result to 1 (since multiplying by 1 does not change the value)
factorial = 1

# Factorial is only defined for 0 and positive integers
if num < 0:
    print("Factorial does not exist for negative numbers.")
elif num == 0:
    print("0! = 1")
else:
    # Loop from 1 to num (inclusive)
    for i in range(1, num + 1):
        factorial *= i  # multiply factorial by current number
    print(f"{num}! = {factorial}")

# 4. Return Uncommon Elements of Lists
# Example input
list1 = [1, 1, 2, 3, 4, 2]
list2 = [1, 3, 4, 5]

# List comprehension to get elements unique to list1
unique_to_list1 = [x for x in list1 if x not in list2]

# List comprehension to get elements unique to list2
unique_to_list2 = [x for x in list2 if x not in list1]

# Combine the two results
uncommon_elements = unique_to_list1 + unique_to_list2

print(uncommon_elements)












