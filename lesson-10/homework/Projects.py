# Lesson - 10
# ==============================================
# Homework 1: ToDo List Application
# ==============================================

# Task class represents a single task in the ToDo List
class Task:
    def __init__(self, title, description, due_date, status="Incomplete"):
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status

    def mark_complete(self):
        # Change task status to Completed
        self.status = "Complete"

    def __str__(self):
        # Nicely formatted task information
        return f"{self.title} - {self.description} (Due: {self.due_date}, Status: {self.status})"


# ToDoList class manages multiple tasks
class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        # Add a new task into the list
        self.tasks.append(task)

    def mark_task_complete(self, title):
        # Mark a task complete by its title
        for task in self.tasks:
            if task.title == title:
                task.mark_complete()
                return f"Task '{title}' marked as complete."
        return f"Task '{title}' not found."

    def list_all_tasks(self):
        # Display all tasks
        return [str(task) for task in self.tasks]

    def list_incomplete_tasks(self):
        # Display only incomplete tasks
        return [str(task) for task in self.tasks if task.status == "Incomplete"]


# ==============================================
# Homework 2: Simple Blog System
# ==============================================

# Post class represents a single blog post
class Post:
    def __init__(self, title, content, author):
        self.title = title
        self.content = content
        self.author = author

    def __str__(self):
        # Nicely formatted post information
        return f"Title: {self.title}\nBy {self.author}\nContent: {self.content}\n"


# Blog class manages multiple posts
class Blog:
    def __init__(self):
        self.posts = []

    def add_post(self, post):
        # Add a new post
        self.posts.append(post)

    def list_all_posts(self):
        # Display all posts
        return [str(post) for post in self.posts]

    def posts_by_author(self, author):
        # Display posts by a specific author
        return [str(post) for post in self.posts if post.author == author]

    def delete_post(self, title):
        # Delete a post by its title
        for post in self.posts:
            if post.title == title:
                self.posts.remove(post)
                return f"Post '{title}' deleted."
        return f"Post '{title}' not found."

    def edit_post(self, old_title, new_title, new_content):
        # Edit a post by updating title and content
        for post in self.posts:
            if post.title == old_title:
                post.title = new_title
                post.content = new_content
                return f"Post '{old_title}' updated."
        return f"Post '{old_title}' not found."

    def latest_posts(self, count=3):
        # Show the most recent posts
        return [str(post) for post in self.posts[-count:]]


# ==============================================
# Homework 3: Simple Banking System
# ==============================================

# Account class represents a single bank account
class Account:
    def __init__(self, acc_number, holder_name, balance=0):
        self.acc_number = acc_number
        self.holder_name = holder_name
        self.balance = balance

    def deposit(self, amount):
        # Deposit money into account
        self.balance += amount
        return f"Deposited {amount}. New Balance: {self.balance}"

    def withdraw(self, amount):
        # Withdraw money with overdraft protection
        if amount > self.balance:
            return "Insufficient funds!"
        self.balance -= amount
        return f"Withdrew {amount}. New Balance: {self.balance}"

    def __str__(self):
        # Display account details
        return f"Account {self.acc_number} - {self.holder_name}, Balance: {self.balance}"


# Bank class manages multiple accounts
class Bank:
    def __init__(self):
        self.accounts = []

    def add_account(self, account):
        # Add a new account
        self.accounts.append(account)

    def find_account(self, acc_number):
        # Find account by account number
        for acc in self.accounts:
            if acc.acc_number == acc_number:
                return acc
        return None

    def check_balance(self, acc_number):
        # Show balance of a specific account
        acc = self.find_account(acc_number)
        if acc:
            return acc.balance
        return "Account not found."

    def deposit_money(self, acc_number, amount):
        # Deposit into a specific account
        acc = self.find_account(acc_number)
        if acc:
            return acc.deposit(amount)
        return "Account not found."

    def withdraw_money(self, acc_number, amount):
        # Withdraw from a specific account
        acc = self.find_account(acc_number)
        if acc:
            return acc.withdraw(amount)
        return "Account not found."

    def transfer_money(self, from_acc, to_acc, amount):
        # Transfer between two accounts
        acc1 = self.find_account(from_acc)
        acc2 = self.find_account(to_acc)
        if acc1 and acc2:
            if acc1.balance >= amount:
                acc1.withdraw(amount)
                acc2.deposit(amount)
                return f"Transferred {amount} from {from_acc} to {to_acc}"
            else:
                return "Insufficient funds for transfer!"
        return "One or both accounts not found."


# ==============================================
# MAIN PROGRAM (for testing all homeworks)
# ==============================================
if __name__ == "__main__":
    # -------- Test ToDoList --------
    print("\n=== ToDo List Test ===")
    todo = ToDoList()
    task1 = Task("Study", "Math homework", "2025-08-30")
    task2 = Task("Shopping", "Buy groceries", "2025-08-26")
    todo.add_task(task1)
    todo.add_task(task2)
    print(todo.list_all_tasks())
    print(todo.mark_task_complete("Study"))
    print(todo.list_incomplete_tasks())

    # -------- Test Blog --------
    print("\n=== Blog Test ===")
    blog = Blog()
    blog.add_post(Post("My Day", "It was great!", "Alice"))
    blog.add_post(Post("Python", "Python is fun!", "Bob"))
    print(blog.list_all_posts())
    print(blog.posts_by_author("Alice"))
    print(blog.delete_post("Python"))
    print(blog.list_all_posts())

    # -------- Test Bank --------
    print("\n=== Bank Test ===")
    bank = Bank()
    acc1 = Account("001", "John", 500)
    acc2 = Account("002", "Jane", 300)
    bank.add_account(acc1)
    bank.add_account(acc2)
    print(bank.deposit_money("001", 200))
    print(bank.withdraw_money("002", 100))
    print(bank.transfer_money("001", "002", 250))
    print(bank.check_balance("001"))
    print(bank.check_balance("002"))
