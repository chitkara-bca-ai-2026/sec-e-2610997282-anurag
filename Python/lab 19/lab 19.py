
import os

def write_notes(filename, content):
    with open(filename, "w") as file:
        file.write(content)

    print("Notes successfully saved to", filename)


def read_notes(filename):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            content = file.read()

        print("\n--- Notes Content ---")
        print(content)

    else:
        print("File does not exist!")


while True:

    print("\n==============================")
    print("   STUDENT NOTES MANAGEMENT")
    print("==============================")

    print("\nSelect an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        notes = input("Enter notes to save: ")
        write_notes("notes.txt", notes)

    elif choice == "2":
        read_notes("notes.txt")

    elif choice == "3":
        print("Thank you for using the Notes Management System. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
