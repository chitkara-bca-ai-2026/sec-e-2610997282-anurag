
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


while True:

    print("\n==============================")
    print("     MATHEMATICS LEARNING TOOL")
    print("==============================")

    print("\nSelect an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        n = int(input("Enter a non-negative integer: "))

        if n >= 0:
            print("Factorial of", n, "is:", factorial(n))
        else:
            print("Please enter a non-negative number.")

    elif choice == "2":
        n = int(input("Enter number of terms: "))

        if n >= 0:
            series = []

            for i in range(n):
                series.append(fibonacci(i))

            print("Fibonacci series:", series)
        else:
            print("Please enter a non-negative number.")

    elif choice == "3":
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("Invalid choice! Please try again.")
