# Lesson 7

# 1. is_prime(n) function
# This function checks if a given number n is a prime number.
# Prime number = divisible only by 1 and itself.

def is_prime(n):
    if n <= 1:          # numbers <= 1 are not prime
        return False
    if n == 2:          # 2 is the only even prime number
        return True
    for i in range(2, int(n**0.5) + 1):   # check divisibility up to square root of n
        if n % i == 0:  # if divisible by any number, not prime
            return False
    return True          # otherwise, prime

# Example test:
n = int(input("Enter a number: "))
print(is_prime(n))


# 2. digit_sum(k) function
# This function calculates the sum of all digits of a number.

def digit_sum(k):
    total = 0
    for digit in str(k):    # convert number to string to iterate through digits
        total += int(digit) # convert back to int and add to total
    return total

# Example test:
k = int(input("Enter any number: "))
print(digit_sum(k))


# 3. power_of_n(n) function
# This function prints all powers of 2 that are less than or equal to n.

def power_of_n(n):
    power = 2
    while power <= n:
        print(power, end=" ")  # print numbers in one line separated by space
        power *= 2             # multiply by 2 to get next power

# Example test:
n = int(input("Enter number: "))
power_of_n(n)
