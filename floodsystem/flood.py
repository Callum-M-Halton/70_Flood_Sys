
def stations_level_over_threshold(stations, tol):
    high_level_stations = []
    for station in stations:
        if station.typical_range_consistent:
            rel_level = station.relative_water_level()
            if rel_level > tol:
                high_level_stations.append((station, rel_level))
    
    return high_level_stations.sort(True, key=lambda tup : tup[1])