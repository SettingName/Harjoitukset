import math
def calculate_unit_price(diameter, price):
    area = math.pi * (diameter/2/100)**2
    base_price = price / area
    return base_price

first_pizza_dia = int(input("Enter the diameter of the first pizza (cm): "))
first_pizza_pri = int(input("Enter the price of the first pizza (euros): "))
second_pizza_dia = int(input("Enter the diameter of the second pizza (cm): "))
second_pizza_pri = int(input("Enter the price of the second pizza (euros): "))

print(f"Unit price of the first pizza: {calculate_unit_price(first_pizza_dia, first_pizza_pri):.2f} euros/m²")
print(f"Unit price of the second pizza: {calculate_unit_price(second_pizza_dia, second_pizza_pri):.2f} euros/m²")
if calculate_unit_price(first_pizza_dia, first_pizza_pri) < calculate_unit_price(second_pizza_dia, second_pizza_pri):
    print("The first pizza provides better value for money.")
else:
    print("The second pizza provides better value for money.")
