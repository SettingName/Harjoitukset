from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def getConnection():
    return mysql.connector.connect(
        host = "localhost",
        user = "FakeName",
        password = "arrrr11111",
        database = "flight_game"
    )

@app.route("/kenttä/<string:icao>")
def airportAPI(icao):
    db = getConnection()
    cursor = db.cursor(dictionary = True)
    command = "SELECT ident, name, municipality FROM airport WHERE ident = %s"
    cursor.execute(command, (icao,))
    result = cursor.fetchone()

    if result:
        return jsonify({
            "ICAO": result["ident"],
            "Name": result["name"],
            "Municipality": result["municipality"]
        })
    
if __name__ == "__main__":
    app.run(port=3000)