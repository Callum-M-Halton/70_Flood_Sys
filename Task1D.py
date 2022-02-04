
from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_station, stations_by_river

def run():
    """
    1. Prints how many rivers have at least one monitoring station
        and prints the first 10 of these rivers in alphabetical order.
    2. print the names of the stations located on the following rivers 
        in alphabetical order: ‘River Aire’, ‘River Cam’ & ‘River Thames’
    """

    # Build list of stations
    stations = build_station_list()

    # 1)
    print('\n========== 1 ==========')
    stationed_rivers = rivers_with_station(stations)
    # Print number of stationed rivers
    print(len(stationed_rivers), "stationed rivers.\n")
    # Print the first ten stationed rivers alphabetically
    print("First 10 -", sorted(stationed_rivers)[0:10])

    # 2)
    print('\n========== 2 ==========')
    stations_by_rivername = stations_by_river(stations)
    for rivername in ['River Aire', 'River Cam', 'River Thames']:
        # Print the names of the stations located on the current 
        # river in alphabetical order
        print("\nStations on", rivername + ":", sorted(stations_by_rivername[rivername]))

if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
