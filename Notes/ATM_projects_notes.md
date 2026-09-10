# 🏧 ATM Simulator Project Notes

## 📖 Project Goal

Build a realistic ATM Simulator that grows as I learn Python.

Instead of rebuilding the project every few days, I will continue improving the same project by adding new Python concepts as I learn them.

---

# 🎯 Project Objectives

The ATM Simulator should allow a user to:

- Check account balance.
- Deposit money.
- Withdraw money.
- View a statement of account.
- Exit the program.

The program should feel more realistic after every lesson.

---

# 📅 Project Evolution

## Version 1 (Current)

Current features:

- Greets the user.
- Displays a menu.
- Allows:
  - Check Balance
  - Deposit
  - Withdraw
  - Exit

Uses:

- Variables
- Input
- If/Else
- While Loop

---

# Future Versions

As I learn more Python, I will continue improving the ATM.

---

# 🧠 Design Decisions

## Greeting

Instead of:

```text
Hello Peter!
```

Ask the user for their name.

Example:

```text
Enter your name:
```

Then display:

```text
Welcome, Peter!
```

Although real ATMs don't ask for names, this makes the project more interactive.

---

# Menu

Display:

```text
====================
ATM SIMULATOR
====================

1. Check Balance
2. Deposit
3. Withdraw
4. Statement of Account
5. Exit
```

---

# Menu Loop

The menu should continue showing after every completed transaction.

Flow:

```text
Start

↓

Enter Name

↓

Display Menu

↓

Choose Option

↓

Complete Option

↓

Return to Menu

↓

Choose Another Option

↓

Exit

↓

Program Ends
```

The user should never need to restart the program just to perform another transaction.

---

# Invalid Menu Option

If the user enters an option that doesn't exist:

Display:

```text
Please pick one of the available options.
```

Then return to the menu.

---

# Balance

The balance should be stored in a variable.

Example:

```python
balance = 5000
```

Every deposit or withdrawal updates this value.

---

# Deposits

Rules:

- Deposit amount must be greater than ₦0.
- Reject negative numbers.
- Reject zero.

Example:

```text
Deposit amount must be greater than ₦0.
```

After a successful deposit:

- Update balance.
- Save transaction.
- Return to menu.

---

# Withdrawals

Rules:

- Withdrawal amount must be greater than ₦0.
- Cannot withdraw more than the current balance.

Example:

```text
Insufficient funds.
```

After a successful withdrawal:

- Update balance.
- Save transaction.
- Return to menu.

---

# Functions

Eventually each menu option should become its own function.

Example:

```python
check_balance()

deposit()

withdraw()

statement()

menu()
```

This makes the program cleaner and easier to maintain.

---

# Transaction History

Instead of only changing the balance...

Store every transaction.

Example:

```python
transactions = []
```

Whenever a deposit happens:

```python
transactions.append("Deposit: ₦5000")
```

Whenever a withdrawal happens:

```python
transactions.append("Withdrawal: ₦2000")
```

The transaction history grows automatically.

---

# Statement of Account

The statement should display every transaction made during the session.

Instead of:

```python
print(transactions[0])
print(transactions[1])
print(transactions[2])
```

Use:

```python
for transaction in transactions:
    print(transaction)
```

This works for any number of transactions.

---

# While Loop

The entire ATM should run inside a while loop.

The loop only ends when the user selects:

```text
Exit
```

---

# Input Validation

Protect the program against invalid input whenever possible.

Examples:

Invalid menu option.

Negative deposit.

Negative withdrawal.

Withdrawal greater than balance.

Deposit of ₦0.

---

# Future Improvements

As I continue learning Python, I plan to add:

## PIN Authentication

Allow three attempts.

Possible idea:

```python
for attempt in range(3):
```

After three failed attempts:

```text
Access Denied
```

---

## Account Number

Ask for an account number.

---

## Multiple Accounts

Store different users.

---

## Transfer Money

Transfer between accounts.

---

## Mini Statement

Show only recent transactions.

---

## Receipt

Display a receipt after every transaction.

---

## Date and Time

Add timestamps to every transaction.

---

## Save Data

Eventually save balances and transactions to a file so data isn't lost when the program closes.

---

# Python Concepts Used

Current:

- Variables
- Input
- print()
- If
- Else
- Elif
- While Loop
- Functions
- Parameters
- Return Values
- Lists
- append()
- remove()
- for Loops
- range()

Future:

- Dictionaries
- File Handling
- Modules
- Exception Handling
- Classes (OOP)

---

# Lessons This Project Reinforced

Day 4

Decision making.

---

Day 6

Loops keep the menu running.

---

Day 7

Each option becomes a function.

---

Day 8

Functions receive parameters.

---

Day 9

Functions return values.

---

Day 10

Store transactions in a list.

---

Day 11

Modify transaction history with append().

---

Day 12

Print the statement using a for loop.

---

Day 13

Use range() to limit PIN attempts.

---

# Project Philosophy

This project is not meant to be finished quickly.

It will grow with every new Python concept I learn.

Each lesson should improve the ATM Simulator rather than replacing it with a new project.

By the end of my Python journey, this ATM Simulator should demonstrate how much I've grown as a programmer.

---

> "Great software isn't built in one day. It's improved one feature at a time."
