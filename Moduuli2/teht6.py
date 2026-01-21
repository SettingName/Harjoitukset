import random
threeDigit = str(random.randint(0,9)) + str(random.randint(0,9)) + str(random.randint(0,9))
fourDigit = str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6)) + str(random.randint(1,6))
print("3-digit code: "+threeDigit)
print("4-digit code: "+fourDigit)