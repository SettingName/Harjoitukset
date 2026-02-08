import mysql.connector
from geopy.distance import geodesic

xd = mysql.connector.connect(
         host="127.0.0.1",
         port= 3306,
         database="flight_game",
         user="name",
         password="fake",
         autocommit=True
         )

def get_airport_coordinates(ident):
    ident = ident.upper()

    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    valitse = xd.cursor()
    valitse.execute(sql, (ident,))
    valitut = valitse.fetchone()

    if valitut:
        return (valitut[0], valitut[1])
    else:
        return None

def run_airport_distance():
    ident1 = input("Enter the ICAO code of the first airport: ").upper()
    ident2 = input("Enter the ICAO code of the second airport: ").upper()
    
    coords1 = get_airport_coordinates(ident1)
    coords2 = get_airport_coordinates(ident2)
    if coords1 and coords2:
        distance = geodesic(coords1, coords2).kilometers
        print(f"Distance between {ident1} and {ident2} is: {distance:.2f} kilometers")
    elif coords1:
        print(f"Airport with ICAO code {ident2} not found in the database.")
    else:
        print(f"Airport with ICAO code {ident1} not found in the database.")
run_airport_distance()