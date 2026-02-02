given_month = input("Enter the number of a month (1-12): ")
month_list = (1,2,3,4,5,6,7,8,9,10,11,12)
def get_season(month):
    if month == 12 or month == 1 or month == 2:
        return "winter"
    elif month == 3 or month == 4 or month == 5:
        return "spring"
    elif month == 6 or month == 7 or month == 8:
        return "summer"
    elif month == 9 or month == 10 or month == 11:
        return "autumn"
if month_list.__contains__(int(given_month)) == True:
    print(f"You entered: {given_month}\nThe season is {get_season(int(given_month))}.")
else:
    print(f"You entered: {given_month}\nPlease enter a number between 1 and 12.")