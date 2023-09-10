"""
Weather CLI using OpenWeatherMap API

This script fetches weather details for a given city using OpenWeatherMap's API.
"""

import requests

API_KEY = 'YOUR_OPENWEATHERMAP_API_KEY'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

def get_weather(city_name):
    complete_url = BASE_URL + "q=" + city_name + "&appid=" + API_KEY
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] == 200:
        main_data = data["main"]
        weather_data = data["weather"][0]
        print(f"Weather in {city_name}:")
        print(f"Temperature: {main_data['temp']}K")
        print(f"Humidity: {main_data['humidity']}%")
        print(f"Weather description: {weather_data['description']}")
    else:
        print("City not found!")

city = input("Enter city name: ")
get_weather(city)
