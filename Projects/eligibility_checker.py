print("="*40)
print("     ELIGIBILITY CHECKER")
print("="*40)

name = input("What is your name? ")
age = int(input("How old are you? "))

print()

print("Name: ", name)
print("Age: ", age)
if age >= 18:
    print("Status: You're eligible to vote.")
else:
    print("Status: You are not eligible to vote yet.")
if age >= 60:
        print("Discount: Eligible for Senior discount.")
else: 
    print("Discount: Not eligible for discount.")