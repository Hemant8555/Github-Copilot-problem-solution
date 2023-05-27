import pip._vendor.requests
import json
import sys

def fetch_weather(city):
    api_key = "2a3a7b92f0f4831a401a537083650887"  #
    base_url = "http://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"  
    }

    try:
        response = pip._vendor.requests.get(base_url, params=params)
        response.raise_for_status()  

        weather_data = response.json()

        
        temperature = weather_data["main"]["temp"]
        humidity = weather_data["main"]["humidity"]
        pressure = weather_data["main"]["pressure"]
        description = weather_data["weather"][0]["description"]

        return f"The current weather in {city} is {description} with a temperature of {temperature}°C.\nHumidity: {humidity}%\nPressure: {pressure} hPa"
    except pip._vendor.requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        sys.exit(1)
    except (KeyError, IndexError, json.JSONDecodeError):
        print("Error: Failed to parse weather data.")
        sys.exit(1)

def main():
    city = input("Please enter the city name:")

    weather = fetch_weather(city)
    print(weather)

if __name__ == "__main__":
    main()


