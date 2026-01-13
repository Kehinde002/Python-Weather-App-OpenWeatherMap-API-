import requests
import os
from dotenv import load_dotenv

load_dotenv() # This loads the variables from .env
api_key = os.getenv("API_KEY") # This grabs your key securely


user_input = input("Enter City: ")

weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}"
)

# Convert to JSON first, then check
data = weather_data.json()

if data['cod'] == '404' or data['cod'] == 404:
    print("No City Found")
else:
    weather = data['weather'][0]['main']
    temp = round(data['main']['temp'])

    print(f"The weather in {user_input} is: {weather}")
    print(f"The temperature in {user_input} is: {temp}°F")
