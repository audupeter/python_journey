# 🐍 Python Cheat Sheet

A quick reference guide built during my 365-Day Python Journey.

---

# 📅 Day 1 – Python Basics

## Print Output

```python
print("Hello, World!")
```

## Variables

```python
name = "Peter"
age = 24
```

## User Input

```python
name = input("Enter your name: ")
```

---

# 📅 Day 2 – Git & GitHub

## Initialize Repository

```bash
git init
```

## Check Status

```bash
git status
```

## Stage Files

```bash
git add .
```

## Commit

```bash
git commit -m "Your message"
```

## Push

```bash
git push
```

---

# 📅 Day 3 – Variables & Input

## Integer

```python
age = 24
```

## Float

```python
height = 6.0
```

## String

```python
name = "Peter"
```

## Input

```python
name = input("Name: ")
```

---

# 📅 Day 4 – If & Else

```python
if age >= 18:
    print("Adult")
else:
    print("Minor")
```

## Comparison Operators

```python
==
!=
>
<
>=
<=
```

---

# 📅 Day 5 – Elif

```python
if score >= 90:
    print("A")
elif score >= 70:
    print("B")
else:
    print("F")
```

---

# 📅 Day 6 – While Loops

```python
while True:
    print("Running")
```

```python
while balance > 0:
    print(balance)
```

---

# 📅 Day 7 – Functions

```python
def greet():
    print("Hello")
```

## Calling a Function

```python
greet()
```

---

# 📅 Day 8 – Parameters

```python
def greet(name):
    print("Hello", name)
```

```python
greet("Peter")
```

---

# 📅 Day 9 – Return Values

```python
def add(a, b):
    return a + b
```

```python
answer = add(5, 3)
```

---

# 📅 Day 10 – Lists

## Create List

```python
numbers = [1, 2, 3]
```

## Indexing

```python
numbers[0]
numbers[-1]
```

---

# 📅 Day 11 – List Methods

## Add Item

```python
numbers.append(4)
```

## Remove Item

```python
numbers.remove(2)
```

## Replace Item

```python
numbers[1] = 10
```

---

# 📅 Day 12 – For Loops

## Loop Through List

```python
for item in numbers:
    print(item)
```

---

# 📅 Day 13 – range()

## Count

```python
range(5)
```

## Start & Stop

```python
range(1, 5)
```

## Step

```python
range(2, 11, 2)
```

## Loop

```python
for i in range(5):
    print(i)
```

---

# 📅 Day 14 – Strings

## Length

```python
len(name)
```

## Positive Index

```python
name[0]
```

## Negative Index

```python
name[-1]
```

## Uppercase

```python
name.upper()
```

## Lowercase

```python
name.lower()
```

## Title Case

```python
name.title()
```

## Remove Spaces

```python
name.strip()
```

## Check Text

```python
"a" in name
```

---

# 📅 Day 15 – Dictionaries

## Create Dictionary

```python
student = {
    "name": "Peter",
    "age": 24
}
```

## Access Value

```python
student["name"]
```

## Add Data

```python
student["course"] = "Mathematics"
```

## Update Data

```python
student["age"] = 25
```

## Delete Data

```python
del student["age"]
```

## Loop Through Keys

```python
for key in student:
    print(key)
```

## Loop Through Values

```python
for key in student:
    print(student[key])
```

---

# ⚡ Common Built-in Functions

```python
print()
input()
len()
range()
```

---

# 🎯 Common String Methods

```python
.upper()
.lower()
.title()
.strip()
```

---

# 📚 Common List Methods

```python
.append()
.remove()
```

---

# 🧠 Golden Rules

- Indexes start at **0**.
- Negative indexes count from the end.
- `=` assigns a value.
- `==` compares values.
- `return` sends a value back.
- `print()` displays output.
- `for` loops iterate over collections.
- `while` loops repeat while a condition is `True`.
- Dictionaries store **key-value pairs**.

---

---

# 📅 Day 16 – Tuples

## Create Tuple

```python
fruits = ("Apple", "Banana", "Orange")
```

## Access Items

```python
fruits[0]
fruits[-1]
```

## Count Items

```python
len(fruits)
```

## Loop Through Tuple

```python
for fruit in fruits:
    print(fruit)
```

## Remember

- Uses `()`
- Ordered
- Immutable
- Supports indexing
- Works with `len()`
- Works with `for` loops

---

# 📅 Day 17 – Sets

## Create a Set

```python
fruits = {"Apple", "Banana", "Orange"}
```

## Add Item

```python
fruits.add("Mango")
```

## Remove Item

```python
fruits.remove("Banana")
```

## Count Items

```python
len(fruits)
```

## Loop Through a Set

```python
for fruit in fruits:
    print(fruit)
```

## Remember

- Uses `{}`
- Stores unique items only
- Automatically removes duplicates
- Supports `len()`
- Supports `for` loops
- Does **not** use key-value pairs

---

---

# 📅 Day 18 – Modules

## Create a Module

```python
# calculator.py

def add(a, b):
    return a + b
```

## Import Entire Module

```python
import calculator

print(calculator.add(5, 3))
```

## Import Specific Function

```python
from calculator import add

print(add(5, 3))
```

## Built-in `math` Module

```python
import math

math.sqrt(25)
```

