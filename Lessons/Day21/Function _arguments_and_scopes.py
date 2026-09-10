def greet(name):
    print("Hello", name)

greet("Peter")

def add(a, b):
    return(a + b)
result = add(10, 20)
print(result)

## Default parameters

def greet(name = "Peter"):
    print("Hello", name)

greet()
greet("John")
## the default is used when we don't provide an argument 

## Variable Scope
def greet():
    message = "Hello"
    print(message)
greet()

## Global Variable
name = "Peter"

def greet():
    print(name)

greet()