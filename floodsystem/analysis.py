from this import d
from floodsystem.datafetcher import fetch_measure_levels
from datetime import datetime, timedelta
import numpy as np
from floodsystem.stationdata import build_station_list
import matplotlib.pyplot as plt

def polyfit(dates, levels, p):
    """
    Computes a least-squares fit of a polynomial of degree p to water level data
    """
    d0 = dates[-1]
    p_coeff = np.polyfit(dates-d0, levels, p)
    poly = np.poly1d(p_coeff)
    return poly, d0

