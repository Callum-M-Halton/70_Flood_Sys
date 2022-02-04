
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    """
    Prints the list of the top 9 (river name, number of stations)
    tuples by number of stations using geo.rivers_by_station_number.
    """

    # Build list of stations
    stations = build_station_list()

    # Demo
    print(rivers_by_station_number(stations, 9))

if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
