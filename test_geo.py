
from distutils.command.build import build
from floodsystem.geo import stations_by_distance, stations_within_radius, rivers_with_station, stations_by_river, rivers_by_station_number
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

def test_rivers_with_station():
    """
    Tests the rivers_with_station function in geo.py
    """
    rivers_with_station_set = rivers_with_station(build_station_list())
    # Checks container type
    assert type(rivers_with_station_set) == set
    # Checks number of rivers contained
    assert len(rivers_with_station_set) == 949
    # Checks last 20 rivers alpabetically
    assert sorted(rivers_with_station_set)[-20:] == ['Winterbourne Stream', 'Withy Brook', 'Withycombe Brook', 'Wiza Beck', 'Wood Brook', 'Woodbridge Brook', 'Wool Brook', 'Wooler Water', 'Wootton Brook', 'Worsley Brook', 'Wortley Beck', 'Wotton Brook', 'Wraysbury River', 'Wydon Burn', 'Wyke Beck', 'Wymans Brook', 'Yazor Brook', 'Yeading Brook', 'Yeading Brook (Eastern Arm)', 'Yeolands Stream']


def test_stations_by_river():
    """
    Tests the stations_by_river function in geo.py
    """
    stations_by_rivername = stations_by_river(build_station_list())
    # Checks stations_by_rivername is a dict
    assert type(stations_by_rivername) == dict
    # Checks river sets for the 3 rivers in the demo
    expected_stations = {
        'River Aire'   : ['Airmyn', 'Apperley Bridge', 'Armley', 'Beal Weir Bridge', 'Bingley', 'Birkin Holme Washlands', 'Carlton Bridge', 'Castleford', 'Chapel Haddlesey', 'Cononley', 'Cottingley Bridge', 'Ferrybridge Lock', 'Fleet Weir', 'Gargrave', 'Kildwick', 'Kirkstall Abbey', 'Knottingley Lock', 'Leeds Crown Point', 'Leeds Crown Point Flood Alleviation Scheme', 'Leeds Knostrop Weir Flood Alleviation Scheme', 'Oulton Lemonroyd', 'Saltaire', 'Snaygill', 'Stockbridge'],
        'River Cam'    : ['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Great Chesterford', 'Weston Bampfylde'],
        'River Thames' : ['Abingdon Lock', 'Bell Weir', 'Benson Lock', 'Boulters Lock', 'Bray Lock', 'Buscot Lock', 'Caversham Lock', 'Chertsey Lock', 'Cleeve Lock', 'Clifton Lock', 'Cookham Lock', 'Cricklade', 'Culham Lock', 'Days Lock', 'Ewen', 'Eynsham Lock', 'Farmoor', 'Godstow Lock', 'Goring Lock', 'Grafton Lock', 'Hannington Bridge', 'Hurley Lock', 'Iffley Lock', 'Kings Lock', 'Kingston', 'Maidenhead', 'Mapledurham Lock', 'Marlow Lock', 'Marsh Lock', 'Molesey Lock', 'Northmoor Lock', 'Old Windsor Lock', 'Osney Lock', 'Penton Hook', 'Pinkhill Lock', 'Radcot Lock', 'Reading', 'Romney Lock', 'Rushey Lock', 'Sandford-on-Thames', 'Shepperton Lock', 'Shifford Lock', 'Shiplake Lock', 'Somerford Keynes', 'Sonning Lock', 'St Johns Lock', 'Staines', 'Sunbury  Lock', 'Sutton Courtenay', 'Teddington Lock', 'Thames Ditton Island', 'Trowlock Island', 'Walton', 'Whitchurch Lock', 'Windsor Park']
    }
    for rivername in expected_stations:
        assert sorted(stations_by_rivername[rivername]) == expected_stations[rivername]

'''
def test_rivers_by_station_number():
    """
    Tests the rivers_by_station_number function in geo.py
    """
'''