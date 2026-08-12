
contacts = {}


# Add Contact
def add_contact():

    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully!")


# View Contacts
def view_contacts():

    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("\n========== CONTACTS ==========")

    for name, details in contacts.items():

        print("\nName  :", name)
        print("Phone :", details["phone"])
        print("Email :", details["email"])


# Search Contact
def search_contact():

    name = input("Enter name to search: ")

    if name in contacts:

        print("\nContact Found")
        print("Name  :", name)
        print("Phone :", contacts[name]["phone"])
        print("Email :", contacts[name]["email"])

    else:
        print("Contact not found.")


# Update Contact
def update_contact():

    name = input("Enter name to update: ")

    if name in contacts:

        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")

        contacts[name]["phone"] = phone
        contacts[name]["email"] = email

        print("Contact updated successfully!")

    else:
        print("Contact not found.")


# Delete Contact
def delete_contact():

    name = input("Enter name to delete: ")

    if name in contacts:

        del contacts[name]

        print("Contact deleted successfully!")

    else:
        print("Contact not found.")


# Main Menu
while True:

    print("\n========== CONTACT BOOK ==========")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_contact()

    elif choice == "2":
        view_contacts()

    elif choice == "3":
        search_contact()

    elif choice == "4":
        update_contact()

    elif choice == "5":
        delete_contact()

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break

    else:
        print("Invalid choice.")