## Built-in `random` Module

```python
import random

random.randint(1, 10)
```

## Remember

- A module is a reusable Python file.
- Avoid rewriting the same code.
- `import module` imports everything.
- `from module import function` imports only what you need.
- Modules make projects cleaner and easier to maintain.

---

# 📅 Day 19 – File Handling

## Open a File

```python
file = open("notes.txt", "r")
```

## Write to a File

```python
file = open("notes.txt", "w")
file.write("Hello")
file.close()
```

## Read a File

```python
file = open("notes.txt", "r")
print(file.read())
file.close()
```

## Append to a File

```python
file = open("notes.txt", "a")
file.write("\nWelcome back!")
file.close()
```

## Remember

- `open()` opens a file.
- `"w"` writes (creates or replaces).
- `"r"` reads.
- `"a"` appends.
- `.write()` writes data.
- `.read()` reads data.
- `.close()` closes the file.

---

# 📅 Day 20 – Exception Handling

## Basic Exception Handling

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid number.")
```

---

## Handle Division by Zero

```python
try:
    result = 100 / number
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

---

## Using `else`

```python
try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input.")
else:
    print("Success!")
```

---

## Using `finally`

```python
try:
    print("Trying...")
finally:
    print("Finished.")
```

---

## Multiple Exceptions

```python
try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Numbers only!")
except ZeroDivisionError:
    print("Zero is not allowed!")
```

---

## Remember

- `try` → Code that may fail.
- `except` → Handles errors.
- `else` → Runs only if no error occurs.
- `finally` → Always runs.
- Exception handling keeps programs from crashing.

---
# Python Cheat Sheet — Day 21

## Functions: Parameters & Arguments

### Parameter

A parameter is a placeholder in a function definition.

```python
def greet(name):
    print("Hello", name)
```

### Argument

An argument is the actual value passed into a function.

```python
greet("Peter")
```

`name` = parameter
`"Peter"` = argument

---

## Multiple Parameters

```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)
```

---

## Return

`return` sends a value back from a function.

```python
def multiply(a, b):
    return a * b

answer = multiply(5, 4)
print(answer)
```

Output:

```text
20
```

---

## Default Parameters

A default parameter is used when no argument is provided.

```python
def greet(name="Peter"):
    print("Hello", name)

greet()
```

Output:

```text
Hello Peter
```

Providing another argument replaces the default:

```python
greet("John")
```

---

## Variable Scope

### Local Variable

Created inside a function.

```python
def greet():
    message = "Hello"
    print(message)
```

`message` is local to the function.

### Global Variable

Created outside a function.

```python
name = "Peter"

def greet():
    print(name)
```

---

## Function Design Pattern

Think:

```text
Input → Processing → Return
```

Example:

```python
def deposit(balance, amount):
    return balance + amount
```

---

## Calculator Function Pattern

```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b
```

---

## Stretch Challenge

```python
def calculate_total_cost(price, quantity):
    return price * quantity

total_cost = calculate_total_cost(500, 4)
print(total_cost)
```

Output:

```text
2000
```
---
# Day 22 — Functions: Deeper Practice

## Function Flow

```text
Arguments
    ↓
Function
    ↓
Processing
    ↓
Return value
    ↓
Variable stores returned value
```

---

## Parameters

Parameters are placeholders defined in a function.

```python
def add(a, b):
    return a + b
```

`a` and `b` are parameters.

---

## Arguments

Arguments are the actual values passed to a function.

```python
add(10, 20)
```

`10` and `20` are arguments.

---

## Return

`return` sends a value back from a function.

```python
def add(a, b):
    return a + b

result = add(10, 20)
```

Result:

```python
result = 30
```

### Important

The variable stores the **returned value**, not the function itself.

---

## Return Ends the Function

```python
def example():
    return 10
    print("This will not run")
```

Anything after `return` in the same execution path will not run.

---

## Multiple Parameters

```python
def calculate_total(price, quantity):
    return price * quantity
```

Call:

```python
total = calculate_total(500, 3)
```

Result:

```python
total = 1500
```

---

## Functions and Variables

```python
balance = 50000
total = withdrawal(balance, 10000)
```

If the function returns `40000`:

```text
balance → 50000
total   → 40000
```

The original variable does not automatically change.

---

## Updating a Variable With a Return Value

To replace the old value with the returned value:

```python
balance = deposit(balance, 10000)
```

The returned value becomes the new value of `balance`.

---

## Conditional Function Logic

```python
def withdrawal(balance, amount):
    if amount > balance:
        print("Insufficient funds")
    else:
        print("Withdrawal successful!")
        return balance - amount
```

---

## `None`

If a function reaches the end without returning a value:

```python
def example():
    print("Hello")
```

then:

```python
result = example()
```

makes:

```python
result = None
```

---

## ATM Function Pattern

```python
def check_balance(balance):
    return balance

def deposit(balance, amount):
    return balance + amount

def withdrawal(balance, amount):
    # check condition
    # return updated balance when successful
```

---

## Function Design Pattern

When designing a function, ask:

1. What information does the function need?
2. What parameters should it receive?
3. What should it do with the information?
4. What should it return?

---

## Day 22 Key Reminder

```python
result = function(arguments)
```

means:

**call the function → get the returned value → store that value in `result`.**

---