# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from .utils import sorted_by_key # noqa
from haversine import haversine

def stations_by_distance(stations, p):
    """
    With aruments being a list of stations (stations) and a coordinate (p):
        Returns a list of stations and their distance from coordinate p
    """
    distance_list = []
    for station in stations:
        distance = haversine(station.coord, p)
        distance_list.append((station, distance))

    distance_list = sorted_by_key(distance_list, 1)
    return distance_list

def stations_within_radius(stations, centre, r):
    """
    Returns a list of all stations within radius r of a geographic coordinate x
    """
    stations_list = [] #list of all stations within radius r of the centre point
    distance_list = stations_by_distance(stations, centre)
    for pair in distance_list: 
        if pair[1] < r:
            stations_list.append(pair[0])
        else:
            break
    return stations_list 
            
        
