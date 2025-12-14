# Interactive Map Visualizer

Create beautiful, interactive maps with custom markers, circles, and heatmaps using Python.

## Features

- 🗺️ Interactive web-based maps
- 📍 Custom markers with popups
- ⭕ Circle overlays with radius
- 🔥 Heatmap visualization
- 🖼️ Minimap navigation
- 🖥️ Fullscreen mode

## Installation

```bash
pip install -r requirements.txt
```

## Usage

```python
from interactive_map import InteractiveMapGenerator

# Create a new map
map_gen = InteractiveMapGenerator(center_lat=0, center_lon=0, zoom_start=2)

# Add markers
map_gen.add_marker(40.7128, -74.0060, "New York City", icon_color='blue')

# Add circles
map_gen.add_circle(51.5074, -0.1278, 50000, "London - 50km radius", color='red')

# Save the map
map_gen.save_map('my_map.html')
```

## Run Demo

```bash
python interactive_map.py
```

This will generate two demo maps:
- `world_cities_map.html` - Major cities around the world
- `tanzania_map.html` - Cities in Tanzania

## Customization

You can customize:
- Map center coordinates
- Zoom level
- Marker colors and icons
- Circle radius and colors
- Map tiles (OpenStreetMap, Stamen Terrain, etc.)
