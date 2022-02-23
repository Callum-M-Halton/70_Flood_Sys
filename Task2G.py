import math

from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import get_towns_flood_times_ordered, risk_level_from_flood_time

def run():
    """
    """
    station_list = build_station_list()
    update_water_levels(station_list)
    towns_flood_times_ordered = get_towns_flood_times_ordered(station_list)
    
    previous_flood_time = math.inf
    current_rank = 1
    for town_pair in towns_flood_times_ordered:
        flood_time = town_pair[1]
        risk_level = risk_level_from_flood_time(flood_time)


        if flood_time > previous_flood_time:
            previous_flood_time = flood_time
            current_rank += 1
        
        print(f"{current_rank}.", f"{town_pair[0]}:", risk_level))    
        
    '''

if __name__ == "__main__":
    print("*** Task 2B: CUED Part IA Flood Warning System ***")
    run()