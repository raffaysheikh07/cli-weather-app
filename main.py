import os
import requests
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY") 

if not API_KEY:
    print("Error: OPENWEATHER_API_KEY not found in environment variables!")
    print("Make sure you created a .env file with OPENWEATHER_API_KEY=your_key")
    exit(1)

print("----Weather app----")
print("Enter 'Exit' anytime to exit from the app")
while True:
    cityName = input("Enter city: ").strip()
    if cityName.lower() == 'exit':
        print("Thank you for using the app")
        break

    if not cityName:
        print("City name cannot be empty. Please try again.\n")
        continue

    try:
        params = {
            "q": cityName,
            "appid": API_KEY,
            "units": "metric",
        }
        response = requests.get(
            "https://api.openweathermap.org/data/2.5/weather",
            params=params,
            timeout=10,
        )
        
        data = response.json()

        if response.status_code == 200:
            print(f"City: {data['name']}")
            print(f"Temperature: {data['main']['temp']}°C")
            print(f"Condition: {data['weather'][0]['description']}")
        else:
            error_msg = data.get("message", "Could not retrieve weather data")
            print(f"\nError ({response.status_code}): {error_msg.capitalize()}\n")
    except requests.RequestException as e:
        print(f"\nNetwork Error: Could not connect to weather service. ({e})\n")