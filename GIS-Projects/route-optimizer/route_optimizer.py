"""
Route Optimizer and Distance Calculator
Calculate optimal routes and distances between multiple locations
"""

from geopy.distance import geodesic, great_circle
from geopy.geocoders import Nominatim
import folium
from folium import plugins
import itertools
import time

class RouteOptimizer:
    def __init__(self):
        """Initialize Route Optimizer"""
        self.geolocator = Nominatim(user_agent="route_optimizer_app")
        self.locations = []

    def add_location(self, location):
        """
        Add a location to the route

        location: Can be (lat, lon) tuple or address string
        """
        if isinstance(location, str):
            # Geocode the address
            try:
                geo_location = self.geolocator.geocode(location, timeout=10)
                if geo_location:
                    self.locations.append({
                        'name': location,
                        'lat': geo_location.latitude,
                        'lon': geo_location.longitude
                    })
                    print(f"✅ Added: {location}")
                else:
                    print(f"❌ Could not find: {location}")
            except Exception as e:
                print(f"❌ Error: {e}")
        elif isinstance(location, tuple) and len(location) == 2:
            # Direct coordinates
            self.locations.append({
                'name': f"Location {len(self.locations) + 1}",
                'lat': location[0],
                'lon': location[1]
            })
            print(f"✅ Added: ({location[0]}, {location[1]})")

    def calculate_distance(self, loc1, loc2, method='geodesic'):
        """
        Calculate distance between two locations

        method: 'geodesic' (more accurate) or 'great_circle' (faster)
        Returns: Distance in kilometers
        """
        point1 = (loc1['lat'], loc1['lon'])
        point2 = (loc2['lat'], loc2['lon'])

        if method == 'geodesic':
            distance = geodesic(point1, point2).kilometers
        else:
            distance = great_circle(point1, point2).kilometers

        return distance

    def calculate_total_distance(self, route_order=None):
        """
        Calculate total distance for a route

        route_order: List of indices specifying the order
        """
        if not self.locations:
            return 0

        if route_order is None:
            route_order = list(range(len(self.locations)))

        total_distance = 0
        for i in range(len(route_order) - 1):
            loc1 = self.locations[route_order[i]]
            loc2 = self.locations[route_order[i + 1]]
            distance = self.calculate_distance(loc1, loc2)
            total_distance += distance

        return total_distance

    def optimize_route_bruteforce(self, start_index=0, return_to_start=False):
        """
        Optimize route using brute force (for small number of locations)

        start_index: Index of starting location
        return_to_start: Whether to return to starting point
        """
        if len(self.locations) > 10:
            print("⚠️ Warning: Brute force optimization is slow for >10 locations")
            print("   Consider using nearest neighbor instead")

        # Get all other locations
        other_indices = [i for i in range(len(self.locations)) if i != start_index]

        # Try all permutations
        best_distance = float('inf')
        best_route = None

        print(f"🔍 Testing {len(list(itertools.permutations(other_indices)))} possible routes...")

        for perm in itertools.permutations(other_indices):
            route = [start_index] + list(perm)
            if return_to_start:
                route.append(start_index)

            distance = self.calculate_total_distance(route)

            if distance < best_distance:
                best_distance = distance
                best_route = route

        return best_route, best_distance

    def optimize_route_nearest_neighbor(self, start_index=0, return_to_start=False):
        """
        Optimize route using nearest neighbor algorithm (greedy)

        Faster but not guaranteed to be optimal
        """
        route = [start_index]
        unvisited = set(range(len(self.locations))) - {start_index}

        current = start_index

        while unvisited:
            nearest = min(
                unvisited,
                key=lambda x: self.calculate_distance(
                    self.locations[current],
                    self.locations[x]
                )
            )
            route.append(nearest)
            unvisited.remove(nearest)
            current = nearest

        if return_to_start:
            route.append(start_index)

        total_distance = self.calculate_total_distance(route)

        return route, total_distance

    def create_route_map(self, route_order=None, filename='route_map.html'):
        """Create an interactive map showing the route"""
        if not self.locations:
            print("No locations to map")
            return

        if route_order is None:
            route_order = list(range(len(self.locations)))

        # Calculate center
        avg_lat = sum(loc['lat'] for loc in self.locations) / len(self.locations)
        avg_lon = sum(loc['lon'] for loc in self.locations) / len(self.locations)

        # Create map
        route_map = folium.Map(
            location=[avg_lat, avg_lon],
            zoom_start=5
        )

        # Draw route lines
        route_coords = []
        for idx in route_order:
            loc = self.locations[idx]
            route_coords.append([loc['lat'], loc['lon']])

        folium.PolyLine(
            route_coords,
            color='blue',
            weight=4,
            opacity=0.8,
            popup='Route'
        ).add_to(route_map)

        # Add markers
        for i, idx in enumerate(route_order):
            loc = self.locations[idx]

            # Different icon for start, end, and waypoints
            if i == 0:
                icon_color = 'green'
                icon = 'play'
                label = 'START'
            elif i == len(route_order) - 1:
                icon_color = 'red'
                icon = 'stop'
                label = 'END'
            else:
                icon_color = 'blue'
                icon = 'info-sign'
                label = f'Stop {i}'

            # Calculate distance to next location
            if i < len(route_order) - 1:
                next_idx = route_order[i + 1]
                next_loc = self.locations[next_idx]
                distance = self.calculate_distance(loc, next_loc)
                distance_text = f"<p><b>Distance to next:</b> {distance:.2f} km</p>"
            else:
                distance_text = ""

            popup_html = f"""
            <div style="font-family: Arial; width: 250px;">
                <h4 style="color: #2c3e50;">{label}</h4>
                <p><b>Location:</b> {loc['name']}</p>
                <p><b>Coordinates:</b><br>
                   {loc['lat']:.6f}, {loc['lon']:.6f}
                </p>
                {distance_text}
            </div>
            """

            folium.Marker(
                location=[loc['lat'], loc['lon']],
                popup=folium.Popup(popup_html, max_width=300),
                tooltip=f"{label}: {loc['name']}",
                icon=folium.Icon(color=icon_color, icon=icon)
            ).add_to(route_map)

            # Add step number
            folium.Marker(
                location=[loc['lat'], loc['lon']],
                icon=folium.DivIcon(html=f"""
                    <div style="font-size: 14pt; color: white;
                                background-color: {'green' if i == 0 else 'red' if i == len(route_order) - 1 else 'blue'};
                                width: 30px; height: 30px;
                                border-radius: 50%;
                                text-align: center;
                                line-height: 30px;
                                font-weight: bold;
                                border: 2px solid white;">
                        {i + 1}
                    </div>
                """)
            ).add_to(route_map)

        # Add measurement tool
        plugins.MeasureControl().add_to(route_map)

        # Add fullscreen
        plugins.Fullscreen().add_to(route_map)

        # Save map
        route_map.save(filename)
        print(f"✅ Route map saved as {filename}")

        return route_map

    def print_route_details(self, route_order):
        """Print detailed route information"""
        print("\n" + "=" * 70)
        print("ROUTE DETAILS")
        print("=" * 70)

        total_distance = 0

        for i, idx in enumerate(route_order):
            loc = self.locations[idx]
            print(f"\n{i + 1}. {loc['name']}")
            print(f"   Coordinates: ({loc['lat']:.6f}, {loc['lon']:.6f})")

            if i < len(route_order) - 1:
                next_idx = route_order[i + 1]
                next_loc = self.locations[next_idx]
                distance = self.calculate_distance(loc, next_loc)
                total_distance += distance
                print(f"   ↓ {distance:.2f} km to next location")

        print("\n" + "=" * 70)
        print(f"TOTAL DISTANCE: {total_distance:.2f} km ({total_distance * 0.621371:.2f} miles)")
        print("=" * 70)

