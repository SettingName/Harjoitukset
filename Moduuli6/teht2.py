import random
def roll_dice(max_roll):
    rolled = random.randint(1,max_roll)
    print(rolled)
    while rolled != max_roll:
        rolled = random.randint(1,max_roll)
        print(rolled)
roll_dice(int(input()))