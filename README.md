# CLI Weather App

A lightweight, interactive Python Command Line Interface (CLI) application that fetches real-time weather reports for any city using the **OpenWeatherMap API** and the `requests` library.

---

## Features

- **Real-Time Data:** Fetches current temperature (°C), weather conditions, and humidity.
- **Interactive CLI:** Search multiple cities continuously in a loop until you exit.
- **Error Handling:** Gracefully handles invalid city inputs and API errors.
- **Secure Key Management:** Uses `python-dotenv` to keep API keys safely isolated from source code.

---

## Prerequisites

- Python 3.8+
- An API Key from [OpenWeatherMap](https://openweathermap.org/api) (Free Tier)

---

## Installation & Setup

### 1. Clone the Repository
```bash
git clone [https://github.com/raffaysheikh07/cli-weather-app.git](https://github.com/raffaysheikh07/cli-weather-app.git)
cd cli-weather-app
