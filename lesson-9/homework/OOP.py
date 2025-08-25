#Lesson - 9
# ======================================================
# Object-Oriented Programming (OOP) Exercises - Homework
# ======================================================

# 1. Circle Class
# Write a Python program to create a class representing a Circle.
# Include methods to calculate its area and perimeter.
import math
from datetime import date

class Circle:
    # Constructor with radius
    def __init__(self, radius):
        self.radius = radius

    # Method to calculate area of circle
    def area(self):
        return math.pi * (self.radius ** 2)

    # Method to calculate perimeter (circumference) of circle
    def perimeter(self):
        return 2 * math.pi * self.radius

# Example usage
c = Circle(5)
print("\nQ1. Circle Class")
print("Area:", c.area())
print("Perimeter:", c.perimeter())


# 2. Person Class
# Write a Python program to create a Person class. Include attributes like
# name, country, and date of birth. Implement a method to determine the person's age.
class Person:
    # Constructor with name, country, and date of birth (tuple: YYYY, MM, DD)
    def __init__(self, name, country, dob):
        self.name = name
        self.country = country
        self.dob = date(*dob)  # convert tuple into a date object

    # Method to calculate age
    def age(self):
        today = date.today()
        return today.year - self.dob.year - ((today.month, today.day) < (self.dob.month, self.dob.day))

# Example usage
p = Person("Alice", "Uzbekistan", (2000, 5, 15))
print("\nQ2. Person Class")
print("Name:", p.name, "| Country:", p.country, "| Age:", p.age())


# 3. Calculator Class
# Write a Python program to create a Calculator class.
# Include methods for basic arithmetic operations.
class Calculator:
    # Addition
    def add(self, a, b):
        return a + b

    # Subtraction
    def subtract(self, a, b):
        return a - b

    # Multiplication
    def multiply(self, a, b):
        return a * b

    # Division (with error handling for division by zero)
    def divide(self, a, b):
        return a / b if b != 0 else "Error: Division by zero"

# Example usage
calc = Calculator()
print("\nQ3. Calculator Class")
print("Add:", calc.add(5, 3))
print("Divide:", calc.divide(10, 2))


# 4. Shape and Subclasses
# Create a base class Shape with area and perimeter methods.
# Implement subclasses: Circle, Triangle, and Square.
class Shape:
    def area(self):
        pass

    def perimeter(self):
        pass

# Circle subclass (renamed to ShapeCircle to avoid name conflict with Q1)
class ShapeCircle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return 2 * math.pi * self.radius

# Square subclass
class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2

    def perimeter(self):
        return 4 * self.side

# Triangle subclass
class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        s = self.perimeter() / 2  # semi-perimeter
        # Heron's formula for triangle area
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

# Example usage
sq = Square(4)
print("\nQ4. Shape and Subclasses")
print("Square area:", sq.area(), "Perimeter:", sq.perimeter())


# 5. Binary Search Tree Class
# Create a Binary Search Tree with methods for inserting and searching.
class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    # Insert a key into BST
    def insert(self, key):
        if self.root is None:
            self.root = BSTNode(key)
        else:
            self._insert(self.root, key)

    # Helper function for insert
    def _insert(self, node, key):
        if key < node.key:
            if node.left is None:
                node.left = BSTNode(key)
            else:
                self._insert(node.left, key)
        else:
            if node.right is None:
                node.right = BSTNode(key)
            else:
                self._insert(node.right, key)

    # Search for a key
    def search(self, key):
        return self._search(self.root, key)

    # Helper function for search
    def _search(self, node, key):
        if node is None or node.key == key:
            return node is not None
        elif key < node.key:
            return self._search(node.left, key)
        else:
            return self._search(node.right, key)

# Example usage
bst = BST()
bst.insert(10)
bst.insert(5)
bst.insert(20)
print("\nQ5. Binary Search Tree")
print("Search 5:", bst.search(5))
print("Search 15:", bst.search(15))


# 6. Stack Data Structure
# Create a Stack with push, pop, and is_empty methods.
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)  # add item to stack

    def pop(self):
        return self.items.pop() if not self.is_empty() else "Stack is empty"

    def is_empty(self):
        return len(self.items) == 0

# Example usage
s = Stack()
s.push(10)
s.push(20)
print("\nQ6. Stack Data Structure")
print("Popped:", s.pop())


# 7. Linked List Data Structure
# Create a Linked List with methods to display, insert, and delete nodes.
class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # Display all nodes
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    # Insert at beginning
    def insert(self, data):
        new_node = ListNode(data)
        new_node.next = self.head
        self.head = new_node

    # Delete node by key
    def delete(self, key):
        current = self.head
        if current and current.data == key:
            self.head = current.next
            return
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next
        if current:
            prev.next = current.next

# Example usage
ll = LinkedList()
ll.insert(10)
ll.insert(20)
print("\nQ7. Linked List Data Structure")
ll.display()
ll.delete(10)
ll.display()


# 8. Shopping Cart Class
# Create a ShoppingCart with add, remove, and total_price methods.
class ShoppingCart:
    def __init__(self):
        self.items = {}

    def add_item(self, item, price, qty=1):
        if item in self.items:
            self.items[item]['qty'] += qty
        else:
            self.items[item] = {'price': price, 'qty': qty}

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]

    def total_price(self):
        return sum(info['price'] * info['qty'] for info in self.items.values())

# Example usage
cart = ShoppingCart()
cart.add_item("Apple", 2, 3)
cart.add_item("Banana", 1, 5)
print("\nQ8. Shopping Cart Class")
print("Total:", cart.total_price())


# 9. Stack with Display
# Create a Stack with push, pop, and display methods.
class StackWithDisplay:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if self.items else "Stack is empty"

    def display(self):
        print("Stack:", self.items)

# Example usage
sd = StackWithDisplay()
sd.push(5)
sd.push(15)
print("\nQ9. Stack with Display")
sd.display()
sd.pop()
sd.display()


# 10. Queue Data Structure
# Create a Queue with enqueue, dequeue, and display methods.
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)  # add item at end

    def dequeue(self):
        return self.items.pop(0) if self.items else "Queue is empty"

    def display(self):
        print("Queue:", self.items)

# Example usage
q = Queue()
q.enqueue(10)
q.enqueue(20)
print("\nQ10. Queue Data Structure")
q.display()
q.dequeue()
q.display()


# 11. Bank Class
# Create a Bank class with account creation, deposit, withdraw, and balance checking.
class Bank:
    def __init__(self):
        self.accounts = {}  # dictionary to hold accounts

    # Create account
    def create_account(self, acc_no, name, balance=0):
        self.accounts[acc_no] = {"name": name, "balance": balance}

    # Deposit money
    def deposit(self, acc_no, amount):
        if acc_no in self.accounts:
            self.accounts[acc_no]["balance"] += amount

    # Withdraw money (with balance check)
    def withdraw(self, acc_no, amount):
        if acc_no in self.accounts and self.accounts[acc_no]["balance"] >= amount:
            self.accounts[acc_no]["balance"] -= amount
        else:
            print("Insufficient funds or account not found")

    # Check balance
    def check_balance(self, acc_no):
        return self.accounts[acc_no]["balance"] if acc_no in self.accounts else "Account not found"

# Example usage
bank = Bank()
bank.create_account(101, "Alice", 500)
bank.deposit(101, 200)
print("\nQ11. Bank Class")
print("Balance:", bank.check_balance(101))
bank.withdraw(101, 100)
print("Balance:", bank.check_balance(101))
