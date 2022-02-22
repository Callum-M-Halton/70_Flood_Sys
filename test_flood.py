"""Unit test for the flood module"""
from floodsystem.flood import stations_level_over_threshold
from utils_for_tests import StockStation

def test_stations_level_over_threshold():
  """
  Tests the stations_level_over_threshold method of flood.py
  """
  # each station_data_by_name key is the name to be given to the test station and 
  # has a tuple value composed of the typical range of the station
  # followed by the water level to be assigned to the station
  # followed by the relative water level that would be calculated from 
  # the typical range and water level
  station_data_by_name = {
    'a' : ((1 , 5 ), 2 , 0.25 ),
    'b' : ((4 , 12), 7 , 0.375),
    'c' : ((19, 20), 21, 2    ),
    'd' : ((1 , 24), 4 , 0.125),
    'e' : ((5 , 9 ), 7 , 0.5  ),
    'f' : ((2 , 8 ), 6 , 0.667),
    'g' : ((4, 10 ), 5 , 0.167),
    'h' : ((1 , 5 ), 4 , 0.75 ),
    'i' : ((0 , 10), 10, 1    ),
    'j' : ((16, 20), 22, 1.5  ),
  }
  # Defines test tolerance
  tol = 0.5

  # Initialise test station list
  stations = []
  # for each test in station_data_by_name, construct the test station from the 
  # name (key) and typical_range (first tuple element) and assign the 
  # latest_level (2nd tuple element) and add it to the stations list
  for name in station_data_by_name:
    station_data = station_data_by_name[name]
    test_station = StockStation({'name': name, 'typical_range' : station_data[0]})
    test_station.latest_level = station_data[1]
    stations.append(test_station)
  
  # test stations_level_over_threshold on the stations list
  stations_over_tol = stations_level_over_threshold(stations, tol)

  # Initilises last relative level as a large value
  last_rel_level = 10000000000
  for station, rel_level in stations_over_tol:
      # Checks relative level calculated is roughly the vaule expected
      assert abs(rel_level - station_data_by_name[station.name][2]) < 0.01
      # Checks relative level is indeed greater than tol
      assert rel_level > tol
      # Checks stations_over_tol is ordered descending by relative level
      assert rel_level <= last_rel_level
      last_rel_level = rel_level