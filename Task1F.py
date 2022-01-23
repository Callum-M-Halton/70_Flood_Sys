from floodsystem.station import inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list

def test_inconsistent_stations_list(stations = build_station_list()):
    """
    Prints a list of inconsistent stations
    """
    list_of_stations = inconsistent_typical_range_stations(stations)
    name_list = []
    for station in list_of_stations:
        name_list.append(station.name)
    name_list.sort()
    print(name_list)

test_inconsistent_stations_list()