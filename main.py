import requests

import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  # Change units as needed (metric, imperial, etc.)
    }

    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        weather_data = response.json()
        print(f"Weather in {city}:")
        print(f"Temperature: {weather_data['main']['temp']}°C")
        print(f"Weather: {weather_data['weather'][0]['description']}")
    else:
        print("Failed to fetch weather data.")

api_key = "48060542d0ead16163cd61cde9ae920c"  # Replace with your actual API key
city_name = input("Enter city name: ")
get_weather(city_name, api_key)