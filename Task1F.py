from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def demonstrate_inconsistent_stations_list(stations = build_station_list()):
    """
    Prints a list of inconsistent stations
    """
    list_of_stations = inconsistent_typical_range_stations(stations)
    name_list = []
    for station in list_of_stations:
        name_list.append(station.name)
    name_list.sort()
    print(name_list)


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    demonstrate_inconsistent_stations_list()