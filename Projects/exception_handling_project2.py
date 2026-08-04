try:
    number = int(input("Enter a number: "))
    result = 100 / number
except ValueError:
    print("Invalid number.")
except ZeroDivisionError:
    print("You can't divide by 0.")
else:
    print(result)
    print("Good job!")
finally:
    print("Finished.")


print(int("10"))