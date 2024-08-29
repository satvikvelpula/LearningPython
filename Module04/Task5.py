print("Login to your account.")
tries = 5

while True:
    username = str(input("Enter your username: "))
    password = str(input("Enter your password: "))

    if username == "python" and password == "rules":
        print("Welcome Python!")
        break
    else: print("Invalid username or password!")
    tries -= 1

    if tries == 0:
        print("Access denied!")
        break
