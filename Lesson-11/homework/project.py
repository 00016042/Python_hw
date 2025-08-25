# Lesson-11
# ==============================
# Homework: Custom Modules & Packages in One File
# ==============================

# ------------------------------
# math_operations.py (Module)
# ------------------------------

def add(a, b):
    # Function to add two numbers
    return a + b

def subtract(a, b):
    # Function to subtract b from a
    return a - b

def multiply(a, b):
    # Function to multiply two numbers
    return a * b

def divide(a, b):
    # Function to divide a by b (with zero check)
    if b == 0:
        return "Error: Division by zero is not allowed"
    return a / b


# ------------------------------
# string_utils.py (Module)
# ------------------------------

def reverse_string(s):
    # Function to reverse a string
    return s[::-1]

def count_vowels(s):
    # Function to count vowels in a string
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)


# ------------------------------
# geometry/circle.py (Package)
# ------------------------------

def calculate_area(radius):
    # Function to calculate area of a circle (πr²)
    pi = 3.14159
    return pi * (radius ** 2)

def calculate_circumference(radius):
    # Function to calculate circumference of a circle (2πr)
    pi = 3.14159
    return 2 * pi * radius


# ------------------------------
# file_operations/file_reader.py (Package)
# ------------------------------

def read_file(file_path):
    # Function to read the content of a file
    try:
        with open(file_path, 'r') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: File not found"


# ------------------------------
# file_operations/file_writer.py (Package)
# ------------------------------

def write_file(file_path, content):
    # Function to write content into a file
    try:
        with open(file_path, 'w') as f:
            f.write(content)
        return "File written successfully!"
    except Exception as e:
        return f"Error writing file: {e}"


# ==============================
# MAIN PROGRAM (Testing all modules/packages)
# ==============================

if __name__ == "__main__":

    # ---- Testing math_operations ----
    print("Math Operations:")
    print("Add:", add(10, 5))
    print("Subtract:", subtract(10, 5))
    print("Multiply:", multiply(10, 5))
    print("Divide:", divide(10, 5))
    print("Divide by zero:", divide(10, 0))
    print()

    # ---- Testing string_utils ----
    print("String Utilities:")
    print("Reverse String:", reverse_string("Hello"))
    print("Count Vowels:", count_vowels("OpenAI"))
    print()

    # ---- Testing geometry (circle) ----
    print("Geometry - Circle:")
    print("Area of circle with radius 5:", calculate_area(5))
    print("Circumference of circle with radius 5:", calculate_circumference(5))
    print()

    # ---- Testing file_operations ----
    print("File Operations:")
    # Writing to a file
    result = write_file("example.txt", "This is a test content for file writing.")
    print(result)

    # Reading from a file
    content = read_file("example.txt")
    print("File content:", content)
