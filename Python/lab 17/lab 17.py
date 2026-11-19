
students = {
    101: {"name": "Aman", "marks": [85, 90, 78]},
    102: {"name": "Riya", "marks": [88, 84, 92]}
}

def calculate_avg(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    total, average = calculate_avg(student["marks"])

    print("Roll No:", roll)
    print("Name:", student["name"])
    print("Marks:", student["marks"])
    print("Total:", total)
    print("Average:", round(average, 2))

def display_all_students():
    for roll in students:
        display_student(roll, students[roll])
        print("------------------------")

def add_student():
    roll = int(input("Enter Roll Number: "))

    if roll in students:
        print("Roll Number already exists!")
    else:
        name = input("Enter Student Name: ")
        marks = []

        for i in range(1, 4):
            mark = int(input("Enter marks for Subject " + str(i) + ": "))
            marks.append(mark)

        students[roll] = {"name": name, "marks": marks}
        print("Student added successfully!")

def search_student():
    roll = int(input("Enter Roll Number to search: "))

    student = students.get(roll)

    if student:
        display_student(roll, student)
    else:
        print("Student not found!")

while True:

    print("\n===== STUDENT RECORDS MANAGEMENT =====")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        display_all_students()

    elif choice == "2":
        add_student()

    elif choice == "3":
        search_student()

    elif choice == "4":
        print("Thank you for using Student Records Management System!")
        break

    else:
        print("Invalid choice! Please try again.")
