"""
Weather Map Application
Visualize weather data on an interactive map using OpenWeatherMap API
"""

import requests
import folium
from folium import plugins
import json

class WeatherMapper:
    def __init__(self, api_key=None):
        """
        Initialize Weather Mapper

        api_key: OpenWeatherMap API key (optional for demo)
                Get free API key at: https://openweathermap.org/api
        """
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5/weather"
        self.forecast_url = "https://api.openweathermap.org/data/2.5/forecast"

    def get_weather(self, city_name):
        """Get current weather for a city"""
        if not self.api_key:
            return self._get_demo_weather(city_name)

        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric'
        }

        try:
            response = requests.get(self.base_url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error fetching weather for {city_name}: {e}")
            return None

    def _get_demo_weather(self, city_name):
        """Generate demo weather data for testing without API key"""
        demo_data = {
            "London": {"temp": 15, "humidity": 65, "description": "Cloudy", "lat": 51.5074, "lon": -0.1278},
            "New York": {"temp": 22, "humidity": 55, "description": "Partly Cloudy", "lat": 40.7128, "lon": -74.0060},
            "Tokyo": {"temp": 18, "humidity": 70, "description": "Rainy", "lat": 35.6762, "lon": 139.6503},
            "Dubai": {"temp": 35, "humidity": 45, "description": "Sunny", "lat": 25.2048, "lon": 55.2708},
            "Sydney": {"temp": 20, "humidity": 60, "description": "Clear", "lat": -33.8688, "lon": 151.2093},
            "Paris": {"temp": 16, "humidity": 68, "description": "Overcast", "lat": 48.8566, "lon": 2.3522},
            "Mumbai": {"temp": 30, "humidity": 75, "description": "Humid", "lat": 19.0760, "lon": 72.8777},
            "Singapore": {"temp": 28, "humidity": 80, "description": "Thunderstorm", "lat": 1.3521, "lon": 103.8198},
            "Cairo": {"temp": 32, "humidity": 30, "description": "Hot and Dry", "lat": 30.0444, "lon": 31.2357},
            "Moscow": {"temp": 8, "humidity": 50, "description": "Cold", "lat": 55.7558, "lon": 37.6173}
        }

        if city_name in demo_data:
            data = demo_data[city_name]
            return {
                "coord": {"lat": data["lat"], "lon": data["lon"]},
                "main": {"temp": data["temp"], "humidity": data["humidity"]},
                "weather": [{"description": data["description"]}],
                "name": city_name
            }
        return None

    def get_weather_icon(self, temp):
        """Get weather icon based on temperature"""
        if temp >= 30:
            return '☀️'
        elif temp >= 20:
            return '⛅'
        elif temp >= 10:
            return '☁️'
        else:
            return '❄️'

    def get_temp_color(self, temp):
        """Get color based on temperature"""
        if temp >= 35:
            return 'darkred'
        elif temp >= 25:
            return 'red'
        elif temp >= 15:
            return 'orange'
        elif temp >= 5:
            return 'lightblue'
        else:
            return 'blue'

    def create_weather_map(self, cities, filename='weather_map.html'):
        """Create an interactive weather map"""
        # Create map
        weather_map = folium.Map(
            location=[20, 0],
            zoom_start=2,
            tiles='OpenStreetMap'
        )

        for city in cities:
            weather_data = self.get_weather(city)

            if weather_data:
                lat = weather_data['coord']['lat']
                lon = weather_data['coord']['lon']
                temp = weather_data['main']['temp']
                humidity = weather_data['main']['humidity']
                description = weather_data['weather'][0]['description']
                city_name = weather_data['name']

                icon = self.get_weather_icon(temp)

                # Create popup
                popup_html = f"""
                <div style="font-family: Arial; width: 200px;">
                    <h3 style="margin: 0; color: #2c3e50;">
                        {icon} {city_name}
                    </h3>
                    <hr style="margin: 10px 0;">
                    <p style="margin: 5px 0;">
                        <b>🌡️ Temperature:</b> {temp}°C
                    </p>
                    <p style="margin: 5px 0;">
                        <b>💧 Humidity:</b> {humidity}%
                    </p>
                    <p style="margin: 5px 0;">
                        <b>🌤️ Condition:</b> {description.capitalize()}
                    </p>
                </div>
                """

                # Add marker
                folium.CircleMarker(
                    location=[lat, lon],
                    radius=15,
                    popup=folium.Popup(popup_html, max_width=250),
                    color=self.get_temp_color(temp),
                    fill=True,
                    fillColor=self.get_temp_color(temp),
                    fillOpacity=0.7,
                    weight=3
                ).add_to(weather_map)

                # Add label
                folium.Marker(
                    location=[lat, lon],
                    icon=folium.DivIcon(html=f"""
                        <div style="font-size: 12pt; color: black;
                                    background-color: white;
                                    padding: 5px;
                                    border-radius: 5px;
                                    border: 2px solid {self.get_temp_color(temp)};
                                    font-weight: bold;">
                            {icon} {temp}°C
                        </div>
                    """)
                ).add_to(weather_map)

        # Add fullscreen
        plugins.Fullscreen().add_to(weather_map)

        # Save map
        weather_map.save(filename)
        print(f"✅ Weather map saved as {filename}")

        return weather_map

def demo_weather_map():
    """Demo: Create a weather map without API key"""
    print("=" * 60)
    print("🌤️ WEATHER MAP GENERATOR")
    print("=" * 60)

    # Create weather mapper (demo mode - no API key needed)
    mapper = WeatherMapper()

    # Cities to display
    cities = [
        "London", "New York", "Tokyo", "Dubai", "Sydney",
        "Paris", "Mumbai", "Singapore", "Cairo", "Moscow"
    ]

    print(f"\n📍 Fetching weather for {len(cities)} cities...")
    mapper.create_weather_map(cities, 'weather_map.html')

    print("\n✅ Done! Open 'weather_map.html' to view the map.")
    print("\nColor Legend:")
    print("  🔴 Dark Red: 35°C+ (Very Hot)")
    print("  🔴 Red: 25-34°C (Hot)")
    print("  🟠 Orange: 15-24°C (Warm)")
    print("  🔵 Light Blue: 5-14°C (Cool)")
    print("  🔵 Blue: <5°C (Cold)")
    print("\nNote: Running in demo mode. For live weather data,")
    print("get a free API key from https://openweathermap.org/api")

def demo_with_api():
    """Demo: Create weather map with real API (requires API key)"""
    print("\n" + "=" * 60)
    print("To use live weather data:")
    print("=" * 60)
    print("1. Get free API key from: https://openweathermap.org/api")
    print("2. Use the following code:")
    print()
    print("    mapper = WeatherMapper(api_key='YOUR_API_KEY')")
    print("    cities = ['London', 'Paris', 'Tokyo']")
    print("    mapper.create_weather_map(cities, 'live_weather.html')")
    print()

if __name__ == "__main__":
    demo_weather_map()
    demo_with_api()
