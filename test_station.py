# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""


from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list
from utils_for_tests import StockStation


def test_create_monitoring_station():

    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "My Town"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)

    assert s.station_id == s_id
    assert s.measure_id == m_id
    assert s.name == label
    assert s.coord == coord
    assert s.typical_range == trange
    assert s.river == river
    assert s.town == town

def test_typical_range_consistent():
    """
    Tests the typical_range_consistent method in station.py
    """
    #Create stations with different typical ranges

    dict_1 = {"name" : "Station1",
              "typical_range" : (-2.3, 3.4445) 
                } #Station 1 should work as normal as high > low
    dict_2 = {"name" : "Station2",
              "typical_range" : (3.4445, -2.3) 
                } #Station 2 should fail as high < low
    dict_3 = {"name" : "Station2",
            "typical_range" : None
                } #Station 3 should fail as typical_range doesnt exist

    station1 = StockStation(dict_1)
    station2 = StockStation(dict_2)
    station3 = StockStation(dict_3)
    assert station1.typical_range_consistent() 
    assert not station2.typical_range_consistent() 
    assert not station3.typical_range_consistent()

def test_inconsistent_typical_range_stations():
    """
    Tests the inconsistent_typical_range function in station.py
    """
    dict_1 = {"name" : "Station1",
              "typical_range" : (-2.3, 3.4445) 
                } #Station 1 is consistent as high > low
    dict_2 = {"name" : "Station2",
              "typical_range" : (3.4445, -2.3) 
                }   #Should be returned in the list as low < high, therefore inconsistent
    station1 = StockStation(dict_1)
    station2 = StockStation(dict_2)
    inconsistent = inconsistent_typical_range_stations([station1, station2])
    assert len(inconsistent) == 1
    assert inconsistent[0] == station2

def test_relative_water_level():
  """
  Tests the relative_water_level method of station.py
  """
  # each test data element 'test' is composed of the typical range of the station
  # followed by the water level to be assigned to the station
  # followed by the relative water level expected to be calculated from 
  # the typical range and water level
  test_data = (
    ((1, 2), 1,   0   ),
    ((2, 3), 2.5, 0.5 ),
    ((3, 4), 4,   1   )
  )
  
  # for each test in test data, construct the test station and check
  # its relative water level equals the expected level. 
  for test in test_data:
    test_station = StockStation({'typical_range' : test[0]})
    test_station.latest_level = test[1]
    assert test_station.relative_water_level() == test[2]
