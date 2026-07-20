print("="*40)
print("     GRADE CHECKER")
print("="*40)

name = input("What is your name?: ")
score = int(input(("Enter your score: ")))
print()
print("Name:",name)
if score >=70:
    print("Grade: A \nExcellent!") 
elif score >= 50:
    print("Grade: B \nYou passed!")
else:
    print("Grade: F \nKeep practising!")

if score == 100:
    print("Perfect score")