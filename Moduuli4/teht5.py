userName = input("Enter username: ")
userPassword = input("Enter password: ")
correctU = "python"
correctP = "rules"
guesses = 0
while 0 <= guesses <= 5:
    guesses += 1
    if userName == correctU and userPassword == correctP:
         print("Welcome")
         guesses -= 99
    elif guesses >= 5:
            print("Access denied")
            break
    else:
         print("Incorrect username or password. Please try again.")
         userName = input("Enter username: ")
         userPassword = input("Enter password: ")