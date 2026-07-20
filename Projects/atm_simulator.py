name = input("What is your name? :")
balance = 5000


print("="*40)
print("             ATM SIMULATOR")
print("="*40)
print("Welcome ", name + "!")

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")
print("4. Exit")
choose_option = int(input("Choose an option: "))
if choose_option == 1:
    print("Your balance is ",balance)
elif choose_option == 2:
    deposit = int(input("How much would you like to deposit?: "))
    print(deposit + balance)
    print("Deposit Sucessful")
    print("New Balance: ", deposit + balance)
elif choose_option == 3:
    withdraw = int(input("How much would you like to withdraw?: "))
    if withdraw > balance:
        print("Insufficient funds")
    else:
        print("Withdrawal Successful")
        print("Remaining Balance: ", balance - withdraw)
elif choose_option == 4:
    print("Thank you for banking with us!")