from src.utils import load_coordinates_from_csv
from src.optimizer import nearest_neighbor
from src.visualizer import visualize_route_map  # ⬅️ tambahkan
import matplotlib.pyplot as plt

def main():
    print(">>> Program dimulai (GPS version)")

    # 1. Load data
    coordinates = load_coordinates_from_csv("data/coordinates_gps.csv")
    print(">>> Data berhasil dibaca")
    for city, (lat, lon) in coordinates.items():
        print(f"{city}: ({lat}, {lon})")

    # 2. Jalankan algoritma
    start_node = list(coordinates.keys())[0]  # titik awal = pertama di CSV
    print(f">>> Mulai algoritma dari titik {start_node}")
    route, total_distance = nearest_neighbor(coordinates, start_node)

    # 3. Output
    print("\nRute terbaik (Nearest Neighbor):")
    print(" -> ".join(route))
    print(f"Total Jarak: {total_distance:.2f} km")

    # 4. Visualisasi interaktif
    visualize_route_map(coordinates, route)

if __name__ == "__main__":
    main()
