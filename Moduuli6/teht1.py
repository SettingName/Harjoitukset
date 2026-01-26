import random
def roll_dice():
    rolled = random.randint(1,6)
    print(rolled)
    while rolled != 6:
        rolled = random.randint(1,6)
        print(rolled)
roll_dice()