import pandas as pd
import math

def haversine_distance(coord1, coord2):
    """
    Menghitung jarak antara dua koordinat GPS (lat, lon) dalam kilometer.
    """
    R = 6371  # radius bumi (km)

    lat1, lon1 = coord1
    lat2, lon2 = coord2

    # konversi derajat → radian
    phi1, phi2 = math.radians(lat1), math.radians(lat2)
    dphi = math.radians(lat2 - lat1)
    dlambda = math.radians(lon2 - lon1)

    a = math.sin(dphi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(dlambda / 2) ** 2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    return R * c  # hasil dalam km

def load_coordinates_from_csv(path="data/coordinates_gps.csv"):
    """
    Membaca koordinat GPS dari file CSV.
    """
    df = pd.read_csv(path)
    points = {row["id"]: (row["latitude"], row["longitude"]) for _, row in df.iterrows()}
    return points
