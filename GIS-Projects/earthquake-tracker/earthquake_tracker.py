"""
Real-Time Earthquake Tracker and Visualizer
Fetches earthquake data from USGS and visualizes on an interactive map
"""

import requests
import folium
from folium import plugins
from datetime import datetime, timedelta
import json

class EarthquakeTracker:
    def __init__(self):
        """Initialize the Earthquake Tracker"""
        self.base_url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/"
        self.earthquakes = []

    def fetch_earthquakes(self, time_period='day', min_magnitude='all'):
        """
        Fetch earthquake data from USGS

        time_period: 'hour', 'day', 'week', 'month'
        min_magnitude: 'all', 'significant', '4.5', '2.5', '1.0'
        """
        url = f"{self.base_url}{min_magnitude}_{time_period}.geojson"

        try:
            print(f"Fetching earthquake data from USGS...")
            response = requests.get(url, timeout=10)
            response.raise_for_status()
            data = response.json()

            self.earthquakes = data['features']
            print(f"✅ Found {len(self.earthquakes)} earthquakes")
            return self.earthquakes

        except requests.exceptions.RequestException as e:
            print(f"❌ Error fetching data: {e}")
            return []

    def get_marker_color(self, magnitude):
        """Get marker color based on earthquake magnitude"""
        if magnitude >= 7.0:
            return 'darkred'
        elif magnitude >= 6.0:
            return 'red'
        elif magnitude >= 5.0:
            return 'orange'
        elif magnitude >= 4.0:
            return 'yellow'
        elif magnitude >= 3.0:
            return 'lightgreen'
        else:
            return 'green'

    def get_circle_radius(self, magnitude):
        """Calculate circle radius based on magnitude"""
        return magnitude * 20000

    def create_map(self, filename='earthquake_map.html'):
        """Create an interactive map with earthquake data"""
        if not self.earthquakes:
            print("No earthquake data available. Fetch data first.")
            return

        # Create map centered on the world
        eq_map = folium.Map(
            location=[20, 0],
            zoom_start=2,
            tiles='OpenStreetMap'
        )

        # Add earthquake markers
        for eq in self.earthquakes:
            coords = eq['geometry']['coordinates']
            lon, lat, depth = coords[0], coords[1], coords[2]

            properties = eq['properties']
            magnitude = properties.get('mag', 0)
            place = properties.get('place', 'Unknown')
            time = properties.get('time', 0)
            tsunami = properties.get('tsunami', 0)

            # Convert timestamp to readable date
            eq_time = datetime.fromtimestamp(time / 1000).strftime('%Y-%m-%d %H:%M:%S UTC')

            # Create popup text
            popup_html = f"""
            <div style="font-family: Arial; width: 250px;">
                <h4 style="color: #d73027; margin-bottom: 10px;">
                    🌍 Magnitude {magnitude}
                </h4>
                <p><b>Location:</b> {place}</p>
                <p><b>Time:</b> {eq_time}</p>
                <p><b>Depth:</b> {depth:.2f} km</p>
                <p><b>Coordinates:</b> {lat:.4f}, {lon:.4f}</p>
                {'<p style="color: red;"><b>⚠️ TSUNAMI WARNING</b></p>' if tsunami else ''}
            </div>
            """

            # Add circle (size based on magnitude)
            folium.Circle(
                location=[lat, lon],
                radius=self.get_circle_radius(magnitude),
                popup=folium.Popup(popup_html, max_width=300),
                color=self.get_marker_color(magnitude),
                fill=True,
                fillColor=self.get_marker_color(magnitude),
                fillOpacity=0.4,
                weight=2
            ).add_to(eq_map)

            # Add marker
            folium.CircleMarker(
                location=[lat, lon],
                radius=magnitude * 2,
                popup=folium.Popup(popup_html, max_width=300),
                color=self.get_marker_color(magnitude),
                fill=True,
                fillColor=self.get_marker_color(magnitude),
                fillOpacity=0.8
            ).add_to(eq_map)

        # Add fullscreen button
        plugins.Fullscreen().add_to(eq_map)

        # Add measurement tool
        plugins.MeasureControl().add_to(eq_map)

        # Save map
        eq_map.save(filename)
        print(f"✅ Map saved as {filename}")

        return eq_map

    def get_statistics(self):
        """Get statistics about earthquakes"""
        if not self.earthquakes:
            return "No data available"

        magnitudes = [eq['properties'].get('mag', 0) for eq in self.earthquakes]

        stats = {
            'total_count': len(self.earthquakes),
            'max_magnitude': max(magnitudes),
            'min_magnitude': min(magnitudes),
            'avg_magnitude': sum(magnitudes) / len(magnitudes),
            'mag_7_plus': sum(1 for m in magnitudes if m >= 7.0),
            'mag_6_plus': sum(1 for m in magnitudes if m >= 6.0),
            'mag_5_plus': sum(1 for m in magnitudes if m >= 5.0),
            'mag_4_plus': sum(1 for m in magnitudes if m >= 4.0)
        }

        return stats

    def print_statistics(self):
        """Print earthquake statistics"""
        stats = self.get_statistics()

        if isinstance(stats, str):
            print(stats)
            return

        print("\n" + "=" * 60)
        print("EARTHQUAKE STATISTICS")
        print("=" * 60)
        print(f"Total Earthquakes: {stats['total_count']}")
        print(f"Magnitude Range: {stats['min_magnitude']:.1f} - {stats['max_magnitude']:.1f}")
        print(f"Average Magnitude: {stats['avg_magnitude']:.2f}")
        print("\nBreakdown by Magnitude:")
        print(f"  7.0+: {stats['mag_7_plus']} (Major)")
        print(f"  6.0+: {stats['mag_6_plus']} (Strong)")
        print(f"  5.0+: {stats['mag_5_plus']} (Moderate)")
        print(f"  4.0+: {stats['mag_4_plus']} (Light)")
        print("=" * 60)

def main():
    """Main function to run the earthquake tracker"""
    print("=" * 60)
    print("🌍 REAL-TIME EARTHQUAKE TRACKER")
    print("=" * 60)

    # Create tracker instance
    tracker = EarthquakeTracker()

    # Fetch earthquake data for the past day (magnitude 2.5+)
    tracker.fetch_earthquakes(time_period='day', min_magnitude='2.5')

    # Print statistics
    tracker.print_statistics()

    # Create visualization
    print("\n📊 Creating interactive map...")
    tracker.create_map('earthquake_map.html')

    print("\n✅ Done! Open 'earthquake_map.html' in your browser to view the map.")
    print("\nLegend:")
    print("  🔴 Dark Red: Magnitude 7.0+ (Major)")
    print("  🔴 Red: Magnitude 6.0-6.9 (Strong)")
    print("  🟠 Orange: Magnitude 5.0-5.9 (Moderate)")
    print("  🟡 Yellow: Magnitude 4.0-4.9 (Light)")
    print("  🟢 Light Green: Magnitude 3.0-3.9 (Minor)")
    print("  🟢 Green: Magnitude < 3.0 (Micro)")

if __name__ == "__main__":
    main()
