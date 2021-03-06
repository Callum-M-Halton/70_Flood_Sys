import math
import numpy as np
from datetime import timedelta

from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.geo import get_stations_by_town

def polyfit(dates, levels, p):
    """
    Computes a least-squares fit of a polynomial of degree p to water level data
    """
    d0 = dates[-1]
    p_coeff = np.polyfit(dates-d0, levels, p)
    poly = np.poly1d(p_coeff)
    return poly, d0

def get_flood_time(station):
    """
    FOr a given station, returns the expected time until flooding occurs
    
    Works by calculating the rate of increase of the water level across the previous
    day and extrapolates until the flooding relative level (arbritarily chosen as 4) is met

    If the gradient is negative, returns an infinite time. 
    """
    # Define relative flood level at which flooding is expected
    expected_flooding_rel_level = 1.7
    rel_level = station.relative_water_level()
    if rel_level == None:
        return math.inf
    if rel_level >= expected_flooding_rel_level: #If already flooded
        return 0

    try:
        level_day_ago = fetch_measure_levels(station.measure_id, dt=timedelta(days = 1))[1][-1]
        test = level_day_ago + 1.0
    except:
        return math.inf
   
    relative_level_grad_over_day = (
        (rel_level - station.level_to_relative_level(level_day_ago))) #Calculates time until river floods

    if relative_level_grad_over_day > 0:
        print(station.name, station.town)

    if relative_level_grad_over_day <= 0: #i.e. never going to flood
        return math.inf #Returns infinite time until flooding
    else: #Floods in returned number of days
        return ((expected_flooding_rel_level - rel_level) / 
            relative_level_grad_over_day)
    
def get_towns_flood_times_ordered(stations):
    """
    Returns tuple pairs of towns, and flood times in
    Ascending order
    """
    stations_by_town = get_stations_by_town(stations)
    town_flood_times = []
    for town in stations_by_town:
        town_stations = stations_by_town[town] # List of stations by town
        min_flood_time = math.inf # Start at infinity (hightest possible time)
        for station in town_stations: 
            flood_time = get_flood_time(station) # Gets flood time
            if flood_time < min_flood_time:
                min_flood_time = flood_time 
                # Only uses the minimum time to flood if a town has more than one station
        town_flood_times.append((town, min_flood_time))
    
    town_flood_times.sort(reverse=False, key=(lambda pair : pair[1]))
    return town_flood_times

def risk_level_from_flood_time(flood_time):
    """
    Calculates the level of severity given the flood_time
    Returns the risk severity (low, medium, high, severe)
    """
    flood_time_thresholds = (
        ( 'severe'   , 0  ),
        ( 'high'     , 3  ),
        ( 'moderate' , 7  ),
        ( 'low'      , 14 ),
    )

    for threshold_pair in flood_time_thresholds:
        if flood_time >= threshold_pair[1]:
            risk_level = threshold_pair[0]
        else:
            break
    return risk_level

        
