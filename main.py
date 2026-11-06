password = input("Put your password : ")
is_number = False
is_capital = False

for password_test in password:
    if password_test in "0123456789":
        is_number = True
    if password_test in "QAZWSXEDCRFVTGBYHNUJMIKOLP":
        is_capital = True

if len(password) < 8:
    print("Too short")
if not is_number:
    print("No number")
if not is_capital:
    print("No capital letter")
if len(password) >= 8 and is_number and is_capital:
    print("Password is valid")