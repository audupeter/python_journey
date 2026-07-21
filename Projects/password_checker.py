print("="*40)
print("             PASSWORD CHECKER")
print("="*40)
print()
password = "python123"
enter_pass = input("Enter Password: ")
trials = password != enter_pass
if password == enter_pass:
    print("Access Granted!")
    exit
elif password != enter_pass:
    print("Access Denied.")
    while trials <= 2:
        enter_pass = input("Enter Password: ")
        if password == enter_pass:
            print("Access Granted!")
        elif password != enter_pass:
            print("Access Denied")
            trials = trials + 1