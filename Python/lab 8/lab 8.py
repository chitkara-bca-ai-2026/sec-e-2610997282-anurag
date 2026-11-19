
print("========================================")
print("       SCHOOL RESULT PROCESSING")
print("========================================")

name = input("Enter Student Name: ")
roll = input("Enter Roll Number: ")

marks_list = []
failed = False
valid = True

print("\nEnter Marks for 5 Subjects (0-100)")

for i in range(1, 6):
    marks = int(input("Enter marks for Subject " + str(i) + ": "))

    if marks < 0 or marks > 100:
        print("Invalid Marks! Enter marks between 0 and 100.")
        valid = False
        break

    marks_list.append(marks)

    if marks < 40:
        failed = True

if valid:

    total = sum(marks_list)
    percentage = (total / 500) * 100

    if failed:
        result = "FAIL"
        grade = "F"
        remark = "Failed in one or more subjects"

    elif percentage >= 90:
        result = "PASS"
        grade = "A+"
        remark = "Outstanding"

    elif percentage >= 80:
        result = "PASS"
        grade = "A"
        remark = "Excellent"

    elif percentage >= 70:
        result = "PASS"
        grade = "B"
        remark = "Very Good"

    elif percentage >= 60:
        result = "PASS"
        grade = "C"
        remark = "Good"

    elif percentage >= 50:
        result = "PASS"
        grade = "D"
        remark = "Satisfactory"

    else:
        result = "PASS"
        grade = "E"
        remark = "Pass"

    print("\n========================================")
    print("             STUDENT REPORT CARD")
    print("========================================")

    print("Student Name :", name)
    print("Roll Number  :", roll)

    print("----------------------------------------")

    print("Total Marks  :", total, "/ 500")
    print("Percentage   :", format(percentage, ".2f"), "%")
    print("Result       :", result)
    print("Grade        :", grade)
    print("Remarks      :", remark)

    print("========================================")

else:
    print("Program Ended.")
