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

    assert closest_ten == [('Cambridge Jesus Lock', 'Cambridge', 0.840237595667494), ('Bin Brook', 'Cambridge', 2.502277543239629), ("Cambridge Byron's Pool", 'Grantchester', 4.07204948005424), ('Cambridge Baits Bite', 'Milton', 5.115596582531859), ('Girton', 'Girton', 5.227077565748483), ('Haslingfield Burnt Mill', 'Haslingfield', 7.0443978959918025), ('Oakington', 'Oakington', 7.12825901765745), ('Stapleford', 'Stapleford', 7.265704342799649), ('Comberton', 'Comberton', 7.735085060177142), ('Dernford', 'Great Shelford', 7.993872393303291)]
    assert furthest_ten == [('Boscadjack', 'Wendron', 440.00325604140033), ('Gwithian', 'Gwithian', 442.0555261735786), ('Helston County Bridge', 'Helston', 443.3788620846717), ('Loe Pool', 'Helston', 445.0724593420217), ('Relubbus', 'Relubbus', 448.6500629265487), ('St Erth', 'St Erth', 449.0347773512542), ('St Ives Consols Farm', 'St Ives', 450.07409071624505), ('Penzance Tesco', 'Penzance', 456.38638836619003), ('Penzance Alverton', 'Penzance', 458.57727568406375), ('Penberth', 'Penberth', 467.53431870130544)]


test_distance()