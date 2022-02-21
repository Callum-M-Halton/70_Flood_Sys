from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_level_over_threshold

def run():
    """
    Prints the name of each station at which the current relative level is
    over tolerance (initially 0.8), with the relative level alongside the name handling cases of
    inconsistent range data
    """

    # Build list of stations
    stations = build_station_list()

    # Update latest level data for all stations
    update_water_levels(stations)

    # Sets tolerance and prints out station name and relative water level 
    # for each tuple returned by stations_level_over_threshold, the function
    # being demonstrated
    tolerance = 0.9
    for tuple in stations_level_over_threshold(stations, tolerance):
        print(tuple[0].name, tuple[1])
    

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()
