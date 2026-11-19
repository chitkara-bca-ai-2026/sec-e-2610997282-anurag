
books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering")
]

library_categories = {"Programming", "AI", "Software Engineering"}

student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

while True:

    print("\n========================================")
    print("       LIBRARY BOOK & CATEGORY MANAGER")
    print("========================================")

    print("\nSelect an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")

    choice = input("\nEnter your choice (1-6): ")

    if choice == "1":
        print("\n--- Current Library Catalog ---")

        for i in range(len(books)):
            title, author, year, category = books[i]
            print(i + 1, ".", title, "by", author, "(" + year + ") | Genre:", category)

        print("Total Books:", len(books))

    elif choice == "2":
        print("\n--- Add New Book Record ---")

        title = input("Enter book title: ")
        author = input("Enter author name: ")
        year = input("Enter publication year: ")
        category = input("Enter category/genre: ")

        book = (title, author, year, category)

        books.append(book)
        library_categories.add(category)

        print("\n[ SUCCESS ]", title, "added to library.")
        print("[ INFO ] Category set updated with:", category)

    elif choice == "3":
        print("\n--- Unique Library Categories ---")

        for category in sorted(library_categories):
            print("-", category)

        print("Total Unique Genres:", len(library_categories))

    elif choice == "4":
        category = input("Enter category to add to wishlist: ")

        student_wishlist.add(category)

        print("[ SUCCESS ]", category, "added to student wishlist.")

    elif choice == "5":
        print("\n--- Category Gap Analysis ---")

        print("\nCategories available in both:")
        print(library_categories.intersection(student_wishlist))

        print("\nCategories requested but not available:")
        print(student_wishlist.difference(library_categories))

        print("\nAll categories:")
        print(library_categories.union(student_wishlist))

    elif choice == "6":
        print("Thank you for using Library Book Manager!")
        break

    else:
        print("Invalid choice! Please try again.")
