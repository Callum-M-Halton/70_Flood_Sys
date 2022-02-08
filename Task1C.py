from floodsystem.geo import stations_within_radius
from floodsystem.stationdata import build_station_list

def demonstrate_station_radius():
    """
    Prints a sorted list of the names of the stations within a radius r of the cambridge city centre
    """
    stations_list = stations_within_radius(build_station_list(), (52.2053, 0.1218), 10)
    sorted_stations = []
    for station in stations_list:
        sorted_stations.append(station.name)

    sorted_stations.sort()

    assert sorted_stations == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']

    print(sorted_stations)


if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    demonstrate_station_radius()