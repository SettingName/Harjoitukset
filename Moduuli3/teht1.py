pituus = float(input("Enter the length of the zander in centimeters: "))
if pituus < 42:
    puuttuvat_sentit = 42 - pituus
    print("The zander does not meet the size limit.")
    print("Please release the fish back into the lake.")
    print(f"The fish was {puuttuvat_sentit:.1f} centimeters below the size limit.")
else:
    print("The zander meets the size limit.")