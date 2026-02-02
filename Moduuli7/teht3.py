airports = {}

def airport_ask():
    while True:
        print("\nAirport Data Management\n1. Enter a new airport\n2. Fetch airport information\n3. Quit")
        optionNum = int(input("Please choose an option (1-3): "))

        if optionNum == 1:
            airportICAO = input("Enter the ICAO code: ")
            airportName = input("Enter the airport name: ")
            airports[airportICAO] = airportName
            print(f"Airport {airportName} with ICAO code {airportICAO} has been added.")

        elif optionNum == 2:
            airportICAO = input("Enter the ICAO code: ")
            if airports.__contains__(airportICAO):
                print(f"The airport with ICAO code {airportICAO} is {airports[airportICAO]}.")
            else:
                print(f"No airport found with ICAO code {airportICAO}.")
        elif optionNum == 3:
            print("Thank you for using the Airport Data Management system. Goodbye!")
            break

airport_ask()