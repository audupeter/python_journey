print ("==" *15)
print("     CALCULATOR FUNCTIONS")
print("=="*15)

def add(a, b):
    return(a + b)
result = add(10, 30)
print(result)
print()

def subtract(a, b):
    return(a - b)
result = subtract(20, 15)
print(result)
print()

def multiply(a, b):
    return(a * b)
result = multiply(10, 5)
print(result)
print()

def divide(a, b):
    return( a / b)
result = divide(100, 50)
print(result)
print()

# Strech Challenge
def calculate_total_cost(price, quantity):
    return(price * quantity)
total_cost = calculate_total_cost(500, 4)
print(total_cost)