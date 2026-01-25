number = input("Enter a number (or press Enter to quit): ")
largest = 0.0
smallest = 0.0 
while len(number) > 0:
        if smallest == 0.0:
             smallest = float(number)
             largest = float(number)
        if float(number) > largest:
            largest = float(number)
        elif (float(number) < smallest):
            smallest = float(number)
        number = input("Enter a number (or press Enter to quit): ")
print(f"Smallest number: {smallest}\nLargest number: {largest}")