# Route Optimizer & Distance Calculator

Calculate optimal routes and distances between multiple locations using advanced algorithms.

## Features

- 🗺️ **Route Optimization**: Find the shortest path through multiple locations
- 📏 **Distance Calculation**: Accurate geodesic distance measurements
- 🎯 **Multiple Algorithms**: Brute force and nearest neighbor optimization
- 📍 **Geocoding Support**: Use addresses or coordinates
- 🗺️ **Interactive Maps**: Visualize routes on interactive maps
- 📊 **Route Analysis**: Detailed distance breakdowns
- ⚡ **Fast Computation**: Efficient algorithms for quick results

## Installation

```bash
pip install -r requirements.txt
```

## Usage

### Run Demo

```bash
python route_optimizer.py
```

### Code Examples

#### Basic Route Optimization

```python
from route_optimizer import RouteOptimizer

# Create optimizer
optimizer = RouteOptimizer()

# Add locations
optimizer.add_location("New York, USA")
optimizer.add_location("Boston, USA")
optimizer.add_location("Philadelphia, USA")
optimizer.add_location("Washington DC, USA")

# Optimize route (nearest neighbor - fast)
route, distance = optimizer.optimize_route_nearest_neighbor(
    start_index=0,
    return_to_start=False
)

print(f"Optimized distance: {distance:.2f} km")

# Create map
optimizer.create_route_map(route, 'my_route.html')
```

#### Using Coordinates

```python
optimizer = RouteOptimizer()

# Add locations using coordinates
optimizer.add_location((40.7128, -74.0060))  # New York
optimizer.add_location((42.3601, -71.0589))  # Boston
optimizer.add_location((39.9526, -75.1652))  # Philadelphia

# Optimize
route, distance = optimizer.optimize_route_nearest_neighbor()
```

#### Brute Force Optimization

```python
# For small number of locations (<10), find the absolute best route
route, distance = optimizer.optimize_route_bruteforce(
    start_index=0,
    return_to_start=True  # Return to starting point
)
```

#### Distance Calculation Only

```python
optimizer = RouteOptimizer()

loc1 = {'lat': 40.7128, 'lon': -74.0060, 'name': 'New York'}
loc2 = {'lat': 51.5074, 'lon': -0.1278, 'name': 'London'}

distance = optimizer.calculate_distance(loc1, loc2)
print(f"Distance: {distance:.2f} km")
```

## Algorithms

### 1. Nearest Neighbor (Greedy)
- **Speed**: Fast ⚡
- **Accuracy**: Good (not guaranteed optimal)
- **Use for**: Any number of locations
- **Best for**: 5+ locations

```python
route, distance = optimizer.optimize_route_nearest_neighbor()
```

### 2. Brute Force
- **Speed**: Slow 🐌 (factorial time)
- **Accuracy**: Optimal ✅
- **Use for**: < 10 locations
- **Best for**: 3-8 locations when you need the absolute best route

```python
route, distance = optimizer.optimize_route_bruteforce()
```

## Distance Calculation Methods

### Geodesic Distance
- Most accurate
- Accounts for Earth's ellipsoidal shape
- Default method

### Great Circle Distance
- Faster computation
- Assumes Earth is a perfect sphere
- Good for quick estimates

```python
distance = optimizer.calculate_distance(loc1, loc2, method='great_circle')
```

## Map Features

The generated maps include:
- 🟢 **Green marker**: Start location
- 🔵 **Blue markers**: Waypoints
- 🔴 **Red marker**: End location
- **Numbers**: Visit order
- **Blue line**: Route path
- **Popups**: Location details and distances
- **Measurement tool**: Measure custom distances
- **Fullscreen mode**: Expand for better viewing

## Use Cases

### 1. Road Trip Planning
Plan the optimal route through multiple cities.

```python
optimizer.add_location("Los Angeles, CA")
optimizer.add_location("Las Vegas, NV")
optimizer.add_location("Grand Canyon, AZ")
optimizer.add_location("Phoenix, AZ")
```

### 2. Delivery Route Optimization
Optimize delivery routes to save time and fuel.

### 3. Tourist Itinerary
Visit multiple attractions in the most efficient order.

### 4. Sales Routes
Plan optimal routes for sales representatives.

### 5. Multi-City Trips
Find the best order to visit multiple cities.

## Route Details

The tool provides:
- Step-by-step directions
- Distance between each location
- Total route distance
- Coordinates for each stop
- Visual map representation

## Performance

| Locations | Brute Force | Nearest Neighbor |
|-----------|-------------|------------------|
| 3         | Instant     | Instant          |
| 5         | < 1 second  | Instant          |
| 8         | Few seconds | Instant          |
| 10        | ~1 minute   | Instant          |
| 15+       | Too slow ❌ | < 1 second ✅    |

## Tips

1. **Start location**: Choose your starting point wisely
2. **Return to start**: Use `return_to_start=True` for round trips
3. **Algorithm choice**:
   - < 10 locations: Use brute force for optimal route
   - 10+ locations: Use nearest neighbor
4. **API delays**: Add sleep() between geocoding calls
5. **Coordinates**: Use coordinates directly for faster processing

## Examples

### East Africa Road Trip

```python
optimizer = RouteOptimizer()

cities = [
    "Dar es Salaam, Tanzania",
    "Arusha, Tanzania",
    "Nairobi, Kenya",
    "Kampala, Uganda",
    "Kigali, Rwanda"
]

for city in cities:
    optimizer.add_location(city)
    time.sleep(1)

route, distance = optimizer.optimize_route_nearest_neighbor()
optimizer.print_route_details(route)
optimizer.create_route_map(route, 'east_africa_route.html')
```

### European Tour

```python
cities = [
    "Paris, France",
    "Brussels, Belgium",
    "Amsterdam, Netherlands",
    "Berlin, Germany",
    "Prague, Czech Republic"
]

for city in cities:
    optimizer.add_location(city)

route, distance = optimizer.optimize_route_bruteforce(
    start_index=0,
    return_to_start=True  # Return to Paris
)
```

## Limitations

- Geocoding requires internet connection
- Rate limited to ~1 request/second
- Brute force is exponential (slow for >10 locations)
- Doesn't account for roads (straight-line distance)
- No real-time traffic data

## Advanced Features

### Custom Route Order

```python
# Manually specify route order
custom_route = [0, 2, 1, 3]  # Visit in specific order
distance = optimizer.calculate_total_distance(custom_route)
optimizer.create_route_map(custom_route)
```

### Compare Routes

```python
# Compare original vs optimized
original = list(range(len(optimizer.locations)))
optimized, opt_dist = optimizer.optimize_route_nearest_neighbor()

original_dist = optimizer.calculate_total_distance(original)
savings = original_dist - opt_dist
print(f"Savings: {savings:.2f} km ({savings/original_dist*100:.1f}%)")
```
