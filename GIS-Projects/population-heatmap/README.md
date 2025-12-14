# Population Density Heatmap Generator

Visualize population density across the globe using interactive heatmaps.

## Features

- 🔥 **Heatmap Visualization**: Color-coded population density
- 🌍 **Global Coverage**: Major cities worldwide
- 📊 **Statistical Analysis**: Population statistics
- ⭕ **Choropleth Maps**: Circle-based population visualization
- 📈 **Graduated Symbols**: Size represents population
- 🖥️ **Interactive Maps**: Zoom, pan, and explore

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run Demo

```bash
python population_heatmap.py
```

This generates two maps:
- `population_heatmap.html` - Density heatmap
- `choropleth_population.html` - Circle size visualization

### Code Examples

#### Basic Heatmap

```python
from population_heatmap import PopulationHeatmap

# Create generator
generator = PopulationHeatmap()

# Load demo data
generator.load_demo_data()

# Generate heatmap
generator.create_heatmap('my_heatmap.html')
```

#### Custom Data

```python
# Custom population data: [lat, lon, population_in_millions]
custom_data = [
    [40.7128, -74.0060, 18.8],  # New York
    [51.5074, -0.1278, 9.0],     # London
    [35.6762, 139.6503, 37.4],   # Tokyo
]

generator = PopulationHeatmap()
generator.load_custom_data(custom_data)
generator.create_heatmap('custom_heatmap.html')
```

#### Get Statistics

```python
generator.load_demo_data()
stats = generator.get_statistics()

print(f"Total cities: {stats['total_cities']}")
print(f"Mega cities (10M+): {stats['mega_cities']}")
print(f"Largest city: {stats['max_population']}M")
```

## Map Types

### 1. Heatmap
Shows population density as a smooth gradient:
- Blue: Low density
- Green: Medium-low density
- Yellow: Medium density
- Orange: High density
- Red: Very high density

### 2. Choropleth Map
Shows population using graduated circles:
- Circle size = population
- Color intensity = population density
- Click circles for exact population

## Data Format

Population data should be in the format:
```python
[latitude, longitude, population_in_millions]
```

Example:
```python
[40.7128, -74.0060, 18.8]  # New York: 18.8 million
```

## Included Cities

The demo includes 45+ major cities from:
- **Asia**: Tokyo, Delhi, Shanghai, Mumbai, etc.
- **Europe**: London, Paris, Moscow, Berlin, etc.
- **Americas**: New York, São Paulo, Mexico City, etc.
- **Africa**: Cairo, Lagos, Nairobi, Dar es Salaam, etc.
- **Oceania**: Sydney, Melbourne

## Customization

### Heatmap Parameters

Adjust heatmap appearance:
```python
plugins.HeatMap(
    data,
    min_opacity=0.2,    # Minimum opacity
    max_zoom=13,        # Max zoom level
    radius=25,          # Point radius
    blur=35,            # Blur amount
    gradient={...}      # Color gradient
)
```

### Color Gradients

Custom color schemes:
```python
gradient = {
    0.0: 'navy',
    0.5: 'yellow',
    1.0: 'red'
}
```

## Use Cases

### 1. Urban Planning
Identify population centers and plan infrastructure.

### 2. Market Analysis
Find high-density areas for business expansion.

### 3. Resource Allocation
Distribute resources based on population needs.

### 4. Research & Education
Visualize global population patterns.

### 5. Emergency Response
Identify high-risk areas for disaster planning.

## Statistics

The tool provides:
- Total city count
- Total population sum
- Average population
- Population range (min/max)
- Mega city count (10M+)

## Tips

1. **Zoom in**: Details appear at higher zoom levels
2. **Click markers**: See exact population figures
3. **Fullscreen**: Use fullscreen for better viewing
4. **Compare maps**: View both heatmap and choropleth for insights

## Data Sources

Demo data is based on:
- UN World Urbanization Prospects
- City-proper populations
- Metropolitan area estimates

## Limitations

- Demo data is approximate
- Population figures are in millions
- Data represents major cities only
- Not real-time (static snapshot)

## Advanced Usage

### Add Your Own Cities

```python
generator = PopulationHeatmap()

# Start with demo data
generator.load_demo_data()

# Add custom cities
generator.population_data.extend([
    [lat1, lon1, pop1],
    [lat2, lon2, pop2],
])

generator.create_heatmap('extended_map.html')
```

### Filter by Population

```python
# Only show mega cities (10M+)
mega_cities = [
    data for data in generator.population_data
    if data[2] >= 10
]

generator.load_custom_data(mega_cities)
generator.create_heatmap('mega_cities.html')
```
