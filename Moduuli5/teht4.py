cityNames = []
for city in range(5):
    cityName = input("Enter the name of a city: ")
    cityNames.append(cityName)
print("\n")
print("The cities you entered:")
for city in cityNames:
    print(city)