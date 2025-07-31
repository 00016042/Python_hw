#Lesson-1
import math

# 1. Square: Perimeter and Area
side = float(input("Enter the side length of the square: "))
square_perimeter = 4 * side
square_area = side ** 2
print(f"Square -> Perimeter: {square_perimeter}, Area: {square_area}")

# 2. Circle: Circumference from Diameter
diameter = float(input("\nEnter the diameter of the circle: "))
circle_circumference = math.pi * diameter
print(f"Circle -> Circumference (Length): {circle_circumference}")

# 3. Mean of Two Numbers
a = float(input("\nEnter first number (a): "))
b = float(input("Enter second number (b): "))
mean = (a + b) / 2
print(f"Mean of {a} and {b} is: {mean}")

# 4. Sum, Product, and Squares of Two Numbers
sum_ab = a + b
product_ab = a * b
a_squared = a ** 2
b_squared = b ** 2
print(f"\nSum: {sum_ab}, Product: {product_ab}")
print(f"Square of {a}: {a_squared}")
print(f"Square of {b}: {b_squared}")

