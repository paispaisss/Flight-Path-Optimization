from src.utils import haversine_distance

def nearest_neighbor(points, start):
    """
    Algoritma Nearest Neighbor untuk rute terpendek berbasis GPS (haversine).
    """
    unvisited = set(points.keys())
    route = [start]
    unvisited.remove(start)
    total_distance = 0

    current = start
    while unvisited:
        next_point = min(unvisited, key=lambda p: haversine_distance(points[current], points[p]))
        total_distance += haversine_distance(points[current], points[next_point])
        route.append(next_point)
        current = next_point
        unvisited.remove(next_point)

    # kembali ke titik awal
    total_distance += haversine_distance(points[current], points[start])
    route.append(start)

    return route, total_distance
