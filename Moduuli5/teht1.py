import random
rolls = input("How many dice to roll: ")
sumOfRolls = 0
randomNum = random.randint(1,6)
for roll in range(int(rolls)):
    sumOfRolls += randomNum
print(f"Sum of the dice: {sumOfRolls}")