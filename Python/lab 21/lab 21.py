
def get_document_statistics(filename):
    with open(filename, "r") as file:
        data = file.readlines()

    line_count = len(data)
    word_count = 0
    char_count = 0

    for line in data:
        word_count = word_count + len(line.split())
        char_count = char_count + len(line)

    return line_count, word_count, char_count


def display_document(filename):
    with open(filename, "r") as file:
        data = file.readlines()

    print("\n--- Document Preview ---")

    for i in range(len(data)):
        print(i + 1, "|", data[i], end="")


filename = "document.txt"

while True:

    print("\n==============================")
    print("     DOCUMENT STATISTICS TOOL")
    print("==============================")

    print("\nSelect an operation:")
    print("1. Calculate Document Statistics")
    print("2. Display Document Content")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        lines, words, characters = get_document_statistics(filename)

        print("\n========== DOCUMENT REPORT ==========")
        print("Target File:", filename)
        print("Total Lines:", lines)
        print("Total Words:", words)
        print("Total Characters:", characters)

    elif choice == "2":
        display_document(filename)

    elif choice == "3":
        print("Thank you for using Document Statistics Tool. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
