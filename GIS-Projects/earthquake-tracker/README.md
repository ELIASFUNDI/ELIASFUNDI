# Earthquake Tracker & Visualizer

Real-time earthquake tracking and visualization using USGS earthquake data API.

## Features

- 🌍 Real-time earthquake data from USGS
- 📊 Interactive map visualization
- 📈 Statistical analysis
- 🎨 Color-coded by magnitude
- ⚠️ Tsunami warnings
- 📏 Measurement tools
- 🖥️ Fullscreen mode

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Basic Usage

```bash
python earthquake_tracker.py
```

### Custom Usage

```python
from earthquake_tracker import EarthquakeTracker

# Create tracker
tracker = EarthquakeTracker()

# Fetch earthquakes
# time_period: 'hour', 'day', 'week', 'month'
# min_magnitude: 'all', 'significant', '4.5', '2.5', '1.0'
tracker.fetch_earthquakes(time_period='day', min_magnitude='2.5')

# Get statistics
tracker.print_statistics()

# Create map
tracker.create_map('my_earthquake_map.html')
```

## Data Source

Data is fetched from the [USGS Earthquake API](https://earthquake.usgs.gov/earthquakes/feed/v1.0/geojson.php)

## Color Legend

- 🔴 **Dark Red**: Magnitude 7.0+ (Major)
- 🔴 **Red**: Magnitude 6.0-6.9 (Strong)
- 🟠 **Orange**: Magnitude 5.0-5.9 (Moderate)
- 🟡 **Yellow**: Magnitude 4.0-4.9 (Light)
- 🟢 **Light Green**: Magnitude 3.0-3.9 (Minor)
- 🟢 **Green**: Magnitude < 3.0 (Micro)

## Features Explained

### Circle Size
The size of each circle represents the earthquake's magnitude - larger circles indicate stronger earthquakes.

### Popup Information
Click on any earthquake marker to see:
- Magnitude
- Location
- Time
- Depth
- Coordinates
- Tsunami warning (if applicable)

### Statistics
The tool provides statistics including:
- Total earthquake count
- Magnitude range
- Average magnitude
- Breakdown by magnitude categories
