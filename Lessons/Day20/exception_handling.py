try:
    number = int(input("Enter a Number: "))
    print(number)

except ValueError:
    print("Enter a valid number.")
finally:
    print("Finished.")
try: 
    result = 10 / 0
    print(result)

except ZeroDivisionError:
    print("You can't divide by 0")

try:
    number = int(input("Enter a number: "))
    result = 10 / number
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("You can't divide by 0")
else: 
    print("Good job!")
