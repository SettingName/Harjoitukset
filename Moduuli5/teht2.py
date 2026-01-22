numList = []
userInput = input("Enter a number: ")
while userInput != "":
    numList.append(float(userInput))
    userInput = input("Enter a number: ")
numList.sort(reverse=True)
print("The greatest numbers in descending order:")
for luku in numList[:5]:
    print(luku)