import validators

user_input = input("Email: ").strip()

if validators.email(user_input):
    print("Valid")
else:
    print("Invalid")
