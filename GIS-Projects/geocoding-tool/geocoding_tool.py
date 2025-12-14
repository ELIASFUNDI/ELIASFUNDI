"""
Geocoding and Reverse Geocoding Tool
Convert addresses to coordinates and coordinates to addresses
"""

from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from geopy.exc import GeocoderTimedOut, GeocoderServiceError
import folium
import time

class GeocodingTool:
    def __init__(self, user_agent="gis_geocoding_app"):
        """Initialize the geocoding tool"""
        self.geolocator = Nominatim(user_agent=user_agent)

    def geocode(self, address):
        """
        Convert an address to coordinates

        Returns: dict with latitude, longitude, and full address
        """
        try:
            print(f"🔍 Searching for: {address}")
            location = self.geolocator.geocode(address, timeout=10)

            if location:
                result = {
                    'address': location.address,
                    'latitude': location.latitude,
                    'longitude': location.longitude,
                    'raw': location.raw
                }
                print(f"✅ Found: {location.address}")
                print(f"📍 Coordinates: ({result['latitude']:.6f}, {result['longitude']:.6f})")
                return result
            else:
                print(f"❌ Address not found: {address}")
                return None

        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"❌ Error: {e}")
            return None

    def reverse_geocode(self, latitude, longitude):
        """
        Convert coordinates to an address

        Returns: dict with address information
        """
        try:
            print(f"🔍 Looking up coordinates: ({latitude}, {longitude})")
            location = self.geolocator.reverse(f"{latitude}, {longitude}", timeout=10)

            if location:
                result = {
                    'address': location.address,
                    'latitude': latitude,
                    'longitude': longitude,
                    'raw': location.raw
                }
                print(f"✅ Found: {location.address}")
                return result
            else:
                print(f"❌ Location not found")
                return None

        except (GeocoderTimedOut, GeocoderServiceError) as e:
            print(f"❌ Error: {e}")
            return None

    def batch_geocode(self, addresses):
        """Geocode multiple addresses"""
        results = []
        for i, address in enumerate(addresses, 1):
            print(f"\n[{i}/{len(addresses)}]")
            result = self.geocode(address)
            if result:
                results.append(result)
            time.sleep(1)  # Be respectful to the API
        return results

    def calculate_distance(self, loc1, loc2):
        """
        Calculate distance between two locations

        loc1, loc2: Can be (lat, lon) tuples or address strings
        Returns: Distance in kilometers
        """
        # If inputs are strings, geocode them first
        if isinstance(loc1, str):
            result1 = self.geocode(loc1)
            if not result1:
                return None
            loc1 = (result1['latitude'], result1['longitude'])

        if isinstance(loc2, str):
            result2 = self.geocode(loc2)
            if not result2:
                return None
            loc2 = (result2['latitude'], result2['longitude'])

        # Calculate distance
        distance = geodesic(loc1, loc2).kilometers
        print(f"📏 Distance: {distance:.2f} km ({distance * 0.621371:.2f} miles)")
        return distance

    def create_map(self, locations, filename='geocoded_map.html'):
        """
        Create a map with geocoded locations

        locations: List of dicts with latitude, longitude, and address
        """
        if not locations:
            print("No locations to map")
            return

        # Calculate center
        avg_lat = sum(loc['latitude'] for loc in locations) / len(locations)
        avg_lon = sum(loc['longitude'] for loc in locations) / len(locations)

        # Create map
        geo_map = folium.Map(
            location=[avg_lat, avg_lon],
            zoom_start=4
        )

        # Add markers
        for i, loc in enumerate(locations, 1):
            popup_html = f"""
            <div style="font-family: Arial; width: 300px;">
                <h4 style="color: #2c3e50;">📍 Location {i}</h4>
                <p><b>Address:</b> {loc['address']}</p>
                <p><b>Coordinates:</b><br>
                   Lat: {loc['latitude']:.6f}<br>
                   Lon: {loc['longitude']:.6f}
                </p>
            </div>
            """

            folium.Marker(
                location=[loc['latitude'], loc['longitude']],
                popup=folium.Popup(popup_html, max_width=350),
                tooltip=f"Location {i}",
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(geo_map)

        # If multiple locations, draw lines between them
        if len(locations) > 1:
            coords = [[loc['latitude'], loc['longitude']] for loc in locations]
            folium.PolyLine(
                coords,
                color='blue',
                weight=2,
                opacity=0.8
            ).add_to(geo_map)

        # Save map
        geo_map.save(filename)
        print(f"\n✅ Map saved as {filename}")
        return geo_map

def demo_geocoding():
    """Demo: Geocoding addresses"""
    print("=" * 70)
    print("🌍 GEOCODING TOOL - DEMO")
    print("=" * 70)

    geocoder = GeocodingTool()

    print("\n📍 PART 1: Geocoding (Address → Coordinates)")
    print("-" * 70)

    # Example addresses
    addresses = [
        "Times Square, New York, USA",
        "Eiffel Tower, Paris, France",
        "Great Wall of China",
        "Sydney Opera House, Australia",
        "Mount Kilimanjaro, Tanzania"
    ]

    locations = geocoder.batch_geocode(addresses)

    print("\n📍 PART 2: Reverse Geocoding (Coordinates → Address)")
    print("-" * 70)

    # Example coordinates
    coords = [
        (51.5074, -0.1278),  # London
        (35.6762, 139.6503),  # Tokyo
    ]

    for lat, lon in coords:
        geocoder.reverse_geocode(lat, lon)
        print()

    print("\n📏 PART 3: Distance Calculation")
    print("-" * 70)

    # Calculate distances
    geocoder.calculate_distance("New York, USA", "London, UK")
    time.sleep(1)
    geocoder.calculate_distance("Dar es Salaam, Tanzania", "Nairobi, Kenya")

    print("\n🗺️ PART 4: Creating Interactive Map")
    print("-" * 70)

    if locations:
        geocoder.create_map(locations, 'geocoded_locations.html')

    print("\n✅ Demo complete! Open 'geocoded_locations.html' to view the map.")

def interactive_mode():
    """Interactive mode for user input"""
    geocoder = GeocodingTool()

    print("\n" + "=" * 70)
    print("🌍 INTERACTIVE GEOCODING MODE")
    print("=" * 70)
    print("\nOptions:")
    print("1. Geocode an address")
    print("2. Reverse geocode coordinates")
    print("3. Calculate distance between two locations")
    print("4. Exit")

    while True:
        choice = input("\nEnter your choice (1-4): ").strip()

        if choice == '1':
            address = input("Enter address: ").strip()
            if address:
                geocoder.geocode(address)

        elif choice == '2':
            try:
                lat = float(input("Enter latitude: ").strip())
                lon = float(input("Enter longitude: ").strip())
                geocoder.reverse_geocode(lat, lon)
            except ValueError:
                print("❌ Invalid coordinates")

        elif choice == '3':
            loc1 = input("Enter first location (address or 'lat,lon'): ").strip()
            loc2 = input("Enter second location (address or 'lat,lon'): ").strip()

            # Check if input is coordinates
            if ',' in loc1 and all(c.replace('.', '').replace('-', '').isdigit() or c == ',' for c in loc1):
                lat1, lon1 = map(float, loc1.split(','))
                loc1 = (lat1, lon1)

            if ',' in loc2 and all(c.replace('.', '').replace('-', '').isdigit() or c == ',' for c in loc2):
                lat2, lon2 = map(float, loc2.split(','))
                loc2 = (lat2, lon2)

            geocoder.calculate_distance(loc1, loc2)

        elif choice == '4':
            print("👋 Goodbye!")
            break

        else:
            print("❌ Invalid choice")

if __name__ == "__main__":
    demo_geocoding()

    # Uncomment to run interactive mode
    # interactive_mode()
