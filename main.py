password = input("Enter your password: ")
is_number = False
is_capital = False
is_symbol = False
is_lowercase_letter = False

for password_test in password:
    if password_test in "0123456789":
        is_number = True
    if password_test in "QAZWSXEDCRFVTGBYHNUJMIKOLP":
        is_capital = True
    if password_test in "!@#$%^&*~-_=+?.":
        is_symbol = True
    if password_test in "qazwsxedcrfvtgbyhnujmikolp":
        is_lowercase_letter = True

len_size = len(password)
if len_size < 8:
    print(f"Too short: {len_size}/8")
if is_number == False:
    print("No number")
if is_capital == False:
    print("No capital letter")
if is_symbol == False:
    print("No symbol")
if is_lowercase_letter == False:
    print("No lowercase letter")
if len_size >= 8 and is_number and is_capital and is_symbol and is_lowercase_letter:
    print("Password is valid")
