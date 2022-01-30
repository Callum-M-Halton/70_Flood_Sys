# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""Unit test for the station module"""


from floodsystem.station import MonitoringStation, inconsistent_typical_range_stations
from floodsystem.stationdata import build_station_list


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
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-2.0, 4.0)
    trange1 = (-2.3, 3.4445)
    trange2 = None
    trange3 = (3.4445, -2.3)
    river = "River X"
    town = "My Town"
    s1 = MonitoringStation(s_id, m_id, label, coord, trange1, river, town)
    s2 = MonitoringStation(s_id, m_id, label, coord, trange2, river, town)
    s3 = MonitoringStation(s_id, m_id, label, coord, trange3, river, town)

    assert s1.typical_range_consistent() 
    assert not s2.typical_range_consistent()
    assert not s3.typical_range_consistent()

def test_inconsistent_typical_range_stations():
    """
    Tests the inconsistent_typical_range function in station.py
    """
    stations = build_station_list()
    list_of_stations = inconsistent_typical_range_stations(stations)
    
    for station in list_of_stations:
        assert station.typical_range_consistent() == False
