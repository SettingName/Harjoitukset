import random
genNum = random.randint(1,10)
userGuess = int(input("Guess a number: "))
while userGuess != genNum:
    if userGuess > genNum:
        print("Too high")
    else:
         print("Too low")
    userGuess = int(input("Guess a number: "))
print("Correct")