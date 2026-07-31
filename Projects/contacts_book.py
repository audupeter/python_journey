print("="*45)
print("                CONTACTS BOOK")
print("="*45)
names = []
phone_numbers = []
contacts = [names, phone_numbers]
def menu():
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("Delete Contact")
    print("5. Exit")
    choice = int(input("What do you want to?: "))    
menu()
def add_contact():
        name = input("Enter name: ").strip().title()
        phone_number = int(input("Enter Phone number: "))
        names.append(name)
        phone_numbers.append(phone_number)
        print("Contact Saved")
        menu()

def view_contacts():
        for contact in contacts:
            print(contact)
