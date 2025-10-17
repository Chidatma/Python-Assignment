Python all assignments in this :
Assignment Folder --->> Commit --->> Push

Star my repo  https://github.com/Chidatma/Python-Assignment.git ⭐

# 🐍 Python Beginner Tasks: Combined Program

This repository contains a **single Python program** that combines two beginner-friendly tasks:

1. **Basic Mathematical Operations**  
2. **Personalized Welcome Message**  

This combined program demonstrates user input handling, arithmetic operations, string manipulation, and console output in Python. It is perfect for beginners to understand multiple Python concepts in one script.

---

## 📘 Problem Statement

The program performs **two main functions** sequentially:

**Task 1: Basic Mathematical Operations**  
- Prompt the user to enter **two numbers**.  
- Perform **addition, subtraction, multiplication, and division**.  
- Display the results in a clear format.

**Task 2: Welcome Message Generator**  
- Prompt the user to enter **first name** and **last name**.  
- Combine them into a **personalized greeting**.  
- Display the greeting message to the user.

This program helps beginners learn about **input handling, type conversion, arithmetic operations, string concatenation, and printing output** in a structured manner.

---

## 🧠 Functionality

1. The program first executes **Task 1**:
   - Asks for two numbers from the user.  
   - Calculates and prints **addition, subtraction, multiplication, and division**.

2. Then the program executes **Task 2**:
   - Asks for first and last name.  
   - Prints a **personalized welcome message**.

---

## 🖥️ Combined Code

```python
# Task 1: Basic Mathematical Operations
f1 = int(input("Enter a first number: "))
f2 = int(input("Enter a second number: "))

print("\n--- Results of Mathematical Operations ---")
print("Addition:", f1 + f2)
print("Subtraction:", f1 - f2)
print("Multiplication:", f1 * f2)
print("Division:", float(f1 / f2))

# Task 2: Welcome Message Generator
first_name = input("\nEnter your first name: ")
last_name = input("Enter your last name: ")

print("\nHello,", first_name + " " + last_name + "!" + " Welcome to the Python Program.")

Enter a first number: 10
Enter a second number: 5

--- Results of Mathematical Operations ---
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2.0

Enter your first name: Chidatma
Enter your last name: Patel

Hello, Chidatma Patel! Welcome to the Python Program.
