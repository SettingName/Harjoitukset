from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

def isPrime(checkNum: int):
    totalDiv = 0
    for num in range(1, checkNum + 1):
        if checkNum % num == 0:
            totalDiv += 1
    if totalDiv == 2:
        return True
    else:
        return False
    
@app.route("/alkuluku/<int:num>")
def primeAPI(num):
    result = {
        "Number": num,
        "isPrime": isPrime(num)
    }
    return jsonify(result)

if __name__ == "__main__":
    app.run(port=3000)