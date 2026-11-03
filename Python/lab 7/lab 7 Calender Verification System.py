print("="*30)
print(" "*5 + "CALENDAR VERIFICATION SYSTEM" + " "*5)
print("="*30)
while True:
    year = int(input("Enter year: "))
    print("\n")
    print("-" * 30)
    if year <= 0:
        print("Invalid year, year must be greater than 0.")
        break

    if year % 400 == 0:
        print("LEAP YEAR")
        print("Days in Year: 366")
        print("Days in February: 29")
        print("Century Year divisible by 400 is a LEAP YEAR")

    elif year % 100 == 0:
        print("COMMON YEAR")
        print("Days in Year: 365")
        print("Days in February: 28")
        print("Century Year divisible by 100 but not by 400 is a COMMON YEAR")
    elif year % 4 == 0:
        print("LEAP YEAR")
        print("Days in Year: 366")
        print("Days in February: 29")
        print("Year divisible by 4 but not by 100 is a LEAP YEAR")

    else:
        print("COMMON YEAR")
        print("Days in Year: 365")
        print("Days in February: 28")
        print("Year not divisible by 4 is a COMMON YEAR")

    print("-" * 30)