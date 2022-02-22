
from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_highest_rel_level


def demonstrate_plot_water_levels(n):
    """
    Plots the water levels for the 5 stations with the highest relative
    water level
    """
    all_stations = build_station_list()
    update_water_levels(all_stations)
    top_five_stations = stations_highest_rel_level(all_stations, n)
    for station in top_five_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days = 10))
        if dates: #Ensures if a stations dates data doesnt exist, top 5 still print
            if levels: #Ensures if stations level data doesn't exist, top 5 still print
                plot_water_levels(station, dates, levels)
            else: 
                if len(top_five_stations) == 5:
                    demonstrate_plot_water_levels(6)
                    break
        else:
            if len(top_five_stations) == 5:
                demonstrate_plot_water_levels(6)
                break




if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    demonstrate_plot_water_levels(5)