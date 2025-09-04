import folium

def visualize_route_map(coordinates, route, output_file="uav_route.html"):
    """
    Membuat peta interaktif rute UAV menggunakan folium.

    Parameters:
        coordinates (dict): dictionary {city: (lat, lon)}
        route (list): urutan nama kota sesuai rute
        output_file (str): nama file HTML output
    """
    # Ambil titik awal (kota pertama di rute)
    start_city = route[0]
    start_coords = coordinates[start_city]

    # Buat peta folium
    m = folium.Map(location=start_coords, zoom_start=5)

    # Tambahkan marker untuk setiap kota
    for city, (lat, lon) in coordinates.items():
        folium.Marker([lat, lon], popup=f"{city} ({lat}, {lon})").add_to(m)

    # Buat polyline sesuai urutan rute
    route_coords = [coordinates[city] for city in route]
    folium.PolyLine(route_coords, color="blue", weight=2.5, opacity=1).add_to(m)

    # Simpan ke file HTML
    m.save(output_file)
    print(f">>> Peta rute disimpan ke {output_file}")
