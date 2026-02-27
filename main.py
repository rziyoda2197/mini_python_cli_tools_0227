import string

password = input("Enter password: ")

score = 0

if len(password) >= 8:
    score += 1
if any(c.islower() for c in password):
    score += 1
if any(c.isupper() for c in password):
    score += 1
if any(c.isdigit() for c in password):
    score += 1
if any(c in string.punctuation for c in password):
    score += 1

if score <= 2:
    print("Weak password")
elif score == 3 or score == 4:
    print("Medium password")
else:
    print("Strong password")
