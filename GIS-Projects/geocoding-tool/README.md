# Geocoding & Reverse Geocoding Tool

Convert addresses to coordinates and coordinates to addresses using Python.

## Features

- 📍 **Geocoding**: Convert addresses to coordinates
- 🔄 **Reverse Geocoding**: Convert coordinates to addresses
- 📏 **Distance Calculator**: Calculate distances between locations
- 🗺️ **Map Visualization**: Display locations on interactive maps
- 📦 **Batch Processing**: Process multiple addresses at once
- 🎯 **Interactive Mode**: Command-line interface for easy use

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Demo Mode

```bash
python geocoding_tool.py
```

### Code Examples

#### Geocoding (Address → Coordinates)

```python
from geocoding_tool import GeocodingTool

geocoder = GeocodingTool()

# Single address
result = geocoder.geocode("Times Square, New York")
print(f"Latitude: {result['latitude']}")
print(f"Longitude: {result['longitude']}")

# Multiple addresses
addresses = ["Paris, France", "Tokyo, Japan", "Sydney, Australia"]
results = geocoder.batch_geocode(addresses)
```

#### Reverse Geocoding (Coordinates → Address)

```python
# Get address from coordinates
result = geocoder.reverse_geocode(40.7128, -74.0060)
print(result['address'])
```

#### Distance Calculation

```python
# Distance between two addresses
distance = geocoder.calculate_distance(
    "New York, USA",
    "London, UK"
)

# Distance between coordinates
distance = geocoder.calculate_distance(
    (40.7128, -74.0060),  # New York
    (51.5074, -0.1278)     # London
)
```

#### Create Map

```python
# Create a map with multiple locations
locations = geocoder.batch_geocode([
    "Eiffel Tower, Paris",
    "Colosseum, Rome",
    "Big Ben, London"
])

geocoder.create_map(locations, 'my_map.html')
```

### Interactive Mode

Uncomment the last line in `geocoding_tool.py`:

```python
if __name__ == "__main__":
    # demo_geocoding()
    interactive_mode()  # Uncomment this
```

Then run:
```bash
python geocoding_tool.py
```

## API Information

This tool uses **Nominatim** (OpenStreetMap's geocoding service):
- Free to use
- No API key required
- Please be respectful: 1 request per second
- Global coverage

## Use Cases

### 1. Address Validation
Verify and standardize addresses in your database.

### 2. Location Mapping
Plot customer locations, delivery routes, or store locations.

### 3. Distance Calculation
Calculate shipping distances, travel distances, or proximity.

### 4. Data Enrichment
Add coordinates to address datasets.

### 5. Route Planning
Plan routes between multiple locations.

## Examples

### Find Famous Landmarks

```python
geocoder = GeocodingTool()

landmarks = [
    "Statue of Liberty, New York",
    "Great Pyramid of Giza, Egypt",
    "Taj Mahal, India",
    "Machu Picchu, Peru"
]

locations = geocoder.batch_geocode(landmarks)
geocoder.create_map(locations, 'world_landmarks.html')
```

### Find What's at Coordinates

```python
# What's at these coordinates?
geocoder.reverse_geocode(-6.7924, 39.2083)
# Output: Dar es Salaam, Tanzania
```

### Calculate Road Trip Distance

```python
route = [
    "Los Angeles, CA",
    "Las Vegas, NV",
    "Grand Canyon, AZ",
    "Phoenix, AZ"
]

total_distance = 0
for i in range(len(route) - 1):
    distance = geocoder.calculate_distance(route[i], route[i+1])
    total_distance += distance
    time.sleep(1)

print(f"Total distance: {total_distance:.2f} km")
```

## Limitations

- Rate limited to ~1 request per second
- Results depend on OpenStreetMap data quality
- Some remote locations may not have detailed data
- Requires internet connection

## Tips

1. **Be specific**: Include city, state, and country for better accuracy
2. **Use official names**: "NYC" might work, but "New York City, USA" is better
3. **Wait between requests**: Add delays when processing multiple addresses
4. **Check results**: Always verify the returned address matches your input

## Error Handling

The tool handles common errors:
- Address not found
- Network timeouts
- Invalid coordinates
- Service unavailable

Always check if the result is `None` before using it.
