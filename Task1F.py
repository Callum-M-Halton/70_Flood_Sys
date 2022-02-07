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
    assert name_list == ['Airmyn', 'Blacktoft', 'Braunton', 'Brentford', 'Broomfleet Weighton Lock', 'East Hull Hedon Road', 'Eastbourne Harbour', 'Fleetwood', 'Goole', 'Hedon Thorn Road Bridge', 'Hedon Westlands Drain', 'Hempholme Pumping Station Roam Drain', 'Hull Barrier Victoria Pier', 'Hull High Flaggs, Lincoln Street', 'Littlehampton', 'Medmerry', 'North America', 'Paull', 'Salt End', 'Sandwich Quay', 'Sindlesham Mill', 'Stone Creek', 'Templers Road', 'Tickton Pumping Station', 'Topsham', 'Totnes', 'Truro Harbour', 'Wilfholme Pumping Station']


if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    demonstrate_inconsistent_stations_list()