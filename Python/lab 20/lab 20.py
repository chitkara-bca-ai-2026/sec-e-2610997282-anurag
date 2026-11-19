
def append_entry(filename, entry):
    with open(filename, "a") as file:
        file.write(entry + "\n")

    print("New entry logged successfully.")


def display_log(filename):
    with open(filename, "r") as file:
        data = file.readlines()

    print("\n========== DAILY LOG BOOK ==========")

    for i in range(len(data)):
        print(data[i], end="")

    print("\nTotal Log Entries:", len(data))


filename = "daily_log.txt"

with open(filename, "a") as file:
    pass

while True:

    print("\nSelect an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        entry = input("Enter log entry: ")
        append_entry(filename, entry)

    elif choice == "2":
        display_log(filename)

    elif choice == "3":
        print("Thank you for using the Daily Log Book. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
