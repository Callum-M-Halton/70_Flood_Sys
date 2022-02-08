
import string
from utils_for_tests import StockStation
from distutils.command.build import build
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number
from floodsystem.stationdata import build_station_list
from utils_for_tests import StockStation


def test_stations_by_distance():
    """
    Tests the stations by distance function in geo.py
    """
    
    p = (52.2053, 0.1218) #Coordinate of Cambridge city centre
    dict_1 = {"name" : "Station1",
              "coord" : (50, 1)  
                } #Station 1 should be closer than station 2
    dict_2 = {"name" : "Station2",
              "coord" : (75, 25)  
                } #Station 2 should be further away than station 1
    station1 = StockStation(dict_1)
    station2 = StockStation(dict_2)
    stations = [station2, station1] #Purposefully inputted in the wrong order to ensure sort works correctly
    
    station_distances = stations_by_distance(stations, p)
    
    assert len(station_distances) == 2 #Checks 2 stations are in the list
    assert station_distances[0][1] < station_distances[1][1] #Checks the first station in the list is closer than the second 
    assert station_distances[0][0].name == "Station1" #Checks that the closer station is actually at the start of the list 


def test_stations_within_radius():
    """
    Tests the stations_within_radius function in geo.py
    """

    stations_list = stations_within_radius(build_station_list(), (52.2053, 0.1218), 10)
    sorted_stations = []
    for station in stations_list:
        sorted_stations.append(station.name)

    sorted_stations.sort()

    assert sorted_stations == ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool",
'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton',
 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']

def test_rivers_with_station():
    """
    Tests the rivers_with_station function in geo.py
    """
    # Builds Test Data
    station_list = [ StockStation({'river' : river_name}) for river_name in (
        'a', 'a', 'b', 'c', 'c') ]
    rivers_with_station_set = rivers_with_station(station_list)
    # Checks container type
    assert type(rivers_with_station_set) == set
    # Checks rivers_with_station_set against expected output
    assert rivers_with_station_set == {'a', 'b', 'c'}
    a = StockStation({'river': 'a'})

def test_stations_by_river():
    """
    Tests the stations_by_river function in geo.py
    """
    # Builds Test Data
    station_list = [ StockStation({'name': pair[0], 'river': pair[1]}) for pair in (
        ('aName', 'xRiver'), ('bName', 'xRiver'), ('cName', 'yRiver'),
        ('dName', 'zRiver'), ('eName', 'zRiver'), ('fName', 'zRiver')) ]
    stations_by_rivername = stations_by_river(station_list)
    # Checks stations_by_rivername is a dict
    assert type(stations_by_rivername) == dict
    print(stations_by_rivername)
    # Checks river sets for the rivers x, y and z (...River)
    expected_stations = {
        'xRiver' : ['aName', 'bName'],
        'yRiver' : ['cName'],
        'zRiver' : ['dName', 'eName', 'fName']
    }
    for river_name in expected_stations:
        assert stations_by_rivername[river_name] == expected_stations[river_name]


def test_rivers_by_station_number():
    """
    Tests the rivers_by_station_number function in geo.py
    """
    
    # Generates 'triangle' of stations where each subsequent river has 
    # 0, 1 or 2 stations more than the previous river, the rivers are numbered
    # in order of generation so we'll know their correct order in the rankings
    tot_rivers = 5
    duplicate_period = 3
    stations = []
    for riverNum in range(1, tot_rivers):
        offset = 0
        if riverNum % duplicate_period == 0:
            offset = -1
        for stationNum in range(riverNum + offset):
            stations.append(
                StockStation({
                    'name'  : f"station on river {riverNum}", 
                    'river' : f"river {riverNum}"
            }))
    for station in stations:
        print(station.river)

    # Chooses N as half the number of test rivers rounded down
    test_N = tot_rivers // 2
    rivers_by_station_number_test = rivers_by_station_number(stations, test_N)
    print('\n\n\n\n', rivers_by_station_number_test)
    # Tests result is list of tuples of length 2
    assert type(rivers_by_station_number_test) == list
    for pair in rivers_by_station_number_test:
        assert type(pair) == tuple
        assert len(pair) == 2

    # Tests tuples returned are in order of number of stations and that 
    # the rivers are in the reverse of the order they were generated in 
    # (which was the order of the rivers by increasing number of stations)
    # and thus that if a river ranks lower than another that its river number should
    # likewise be smaller...
    ranks = 1
    lastPair = rivers_by_station_number_test[0]
    for pair in rivers_by_station_number_test[1:]:
        assert pair[1] <= lastPair[1]
        if pair[1] < lastPair[1]:
            # Checks river number of lower ranking river is smaller than hugher ranking river
            assert int(pair[0][6:]) < int(lastPair[0][6:])
            ranks += 1
        elif pair[1] == lastPair[1]:
            # Checks the river with the same number of rivers has a 
            # neighbouring station number
            assert (int(pair[0][6:]) == int(lastPair[0][6:]) + 1
                or int(pair[0][6:]) == int(lastPair[0][6:]) - 1)
        lastPair = pair
    # ... and that they only include the top test_N ranks
    assert ranks == test_N
