# Regular Functions
def multiply(number):
    return number * 2
result = multiply(5)
print(result)

def division(a,b):
    return a / b
result = division(100,4)
print(result)

print()

# Lamda Functions
add = lambda a, b: a + b
result= add(10,5)
print(result)
subtract = lambda a, b : a - b
result = subtract(4,2)
print(result)

# Checking if lambda has limitations

check_balance = lambda balance: balance > 0
print(check_balance(5000))
print(check_balance(-200))

# Random code

balance = 5000

withdraw = lambda balance, amount: balance - amount

new_balance = withdraw(balance, 1500)

print(new_balance)
print(balance)