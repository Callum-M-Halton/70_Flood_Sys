
from distutils.command.build import build
from floodsystem.geo import stations_by_distance, stations_within_radius
from floodsystem.stationdata import build_station_list


def test_stations_by_distance():
    """
    Tests the stations by distance function in geo.py
    """
    stations = build_station_list()
    p = (52.2053, 0.1218) #Coordinate of Cambridge city centre
    station_distances = stations_by_distance(stations, p)

    closest_ten = [] 
    furthest_ten = []
    
    for pair in station_distances[:10]: #Appends 10 closest stations to a list
        closest_ten.append((pair[0].name, pair[0].town, pair[1]))
    
    for pair in station_distances[-10:]: #Appends 10 furthest stations to a list
        furthest_ten.append((pair[0].name, pair[0].town, pair[1]))

    assert closest_ten == [('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494), ('Bin Brook', 'Cambridge', 2.502277543239629), ("Cambridge Byron's Pool", 'Grantchester', 4.07204948005424), ('Cambridge Baits Bite', 'Milton', 5.115596582531859), ('Girton', 'Girton', 5.227077565748483), ('Haslingfield Burnt Mill', 'Haslingfield', 7.0443978959918025), ('Oakington', 'Oakington', 7.12825901765745), ('Stapleford', 'Stapleford', 7.265704342799649), ('Comberton', 'Comberton', 7.735085060177142), ('Dernford', 'Great Shelford', 7.993872393303291)]
    assert furthest_ten == [('Boscadjack', 'Wendron', 440.00325604140033), ('Gwithian', 'Gwithian', 442.0555261735786), ('Helston County Bridge', 'Helston', 443.3788620846717), ('Loe Pool', 'Helston', 445.0724593420217), ('Relubbus', 'Relubbus', 448.6500629265487), ('St Erth', 'St Erth', 449.0347773512542), ('St Ives Consols Farm', 'St Ives', 450.07409071624505), ('Penzance Tesco', 'Penzance', 456.38638836619003), ('Penzance Alverton', 'Penzance', 458.57727568406375), ('Penberth', 'Penberth', 467.53431870130544)]


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
