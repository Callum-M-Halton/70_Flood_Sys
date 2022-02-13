
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta
from floodsystem.stationdata import build_station_list
import matplotlib.dates as date
from floodsystem.plot import plot_water_levels_with_fit




def demonstrate_poly_fit(t, d):
    """
    Creates a polynomial fit of degree d for the 5 stations at which the current relative
    water level is greatest, for a period of time extending back t days, 
    """
    stations= build_station_list()
    for station in stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days = t))
        dates = date.date2num(dates)
        plot_water_levels_with_fit(station, dates, levels, d)
    




if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    demonstrate_poly_fit(2, 4)
