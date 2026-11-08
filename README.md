##CLI Weather App

A small interactive command line app, written in Python, that shows the current weather for any city. It uses the OpenWeatherMap API and the requests library.

##Features
Current weather: shows the city name, the temperature in °C, and a short description of the weather.
Interactive loop: search as many cities as you like. Type exit (any capitalization) to quit.
Input checks: empty input is rejected with a clear message instead of an API call.
Error handling: invalid cities, API errors, and network problems print a message instead of crashing the app. Requests time out after 10 seconds.
Safe API key handling: the key is read from a .env file with python-dotenv, so it never appears in the source code. The app stops with a helpful message if the key is missing.
##Example
----Weather app----
Enter 'Exit' anytime to exit from the app
Enter city: Lahore
City: Lahore
Temperature: 24.3°C
Condition: haze
Enter city: exit
Thank you for using the app

(The values above are only an example. Real output depends on the current weather.)

##Prerequisites
Python 3.8 or newer
A free API key from OpenWeatherMap. New keys can take a while to activate after you sign up.
Installation
Clone the repository
   git clone https://github.com/raffaysheikh07/cli-weather-app.git
   cd cli-weather-app
Create and activate a virtual environment (recommended) Windows:
   python -m venv venv
   venv\Scripts\activate

##macOS / Linux:

   python3 -m venv venv
   source venv/bin/activate
Install the dependencies
   pip install -r requirements.txt
Configuration
Copy the example file to create your own .env file: Windows:
   copy .env.example .env

##macOS / Linux:

   cp .env.example .env
Open .env and replace the placeholder with your real key:
   OPENWEATHER_API_KEY=your_key_here

The .env file is listed in .gitignore, so it is not uploaded to GitHub. Never share your real key or commit it.

##Usage

Run the app:

python main.py

Type a city name and press Enter. Type exit when you want to quit.

##Project structure
cli-weather-app/
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
Troubleshooting
Problem	What to do
OPENWEATHER_API_KEY not found	Check that the .env file exists in the same folder as main.py and that the variable name is spelled exactly OPENWEATHER_API_KEY.
Invalid API key error	Copy the key again from your OpenWeatherMap account. A brand new key may need some time before it works.
City not found	Check the spelling, or try the city name in English.
Connection error	Check your internet connection and try again.
Built with
Python
requests
python-dotenv
OpenWeatherMap API
Ideas for future improvements
Show humidity and wind speed
Add a 5-day forecast
Let the user choose Celsius or Fahrenheit
Split the code into functions and add tests
Author

Abdul Raffay, GitHub
