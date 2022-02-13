from floodsystem.plot import plot_water_levels
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
from floodsystem.stationdata import build_station_list


def demonstrate_plot_water_levels():
    """
    Plots the water levels for the 5 stations with the highest relative
    water level
    """
    stations = build_station_list()[:5]
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days = 10))
        plot_water_levels(station, dates, levels)





if __name__ == "__main__":
    print("*** Task 2E: CUED Part IA Flood Warning System ***")
    demonstrate_plot_water_levels()