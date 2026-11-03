Tuition_fee = int(input("Enter the tuition fee: "))
Lab_fee = int(input("Enter the lab fee: "))
Library_fee = int(input("Enter the library fee: "))
Exam_fee = int(input("Enter the exam fee: "))
Discount = int(input("Enter the discount: "))

print("Tuition Fee: ", Tuition_fee)
print("Lab Fee: ", Lab_fee)
print("Library Fee: ", Library_fee)
print("Exam Fee: ", Exam_fee)

Total_fee = Tuition_fee + Lab_fee + Library_fee + Exam_fee
print("Total Fee: ", Total_fee)

print("Discount: ", Discount)
print("Fee after discount: ", Total_fee - Discount)

Annual_fee = (Total_fee - Discount) * 2
print("Annual Fee: ", Annual_fee)

Monthly_fee = Annual_fee / 12
print("Monthly Installment: ", Monthly_fee)