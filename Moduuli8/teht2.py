import mysql.connector
from collections import Counter

xd = mysql.connector.connect(
         host="127.0.0.1",
         port= 3306,
         database="flight_game",
         user="fake",
         password="fake",
         autocommit=True
         )

def get_airports_by_country(country_code):
    sql = f"SELECT type FROM airport WHERE iso_country LIKE \"{country_code}\" AND type LIKE \"%port%\" ORDER BY type desc"
    valitse = xd.cursor()
    valitse.execute(sql)
    valinnat = valitse.fetchall()
    return valinnat

def run_country_program():
    country = input("Enter the country code (e.g., FI for Finland): ")
    country.upper()
    valinnat = get_airports_by_country(country)
    if valinnat:  
        types = [row[0] for row in valinnat]
        counts = Counter(types)
        print(f"Airports in {country}:") 
        for type, num in counts.items(): print(f"{num} {type} airports")
    else:
        print((f"No airports found for country code \'{country}\'"))
run_country_program()