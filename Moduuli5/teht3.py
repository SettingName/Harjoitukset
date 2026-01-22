givenNum = int(input("Enter an integer: "))
totalDiv = 0
for num in range(1,givenNum+1):
    if givenNum % num == 0:
        totalDiv += 1
if totalDiv == 2:
    print(f"{givenNum} is a prime number.")
else:
    print(f"{givenNum} is not a prime number.")