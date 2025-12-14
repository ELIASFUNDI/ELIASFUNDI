"""
Population Density Heatmap Generator
Visualize population density using heatmaps
"""

import folium
from folium import plugins
import pandas as pd
import json

class PopulationHeatmap:
    def __init__(self):
        """Initialize Population Heatmap Generator"""
        self.population_data = []

    def load_demo_data(self):
        """Load demo population data for major world cities"""
        # Demo data: [lat, lon, population_in_millions]
        self.population_data = [
            # Asia
            [35.6762, 139.6503, 37.4],  # Tokyo
            [28.7041, 77.1025, 32.9],   # Delhi
            [31.2304, 121.4737, 28.5],  # Shanghai
            [22.3964, 114.1095, 7.5],   # Hong Kong
            [1.3521, 103.8198, 5.9],    # Singapore
            [25.2048, 55.2708, 3.4],    # Dubai
            [19.0760, 72.8777, 20.4],   # Mumbai
            [12.9716, 77.5946, 12.8],   # Bangalore
            [23.8103, 90.4125, 21.0],   # Dhaka
            [14.5995, 120.9842, 14.0],  # Manila
            [13.7563, 100.5018, 10.5],  # Bangkok
            [39.9042, 116.4074, 21.5],  # Beijing
            [37.5665, 126.9780, 9.8],   # Seoul
            [-6.2088, 106.8456, 10.6],  # Jakarta
            [25.0330, 121.5654, 7.0],   # Taipei

            # Europe
            [51.5074, -0.1278, 9.0],    # London
            [48.8566, 2.3522, 11.0],    # Paris
            [55.7558, 37.6173, 12.6],   # Moscow
            [41.9028, 12.4964, 4.3],    # Rome
            [40.4168, -3.7038, 6.6],    # Madrid
            [52.5200, 13.4050, 3.7],    # Berlin
            [41.3851, 2.1734, 5.6],     # Barcelona

            # Americas
            [40.7128, -74.0060, 18.8],  # New York
            [-23.5505, -46.6333, 22.0], # São Paulo
            [19.4326, -99.1332, 21.8],  # Mexico City
            [34.0522, -118.2437, 13.2], # Los Angeles
            [-34.6037, -58.3816, 15.0], # Buenos Aires
            [-22.9068, -43.1729, 13.5], # Rio de Janeiro
            [41.8781, -87.6298, 8.9],   # Chicago
            [43.6532, -79.3832, 6.2],   # Toronto

            # Africa
            [30.0444, 31.2357, 21.3],   # Cairo
            [-26.2041, 28.0473, 5.8],   # Johannesburg
            [6.5244, 3.3792, 14.8],     # Lagos
            [33.9716, -6.8498, 3.7],    # Casablanca
            [-6.7924, 39.2083, 6.7],    # Dar es Salaam
            [-1.2921, 36.8219, 4.9],    # Nairobi
            [9.0320, 38.7469, 4.8],     # Addis Ababa

            # Oceania
            [-33.8688, 151.2093, 5.3],  # Sydney
            [-37.8136, 144.9631, 5.1],  # Melbourne
        ]

        print(f"✅ Loaded {len(self.population_data)} cities")
        return self.population_data

    def create_heatmap(self, filename='population_heatmap.html'):
        """Create a population density heatmap"""
        if not self.population_data:
            print("No population data loaded. Loading demo data...")
            self.load_demo_data()

        # Create map
        pop_map = folium.Map(
            location=[20, 0],
            zoom_start=2,
            tiles='OpenStreetMap'
        )

        # Create heatmap data (weighted by population)
        heatmap_data = []
        for lat, lon, population in self.population_data:
            # Weight the heatmap by population
            # Add multiple points for higher population (intensity)
            intensity = int(population)
            for _ in range(max(1, intensity)):
                heatmap_data.append([lat, lon])

        # Add heatmap layer
        plugins.HeatMap(
            heatmap_data,
            min_opacity=0.2,
            max_zoom=13,
            radius=25,
            blur=35,
            gradient={
                0.0: 'blue',
                0.3: 'cyan',
                0.5: 'lime',
                0.7: 'yellow',
                0.9: 'orange',
                1.0: 'red'
            }
        ).add_to(pop_map)

        # Add city markers with population info
        for lat, lon, population in self.population_data:
            popup_html = f"""
            <div style="font-family: Arial; width: 200px;">
                <h4 style="color: #e74c3c; margin: 0;">
                    👥 Population Data
                </h4>
                <hr style="margin: 5px 0;">
                <p style="margin: 5px 0;">
                    <b>Population:</b> {population:.1f}M
                </p>
                <p style="margin: 5px 0;">
                    <b>Location:</b><br>
                    {lat:.4f}, {lon:.4f}
                </p>
            </div>
            """

            # Only show markers at higher zoom levels to avoid clutter
            folium.CircleMarker(
                location=[lat, lon],
                radius=population / 2,
                popup=folium.Popup(popup_html, max_width=250),
                color='darkred',
                fill=True,
                fillColor='red',
                fillOpacity=0.3,
                weight=1
            ).add_to(pop_map)

        # Add fullscreen
        plugins.Fullscreen().add_to(pop_map)

        # Save map
        pop_map.save(filename)
        print(f"✅ Heatmap saved as {filename}")

        return pop_map

    def create_choropleth_map(self, filename='choropleth_map.html'):
        """Create a choropleth map showing population density by region"""
        # Create base map
        choropleth_map = folium.Map(
            location=[20, 0],
            zoom_start=2,
            tiles='OpenStreetMap'
        )

        # Add markers for major cities with graduated circles
        for lat, lon, population in self.population_data:
            # Calculate radius based on population
            radius = population * 3

            # Color based on population
            if population >= 20:
                color = 'darkred'
            elif population >= 15:
                color = 'red'
            elif population >= 10:
                color = 'orange'
            elif population >= 5:
                color = 'yellow'
            else:
                color = 'lightblue'

            folium.Circle(
                location=[lat, lon],
                radius=radius * 10000,  # Convert to meters
                color=color,
                fill=True,
                fillColor=color,
                fillOpacity=0.4,
                weight=2,
                popup=f"Population: {population:.1f}M"
            ).add_to(choropleth_map)

        # Add fullscreen
        plugins.Fullscreen().add_to(choropleth_map)

        # Save map
        choropleth_map.save(filename)
        print(f"✅ Choropleth map saved as {filename}")

        return choropleth_map

    def get_statistics(self):
        """Calculate population statistics"""
        if not self.population_data:
            return "No data available"

        populations = [pop for _, _, pop in self.population_data]

        stats = {
            'total_cities': len(self.population_data),
            'total_population': sum(populations),
            'average_population': sum(populations) / len(populations),
            'max_population': max(populations),
            'min_population': min(populations),
            'mega_cities': sum(1 for pop in populations if pop >= 10)  # 10M+
        }

        return stats

    def print_statistics(self):
        """Print population statistics"""
        stats = self.get_statistics()

        if isinstance(stats, str):
            print(stats)
            return

        print("\n" + "=" * 60)
        print("POPULATION STATISTICS")
        print("=" * 60)
        print(f"Total Cities: {stats['total_cities']}")
        print(f"Total Population: {stats['total_population']:.1f} Million")
        print(f"Average Population: {stats['average_population']:.1f} Million")
        print(f"Largest City: {stats['max_population']:.1f} Million")
        print(f"Smallest City: {stats['min_population']:.1f} Million")
        print(f"Mega Cities (10M+): {stats['mega_cities']}")
        print("=" * 60)

    def load_custom_data(self, data):
        """
        Load custom population data

        data: List of [latitude, longitude, population_in_millions]
        """
        self.population_data = data
        print(f"✅ Loaded {len(self.population_data)} custom data points")

def main():
    """Main function to generate population heatmaps"""
    print("=" * 60)
    print("🗺️ POPULATION DENSITY HEATMAP GENERATOR")
    print("=" * 60)

    # Create heatmap generator
    generator = PopulationHeatmap()

    # Load demo data
    print("\n📊 Loading population data...")
    generator.load_demo_data()

    # Print statistics
    generator.print_statistics()

    # Create heatmap
    print("\n🔥 Generating heatmap...")
    generator.create_heatmap('population_heatmap.html')

    # Create choropleth map
    print("\n📍 Generating choropleth map...")
    generator.create_choropleth_map('choropleth_population.html')

    print("\n✅ Done! Open the HTML files to view the maps:")
    print("   - population_heatmap.html (Heatmap view)")
    print("   - choropleth_population.html (Circle size view)")

    print("\n🎨 Heatmap Color Legend:")
    print("   🔵 Blue → Low population density")
    print("   💚 Green → Medium-low population")
    print("   🟡 Yellow → Medium population")
    print("   🟠 Orange → High population")
    print("   🔴 Red → Very high population density")

if __name__ == "__main__":
    main()
