print("=" * 40)
print("CYBER SECURITY PASSWORD STRENGTH ANALYZER")
print("=" * 40)

password = input("Enter your password: ")

if len(password) >= 8:
    print("Password Strength: STRONG")
else:
    print("Password Strength: WEAK")