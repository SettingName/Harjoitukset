def gallons_to_liters(gallons):
    while gallons >= 1:
        print(f"{gallons} American gallons is {(gallons * 3.785):.2f} liters.")
        gallons = float(input("Enter a volume in American gallons (negative value to quit): "))
    print("Program finished.")
gallons_to_liters(float(input("Enter a volume in American gallons (negative value to quit): ")))