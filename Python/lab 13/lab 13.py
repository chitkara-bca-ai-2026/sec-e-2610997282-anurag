
items = ["Notebook", "Pen", "Eraser", "Ruler"]

while True:

    print("\n================================")
    print("       INVENTORY CONTROL SYSTEM")
    print("================================")

    print("\nSelect an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ")

    if choice == "1":
        print("\n--- Current Inventory ---")

        for i in range(len(items)):
            print(i + 1, ".", items[i])

    elif choice == "2":
        item = input("Enter item name to add: ")
        items.append(item)
        print(item, "added to inventory.")

    elif choice == "3":
        item = input("Enter item name to remove: ")

        if item in items:
            items.remove(item)
            print(item, "removed from inventory.")
        else:
            print("Item not found in inventory.")

    elif choice == "4":
        items.sort()
        print("Inventory sorted alphabetically.")
        print("Updated Inventory:")

        for i in range(len(items)):
            print(i + 1, ".", items[i])

    elif choice == "5":
        print("Thank you for using Inventory Control System!")
        break

    else:
        print("Invalid choice! Please try again.")
