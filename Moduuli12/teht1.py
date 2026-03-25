import requests

pyyntö = "https://api.chucknorris.io/jokes/random"

try:
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        vastaus = vastaus.json()
        print(vastaus["value"])

except requests.exceptions.RequestException as e:
    print("Haku no go.")