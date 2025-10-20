import requests

API_KEY = "d11b9a26c88f910a22f6fd3b02241d9a"
CITY = "New York"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

if response.status_code == 200:
    temp = data["main"]["temp"]
    desc = data["weather"][0]["description"]
    print(f"Weather in {CITY}: {temp}°C, {desc}")
else:
    print("Error fetching weather data:", data)