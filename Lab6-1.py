text = input("Enter a string: ")

vowels = "aeiouAEIOU"
vowel_count = 0
consonant_count = 0
space_count = 0
lowercase_count = 0

for ch in text:
    if ch in vowels:
        vowel_count += 1
    elif ch.isalpha():
        consonant_count += 1
    if ch == " ":
        space_count += 1
    if ch.islower():
        lowercase_count += 1

print("Number of Vowels:", vowel_count)
print("Number of Consonants:", consonant_count)
print("Number of Spaces:", space_count)
print("Number of Lowercase Letters:", lowercase_count)