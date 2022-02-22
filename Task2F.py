
from floodsystem.datafetcher import fetch_measure_levels
from datetime import timedelta
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib.dates as date
from floodsystem.plot import plot_water_levels_with_fit
from floodsystem.flood import stations_highest_rel_level




def demonstrate_poly_fit(t, d, n):
    """
    Creates a polynomial fit of degree d for the n stations at which the current relative
    water level is greatest, for a period of time extending back t days, 
    """

    all_stations= build_station_list()
    update_water_levels(all_stations)
    top_five_stations = stations_highest_rel_level(all_stations, n)

    for station in top_five_stations:
        dates, levels = fetch_measure_levels(station.measure_id, dt=timedelta(days = t))
        if dates:
            if levels: #Making sure they exist as sometimes they do not
                dates = date.date2num(dates)
                plot_water_levels_with_fit(station, dates, levels, d)
            else:
                if len(top_five_stations) == 5: #Ensures 5 stations are still printed even if the first one has no data
                    demonstrate_poly_fit(2, 4, n+1)
                    break
        else: #Ensures 5 stations are still printed even if the first one has no data
            if len(top_five_stations) == 5:
                demonstrate_poly_fit(2, 4, n+1)
                break
                           



if __name__ == "__main__":
    print("*** Task 2F: CUED Part IA Flood Warning System ***")
    demonstrate_poly_fit(2, 4, 5)
