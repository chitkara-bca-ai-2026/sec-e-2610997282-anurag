
students = {
    101: {"Name": "Aman", "Branch": "BCA AI", "Sem": 1, "Marks": [85, 90, 78]},
    102: {"Name": "Riya", "Branch": "BCA AI", "Sem": 1, "Marks": [88, 95]},
    103: {"Name": "Karan", "Branch": "BCA AI", "Sem": 1, "Marks": [92, 88, 90]},
    104: {"Name": "Simran", "Branch": "BCA AI", "Sem": 1, "Marks": [88, 91, 84]}
}

while True:

    print("\n================================")
    print("     STUDENT INFO MANAGEMENT")
    print("================================")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")

    choice = input("\nEnter your choice (1-7): ")

    if choice == "1":
        print("\n--- Enrolled Student Records ---")

        for roll in students:
            print("Roll No:", roll, "| Name:", students[roll]["Name"])
            print("Branch:", students[roll]["Branch"])
            print("Sem:", students[roll]["Sem"])
            print("Marks:", students[roll]["Marks"])

        print("Total Enrolled Students:", len(students))

    elif choice == "2":
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("Name:", students[roll]["Name"])
            print("Branch:", students[roll]["Branch"])
            print("Semester:", students[roll]["Sem"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student not found!")

    elif choice == "3":
        roll = int(input("Enter Roll Number: "))

        if roll not in students:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")
            sem = int(input("Enter Semester: "))

            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Sem": sem,
                "Marks": []
            }

            print("Student registered successfully!")
        else:
            print("Roll Number already exists!")

    elif choice == "4":
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("1. Update Branch")
            print("2. Update Semester")

            option = input("Enter your choice: ")

            if option == "1":
                branch = input("Enter new Branch: ")
                students[roll]["Branch"] = branch
                print("Branch updated successfully!")

            elif option == "2":
                sem = int(input("Enter new Semester: "))
                students[roll]["Sem"] = sem
                print("Semester updated successfully!")

            else:
                print("Invalid choice!")

        else:
            print("Student not found!")

    elif choice == "5":
        roll = int(input("Enter Roll Number for Academic Performance: "))

        if roll in students:
            marks = students[roll]["Marks"]

            total = sum(marks)
            average = total / len(marks)

            print("\n========== ACADEMIC REPORT ==========")
            print("Student Name:", students[roll]["Name"])
            print("Student Marks:", marks)
            print("Total Marks:", total, "/", len(marks) * 100)
            print("Average Marks:", round(average, 2))

            if average >= 40:
                print("Final Result: PASS")
            else:
                print("Final Result: FAIL")

        else:
            print("Student not found!")

    elif choice == "6":
        roll = int(input("Enter Roll Number to delete: "))

        if roll in students:
            students.pop(roll, None)
            print("Student record deleted successfully!")
        else:
            print("Student not found!")

    elif choice == "7":
        print("Thank you for using Student Information System.")
        break

    else:
        print("Invalid choice! Please try again.")
