
username = input("Enter your username: ")
password = input("Enter your password: ")

print("\n========================================")
print("       PASSWORD VALIDATION REPORT")
print("========================================")

print("Username:", username)
print("Password:", "*" * len(password))

print("\n--- Validation Rules ---")

if len(password) >= 8:
    print("[PASS] Minimum 8 characters (" + str(len(password)) + " characters)")
    length = True
else:
    print("[FAIL] Minimum 8 characters")
    length = False

digit = False

for i in password:
    if i >= '0' and i <= '9':
        digit = True

if digit:
    print("[PASS] At least one digit")
else:
    print("[FAIL] At least one digit")

upper = False

for i in password:
    if i >= 'A' and i <= 'Z':
        upper = True

if upper:
    print("[PASS] At least one uppercase letter")
else:
    print("[FAIL] At least one uppercase letter")

print("\n--- Result ---")

if length and digit and upper:
    print("Password is VALID!")
    print("Account created successfully for", username + "!")
else:
    print("Password is INVALID")
    
print("========================================")
