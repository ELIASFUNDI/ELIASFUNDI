"""
Interactive World Map Visualizer
A tool to create interactive maps with custom markers and information
"""

import folium
from folium import plugins
import json

class InteractiveMapGenerator:
    def __init__(self, center_lat=0, center_lon=0, zoom_start=2):
        """Initialize the map with center coordinates and zoom level"""
        self.map = folium.Map(
            location=[center_lat, center_lon],
            zoom_start=zoom_start,
            tiles='OpenStreetMap'
        )

    def add_marker(self, lat, lon, popup_text, icon_color='red', icon='info-sign'):
        """Add a marker to the map"""
        folium.Marker(
            location=[lat, lon],
            popup=popup_text,
            icon=folium.Icon(color=icon_color, icon=icon)
        ).add_to(self.map)

    def add_circle(self, lat, lon, radius, popup_text, color='blue'):
        """Add a circle to the map"""
        folium.Circle(
            location=[lat, lon],
            radius=radius,
            popup=popup_text,
            color=color,
            fill=True,
            fillColor=color
        ).add_to(self.map)

    def add_heatmap(self, locations):
        """Add a heatmap layer to the map"""
        plugins.HeatMap(locations).add_to(self.map)

    def add_minimap(self):
        """Add a minimap to the map"""
        minimap = plugins.MiniMap()
        self.map.add_child(minimap)

    def add_fullscreen(self):
        """Add fullscreen button to the map"""
        plugins.Fullscreen().add_to(self.map)

    def save_map(self, filename='interactive_map.html'):
        """Save the map to an HTML file"""
        self.map.save(filename)
        print(f"Map saved as {filename}")

    def show_map(self):
        """Display the map"""
        return self.map

def demo_world_cities():
    """Demo: Create a map with world's major cities"""
    world_cities = [
        {"name": "New York", "lat": 40.7128, "lon": -74.0060, "info": "The Big Apple"},
        {"name": "London", "lat": 51.5074, "lon": -0.1278, "info": "Capital of England"},
        {"name": "Tokyo", "lat": 35.6762, "lon": 139.6503, "info": "Japan's capital"},
        {"name": "Paris", "lat": 48.8566, "lon": 2.3522, "info": "City of Light"},
        {"name": "Sydney", "lat": -33.8688, "lon": 151.2093, "info": "Australia's harbor city"},
        {"name": "Dubai", "lat": 25.2048, "lon": 55.2708, "info": "City of gold"},
        {"name": "Singapore", "lat": 1.3521, "lon": 103.8198, "info": "Lion City"},
        {"name": "Cairo", "lat": 30.0444, "lon": 31.2357, "info": "Land of Pyramids"},
        {"name": "Rio de Janeiro", "lat": -22.9068, "lon": -43.1729, "info": "Marvelous City"},
        {"name": "Mumbai", "lat": 19.0760, "lon": 72.8777, "info": "India's financial capital"}
    ]

    # Create map centered on the world
    map_gen = InteractiveMapGenerator(center_lat=20, center_lon=0, zoom_start=2)

    # Add markers for each city
    for city in world_cities:
        map_gen.add_marker(
            city['lat'],
            city['lon'],
            f"<b>{city['name']}</b><br>{city['info']}",
            icon_color='blue'
        )

    # Add minimap and fullscreen
    map_gen.add_minimap()
    map_gen.add_fullscreen()

    # Save the map
    map_gen.save_map('world_cities_map.html')

def demo_custom_locations():
    """Demo: Create a map with custom locations"""
    # Create map centered on Africa
    map_gen = InteractiveMapGenerator(center_lat=-6.369028, center_lon=34.888822, zoom_start=6)

    # Add some locations in Tanzania
    locations = [
        {"name": "Dar es Salaam", "lat": -6.7924, "lon": 39.2083, "info": "Largest city"},
        {"name": "Dodoma", "lat": -6.1630, "lon": 35.7516, "info": "Capital city"},
        {"name": "Arusha", "lat": -3.3869, "lon": 36.6830, "info": "Safari capital"},
        {"name": "Mwanza", "lat": -2.5164, "lon": 32.9175, "info": "Lake Victoria city"},
        {"name": "Zanzibar", "lat": -6.1659, "lon": 39.2026, "info": "Spice Island"}
    ]

    for loc in locations:
        map_gen.add_marker(
            loc['lat'],
            loc['lon'],
            f"<b>{loc['name']}</b><br>{loc['info']}",
            icon_color='red',
            icon='star'
        )

    map_gen.add_fullscreen()
    map_gen.save_map('tanzania_map.html')

if __name__ == "__main__":
    print("=" * 50)
    print("Interactive Map Generator")
    print("=" * 50)

    print("\nGenerating World Cities Map...")
    demo_world_cities()

    print("\nGenerating Tanzania Map...")
    demo_custom_locations()

    print("\n✅ Maps generated successfully!")
    print("Open the HTML files in your browser to view them.")
