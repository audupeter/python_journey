print("="*40)
print("             PASSWORD CHECKER")
print("="*40)
print()
password = "python123"
trials = 0
while trials <= 2:
    enter_pass = input("Enter Password: ")
    if password == enter_pass:
        print("Access Granted!")
        break 
    else:
        print("Incorrect Password. try again")
        trials = trials + 1

if trials == 3:
    print("Access Denied.")