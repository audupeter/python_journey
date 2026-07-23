
balance = 5000


print("="*40)
print("             ATM SIMULATOR")
print("="*40)
print("Welcome! What do you want to do today?")

def show_menu():
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

def check_balance():
    print("Your balance is", balance)

def deposit():
    deposit = int(input("How much would you like to deposit?: "))
    print(deposit + balance)
    print("Deposit Sucessful")
    print("New Balance:", deposit + balance)

def withdraw():
    withdraw = int(input("How much would you like to withdraw?: "))
    if withdraw > balance:
        print("Insufficient funds")
    else:
        print("Withdrawal Successful")
        print("Remaining Balance:", balance - withdraw)

show_menu()
choose_option = int(input("Choose an option: "))
if choose_option == 1:
    check_balance()
elif choose_option == 2:
    deposit()
elif choose_option == 3:
    withdraw()    
elif choose_option == 4:
    print("Thank you for banking with us!")