#Lesson-5

def is_leap_year(year: int) -> bool:
    """
    A year is a leap year if:
    - It is divisible by 4, and
    - It is NOT divisible by 100, unless it is also divisible by 400.

    Parameters:
    year (int): The year to be checked.

    Returns:
    bool: True if the year is a leap year, False otherwise.
    """
    if not isinstance(year, int):
        raise ValueError("Year must be an integer.")

    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)


# Example usage:
print(is_leap_year(2024))  # True
print(is_leap_year(1900))  # False
print(is_leap_year(2000))  # True

#2. Given an integer, n, perform the following conditional actions:

# If n is odd, print Weird
# If n is even and in the inclusive range of 2 to 5, print Not Weird
# If n is even and in the inclusive range of 6 to 20, print Weird
# If n is even and greater than 20, print Not Weird

n = int(input('Enter number : '))

if(n % 2 != 0):
    print('Weird')
elif(2 <= n <= 5):
    print('Not Weird')
elif(6 <= n <= 20):
    print('Weird')
else:
    print('Not Weird')

# 3. Given two integer numbers a and b. Find even numbers between this numbers. a and b are inclusive. Don't use loop.
# Give two solutions.
a = 10

b = 20

# Solution 1 with if-else statement:
a = 10
b = 20

# Make 'a' even
if a % 2 != 0:
    a += 1

# Make 'b' even
if b % 2 != 0:
    b -= 1

# Print all evens between a and b
print(list(range(a, b + 1, 2)))

# Solution 2 without if-else statement:
a = 10
b = 20

# Start from the next even number if a is odd
print(list(range(a + a % 2, b + 1, 2)))