def demo_route_optimization():
    """Demo: Optimize a route through multiple cities"""
    print("=" * 70)
    print("🗺️ ROUTE OPTIMIZER - DEMO")
    print("=" * 70)

    # Create optimizer
    optimizer = RouteOptimizer()

    # Add locations (East Africa road trip)
    print("\n📍 Adding locations...")
    locations = [
        "Dar es Salaam, Tanzania",
        "Arusha, Tanzania",
        "Nairobi, Kenya",
        "Kampala, Uganda",
        "Kigali, Rwanda"
    ]

    for loc in locations:
        optimizer.add_location(loc)
        time.sleep(1)  # Be respectful to geocoding API

    print(f"\n✅ Added {len(optimizer.locations)} locations")

    # Original order
    print("\n📊 ORIGINAL ORDER:")
    original_route = list(range(len(optimizer.locations)))
    original_distance = optimizer.calculate_total_distance(original_route)
    print(f"Total Distance: {original_distance:.2f} km")

    # Optimize using nearest neighbor
    print("\n🔧 OPTIMIZING ROUTE (Nearest Neighbor)...")
    optimized_route, optimized_distance = optimizer.optimize_route_nearest_neighbor(
        start_index=0,
        return_to_start=False
    )

    print(f"✅ Optimized Distance: {optimized_distance:.2f} km")
    print(f"💰 Savings: {original_distance - optimized_distance:.2f} km " +
          f"({((original_distance - optimized_distance) / original_distance * 100):.1f}%)")

    # Print route details
    optimizer.print_route_details(optimized_route)

    # Create map
    print("\n🗺️ Creating route map...")
    optimizer.create_route_map(optimized_route, 'optimized_route.html')

    print("\n✅ Done! Open 'optimized_route.html' to view the optimized route.")

if __name__ == "__main__":
    demo_route_optimization()
