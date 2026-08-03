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