import matplotlib.pyplot as plt
from datetime import datetime, timedelta
from .analysis import polyfit


def plot_water_levels(station, dates, levels):
    """
    Plots water levels against time for a given station
    """
    plt.plot(dates, levels)
    if station.typical_range_consistent(): 
        plt.axhline(y=station.typical_range[1], linestyle = "--", color = "r") #Plots typical high line
        plt.axhline(y = station.typical_range[0], linestyle = "--", color = "g") #PLots typical low line
   
    """
    plt.plot(dates, station.typical_range[1])

    """
    plt.xlabel("Date")
    plt.xticks(rotation=45)
    plt.ylabel("Water level (M)")
    plt.title(station.name)
    plt.tight_layout()
    plt.show()

def plot_water_levels_with_fit(station, dates, levels, p):
    """
    Plots water level data points and a curve of best fit with degree p going through them
    """
    poly, d0 = polyfit(dates, levels, p)
    plt.plot(dates-d0, levels, ".", color = "b")
    plt.plot(dates-d0, poly(dates-d0), color = "r")
    
    if station.typical_range_consistent(): 
        plt.axhline(y=station.typical_range[1], linestyle = "--", color = "r") #Plots typical high line
        plt.axhline(y = station.typical_range[0], linestyle = "--", color = "g") #PLots typical low line
    plt.xlabel("Days since 2 days ago")
    plt.xticks(rotation=45)
    plt.ylabel("Water level (M)")
    plt.title(station.name)
    plt.tight_layout()
    plt.show()
