# -------------------------------
# Contact Book Application
# -------------------------------

contacts = []

# Function to Add Contact
def add_contact():
    print("\n----- Add New Contact -----")
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    }

    contacts.append(contact)
    print("\n✅ Contact Added Successfully!")

# Function to View Contacts
def view_contacts():
    print("\n----- Contact List -----")

    if len(contacts) == 0:
        print("No contacts found.")
        return

    print("{:<20} {:<15}".format("Name", "Phone Number"))
    print("-" * 40)

    for contact in contacts:
        print("{:<20} {:<15}".format(contact["Name"], contact["Phone"]))

# Function to Search Contact
def search_contact():
    print("\n----- Search Contact -----")
    search = input("Enter Name or Phone Number: ").lower()

    found = False

    for contact in contacts:
        if search == contact["Name"].lower() or search == contact["Phone"]:
            print("\nContact Found")
            print("-" * 30)
            print("Name    :", contact["Name"])
            print("Phone   :", contact["Phone"])
            print("Email   :", contact["Email"])
            print("Address :", contact["Address"])
            found = True
            break

    if not found:
        print("❌ Contact not found.")

# Function to Update Contact
def update_contact():
    print("\n----- Update Contact -----")
    name = input("Enter Contact Name: ").lower()

    for contact in contacts:
        if contact["Name"].lower() == name:

            print("Leave blank if you don't want to change a field.")

            new_phone = input(f"New Phone ({contact['Phone']}): ")
            new_email = input(f"New Email ({contact['Email']}): ")
            new_address = input(f"New Address ({contact['Address']}): ")

            if new_phone:
                contact["Phone"] = new_phone

            if new_email:
                contact["Email"] = new_email

            if new_address:
                contact["Address"] = new_address

            print("\n✅ Contact Updated Successfully!")
            return

    print("❌ Contact not found.")

# Function to Delete Contact
def delete_contact():
    print("\n----- Delete Contact -----")
    name = input("Enter Contact Name: ").lower()

    for contact in contacts:
        if contact["Name"].lower() == name:
            contacts.remove(contact)
            print("\n✅ Contact Deleted Successfully!")
            return

    print("❌ Contact not found.")

# Main Program
while True:

    print("\n")
    print("=" * 45)
    print("         CONTACT BOOK APPLICATION")
    print("=" * 45)

    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

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
        print("\nThank you for using Contact Book!")
        break

    else:
        print("\n❌ Invalid Choice! Please enter a number between 1 and 6.")