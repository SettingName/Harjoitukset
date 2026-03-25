import requests

userKunta = input("Enter municipality name: ")
pyyntö = f"https://api.openweathermap.org/data/2.5/weather?q={userKunta}&appid=bd5e378503939ddaee76f12ad7a97608&units=metric"

try: 
    vastaus = requests.get(pyyntö)
    if vastaus.status_code == 200:
        vastaus = vastaus.json()
        print(f"Weather: {vastaus["weather"][0]["description"]}")
        print(f"Temperature: {vastaus["main"]["temp"]} Celsius")

except requests.exceptions.RequestException as e:
    print("Haku no go.")