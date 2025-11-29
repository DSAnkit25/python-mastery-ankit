# DAY 3 MINI PROJECT — INVENTORY MANAGER
#
# This project builds the exact skills needed for:
# ✔ automation scripts
# ✔ data processing
# ✔ CLI tools
# ✔ AWS + API pipelines
# ✔ LLM automation flows
# You will build a CLI tool with these features:
# Add item
# Update quantity
# View all items
# Search item
# Calculate total inventory value
# Exit
from cgi import print_environ_usage

# inventory = {}


inventory = [] #list of dictionries
item_name = set() #for unique value

def add_item():
    name = input("enter name: ").strip().title()
    if name in item_name:
        print("item already exists")
        return
    qty = int(input("enter qty: "))
    price = float(input("enter price: "))
    inventory.append({"name": name, "qty": qty, "price": price})
    item_name.add(name)
    print("\n✅ added item to inventory\n")

def update_inventory():
    name = input("enter name: ").strip().title()
    for item in inventory:
        if item["name"] == name:
            new_qty = int(input("enter new qty: "))
            item["qty"] = new_qty
            print("Inventory updated")
    print("\n items not found in inventory \n")

def view_items():
    if not inventory:
        print("inventory is empty")
        return
    print("\n Inventory Items \n")
    for index,item in enumerate(inventory,start=1):
        print(f"{index}. {item['name']} - Qty: {item['qty']}, Price: {item['price']}")
    print()

def search_inventory():
    name = input("enter name: ").strip().title()
    found = False
    print()
    for item in inventory:
        if name in item["name"]:
            print(f"🔍 Found: {item['name']} — Qty: {item['qty']}, Price: {item['price']}")
            found = True
    if not found:
        print("No Match")
    print()
def total_value():
    """Calculate total inventory value."""
    if not inventory:
        print("\n📭 Inventory is empty!\n")
        return

    total = sum(item["qty"] * item["price"] for item in inventory)

    print(f"\n💰 Total Inventory Value: ₹{total:.2f}\n")

def main():
    while True:
        print("------ INVENTORY MANAGER ------")
        print("1. Add Item")
        print("2. Update Quantity")
        print("3. View Items")
        print("4. Search Item")
        print("5. Total Inventory Value")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_item()
        elif choice == "2":
            update_inventory()
        elif choice == "3":
            view_items()
        elif choice == "4":
            search_inventory()
        elif choice == "5":
            total_value()
        elif choice == "6":
            print("Thank you for using Inventory Manager Exit")
            break
        else:
            print("Invalid Choice")
if __name__ == "__main__":
    main()