print("="*40)
print("         AGE CALCULATOR")
print("="*40)

name = input("What is your name? ")
current_age = int(input("How old are you? "))
future_age = current_age + 10
current_year = int(input("What year is it now? "))
future_year = current_year + 10
print(" ")
print("Name: ", name)
print("Current Age: ", current_age)
print("Current Year: ", current_year)
print("In " , future_year, " you will be ", future_age,  " years old.")