# Weather Map Application

Visualize real-time weather data on interactive maps using the OpenWeatherMap API.

## Features

- 🌤️ Real-time weather data
- 🌡️ Temperature visualization
- 💧 Humidity information
- 🎨 Color-coded by temperature
- 📍 Multiple cities support
- 🖥️ Interactive map interface
- 🆓 Demo mode (no API key needed)

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Demo Mode (No API Key Required)

```bash
python weather_map.py
```

This will generate a demo weather map with sample data for 10 major cities.

### Live Weather Data Mode

1. Get a free API key from [OpenWeatherMap](https://openweathermap.org/api)

2. Use the API in your code:

```python
from weather_map import WeatherMapper

# Initialize with your API key
mapper = WeatherMapper(api_key='YOUR_API_KEY_HERE')

# Choose cities
cities = ['London', 'Paris', 'Tokyo', 'New York', 'Sydney']

# Create weather map
mapper.create_weather_map(cities, 'my_weather_map.html')
```

## Color Legend

Temperature-based color coding:
- 🔴 **Dark Red**: 35°C+ (Very Hot)
- 🔴 **Red**: 25-34°C (Hot)
- 🟠 **Orange**: 15-24°C (Warm)
- 🔵 **Light Blue**: 5-14°C (Cool)
- 🔵 **Blue**: <5°C (Cold)

## Weather Icons

- ☀️ Hot (30°C+)
- ⛅ Warm (20-29°C)
- ☁️ Cool (10-19°C)
- ❄️ Cold (<10°C)

## API Information

The application uses the [OpenWeatherMap API](https://openweathermap.org/api):
- **Free tier**: 1,000 calls/day
- **Data**: Current weather, forecasts, historical data
- **Coverage**: Worldwide cities

## Features Explained

### Interactive Markers
Click on any city marker to see:
- Current temperature
- Humidity percentage
- Weather conditions

### Temperature Display
Each marker shows the temperature directly on the map with a color-coded circle.

### Fullscreen Mode
Use the fullscreen button to expand the map for better viewing.

## Customization

You can customize:
- Cities to display
- Temperature units (metric/imperial)
- Color scheme
- Marker sizes
- Map tiles
