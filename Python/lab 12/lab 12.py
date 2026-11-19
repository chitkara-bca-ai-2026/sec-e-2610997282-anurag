
sentence = input("Enter a sentence: ")

words = len(sentence.split())
vowels = 0
consonants = 0
digits = 0
spaces = 0
special = 0

for i in sentence:

    if i in "aeiouAEIOU":
        vowels += 1

    elif i.isalpha():
        consonants += 1

    elif i.isdigit():
        digits += 1

    elif i == " ":
        spaces += 1

    else:
        special += 1

letters = vowels + consonants

if letters > 0:
    percentage = (vowels / letters) * 100
else:
    percentage = 0

print("\n========================================")
print("         DOCUMENT ANALYSIS REPORT")
print("========================================")

print("Sentence:", sentence)
print("Total characters:", len(sentence))

print("\n--- Character Breakdown ---")

print("Words:", words)
print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Spaces:", spaces)
print("Special characters:", special)

print("\n--- Summary ---")

print("Total letters:", letters)
print("Vowel percentage:", round(percentage, 1), "%")

print("\n========================================")
print("Analysis Complete!")
print("========================================")
