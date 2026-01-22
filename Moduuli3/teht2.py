luokka = input("Enter the cabin class (LUX, A, B, or C): ")
if luokka == "LUX":
    print("Upper-deck cabin with a balcony.")
elif luokka == "A":
    print("Above the car deck, equipped with a window.")
elif luokka == "B":
    print("Windowless cabin above the car deck.")
elif luokka == "C":
    print("Windowless cabin below the car deck.")
else:
    print("Invalid cabin class.")