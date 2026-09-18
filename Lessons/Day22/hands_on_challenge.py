# Challenge 1 and challenge 2
balance = 50000
def check_balance(balance):
    return(balance)
balance = check_balance(balance)
print("Your Balance is:", balance)

def deposit(balance, amount):
    return(balance + amount)
print("Deposit Successful!")
total = deposit(balance, 10000)
print("New Balance:", total)

def withdrawal(balance, amount):
    if amount > balance:
        print("Insufficient funds")
    else:
        print("Withdrawal successful!")
        return (balance - amount)
total = withdrawal(balance, 60000)
print("New Balance:", total)

deposit(balance, 10000)
print(deposit(balance, 10000))