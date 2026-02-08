import mysql.connector

yhteys = mysql.connector.connect(
         host="127.0.0.1",
         port= 3306,
         database="flight_game",
         user="fake",
         password="fake",
         autocommit=True
         )

def getAirport(ident):
    sql = f"SELECT name, municipality FROM airport WHERE ident LIKE \"{ident}\";"
    kursori = yhteys.cursor()
    kursori.execute("", (ident.upper(),))
    tulos = kursori.fetchall()
    if kursori.rowcount > 0:
        for rivi in tulos:
            print(f"Airport name: {rivi[0]} \nLocation: {rivi[1]}")
    else:
        print(f"No airport found with ICAO code {ident}")

airportICAO = input("Enter the ICAO code of an airport: ")
getAirport(airportICAO)