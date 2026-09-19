balance = 50000
print("="*50)
print("                 BANKING PROGRAM")
print("="*50)

def show_menu():
    print("Welcome!")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdrawal")
    print("4. Exit")

def check_balance(balance):
    return balance

def deposit(balance, amount ):
    return balance + amount

def withdrawal(balance, amount):
    if amount > balance:
        print("Insufficient Funds.")
        return balance
    else:
        print("Withdrawal Successful!")
    return balance - amount

running = True
while running:
    show_menu()
    try:
        choice = int(input("What do you want to do? "))
    except ValueError:
        print("Invalid input. Please enter a number.")
        continue
    if choice == 1:
        print ("Your Balance is:", check_balance(balance))
    elif choice == 2:
        try:
            amount = int(input("How much do you want to deposit? "))
            balance = deposit(balance, amount)
            print("Deposit successful! your balance is:", balance)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    elif choice == 3:
        try:
            amount = int(input("How much do you want to withdraw? "))
            balance = withdrawal(balance, amount)
            print("Balance:", balance)
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
    elif choice == 4:
        print("Goodbye!")
        running = False
    else:
        print("Invalid Option. Enter a valid option.")
