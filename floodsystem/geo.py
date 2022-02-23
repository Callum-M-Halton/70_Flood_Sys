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
    With arguments being a list of stations (stations) and a coordinate (p):
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
            
def rivers_with_station(stations):
    """
    Given a list of station objects, returns a set with the names of the
    rivers with a monitoring station. As the container is a set, there are no duplicates.
    """
    stationed_rivers = set()
    for station in stations:
        if station.river:
            stationed_rivers.add(station.river)

    return stationed_rivers


def stations_by_river(stations):
    """
    Given a list of station objects, returns a dictionary that maps river names
    to a list of station objects on a given river
    """
    stations_by_rivername = {}
    for station in stations:
        if station.river:
            if station.river in stations_by_rivername:
                stations_by_rivername[station.river].append(station.name)
            else:
                stations_by_rivername[station.river] = [station.name]
    return stations_by_rivername

def rivers_by_station_number(stations, N):
    """
    Determines the N rivers with the greatest number of monitoring stations 
    and returns a list of (river name, number of stations) tuples,
    sorted by the number of stations. In the case that there are more rivers with
    the same number of stations as the Nth entry, these rivers are included in the list. 
    """

    # Creates count of stations for earch river
    river_station_numbers = {}
    for station in stations:
        if station.river in river_station_numbers:
            river_station_numbers[station.river] += 1
        else:
            river_station_numbers[station.river] = 1
    
    # Selects top N rivers by station number and returns them as tuple list
    remaining_river_pairs = river_station_numbers.items()
    top_N_rivers_by_station_number = []
    for i in range(N):
        if remaining_river_pairs:
            highest = 0
            highest_pairs = []
            for river_pair in remaining_river_pairs:
                if river_pair[1] > highest:
                    highest_pairs = [river_pair]
                    highest = river_pair[1]
                elif river_pair[1] == highest:
                    highest_pairs.append(river_pair)

            remaining_river_pairs = [river_pair for river_pair in remaining_river_pairs if river_pair not in highest_pairs]
            top_N_rivers_by_station_number = top_N_rivers_by_station_number + highest_pairs
        else:
            break
    
    return top_N_rivers_by_station_number

def get_stations_by_town(stations):
    """
    Returns a dictionary consisting of a (key, value) pair of towns (key) and a list of the
    stations inside of them (value)
    """
    towns = {} #dictionary of towns
    for station in stations:
        town = station.town 
        if town in towns:
            towns[town].append(station.name)
        else:
            towns[town] = [station.name]
    return towns