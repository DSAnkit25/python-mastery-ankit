# Features:
# Add contact (name + phone)
# View all contacts
# Search by name
# Exit

# Contacts Manager - Day 2 Mini Project
# Author: Ankit DS
# Description: Simple CLI tool to store and manage contacts using lists & dictionaries

contacts = []


def add_contact():
    """Add a new contact to the list."""
    name = input("Enter name: ").strip().title()
    phone = input("Enter phone number: ").strip()

    # Check if contact already exists
    for c in contacts:
        if c["name"] == name:
            print("\n❌ Contact already exists!\n")
            return

    contacts.append({"name": name, "phone": phone})
    print("\n✅ Contact added successfully!\n")


def view_contacts():
    """Display all stored contacts."""
    if not contacts:
        print("\n📭 No contacts found!\n")
        return

    print("\n📒 CONTACT LIST:")
    for idx, c in enumerate(contacts, start=1):
        print(f"{idx}. {c['name']} — {c['phone']}")
    print()


def search_contact():
    """Search for a contact by name."""
    search = input("Enter name to search: ").strip().title()

    found = False
    print()
    for c in contacts:
        if search in c["name"]:    # partial match allowed
            print(f"🔍 Found: {c['name']} — {c['phone']}")
            found = True

    if not found:
        print("❌ No matching contact found!")
    print()


def main():
    """Main menu loop for the Contact Manager."""
    while True:
        print("\n------ CONTACTS MANAGER ------")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            print("\n👋 Exiting Contacts Manager. Goodbye!\n")
            break
        else:
            print("\n⚠ Invalid choice! Please enter 1–4.\n")


if __name__ == "__main__":
    main()

