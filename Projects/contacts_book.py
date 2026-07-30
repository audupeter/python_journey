print("="*45)
print("                CONTACTS BOOK")
print("="*45)

name = input("Enter name: ").strip().title()
phone_number = int(input("Enter Phone number: "))

contacts = [name, phone_number]
for contact in contacts:
    print("Contact:", contact)

def add_contact():
    return contacts.append("Name:", name, "Phone Number:", phone_number)

print(contacts)