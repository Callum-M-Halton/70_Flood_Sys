from fileinput import close
from math import dist
from turtle import distance
from floodsystem.geo import stations_by_distance
from floodsystem.stationdata import build_station_list

def test_distance():
    """
    Prints the names, towns and distances of the 10 closest and furthest stations from the centre of cambridge
    No arguments expected, returns nothing
    """
    closest_ten = [] 
    furthest_ten = []
    distance_list = stations_by_distance(build_station_list(), (52.2053, 0.1218))
    

    for pair in distance_list[:10]: #Appends 10 closest stations to a list
        closest_ten.append((pair[0].name, pair[0].town, pair[1]))
    
    for pair in distance_list[-10:]: #Appends 10 furt hest stations to a list
        furthest_ten.append((pair[0].name, pair[0].town, pair[1]))
    
    
    print("Closest 10: \n", closest_ten, "\n")
    print("Furthest 10: \n", furthest_ten)

test_distance()