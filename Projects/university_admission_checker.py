print("="*40)
print("           UNIVERSITY ADMISSION CHECKER")
print("="*40)

name = input("Enter your name: ")
age = int(input("How old are you?: "))
score = int(input("Enter JAMB score: "))
department = input("Enter Desired Department: ").lower()

print("Student Name: ", name)
print("Age: ", age)
print("JAMB Score: ", score)
print()
if score >= 280:
    print("Excellent!")
    print("High chance of Admission.")
    print()
elif score >= 200:
    print("Good score.")
    print("You may get admission.")
    print()
else:
    print("Unfortunately,")
    print("you did not meet the cut-off mark.") 
    print()

if age >= 18:
    print("You meet the age requirement.")
    print()
else:
    print("Below recommended admission age.")
    print()

if department == "medicine":
    print("Required Score: 300")
elif department == "engineering":
    print("Required Score: 250")
elif department == "computer science":
    print("Required Score: 250")
else: 
    print("General admission requirement rules apply.")