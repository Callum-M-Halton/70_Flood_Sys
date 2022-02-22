
"""
This module provides functions for processing station relative river
level data to identify high flood risk locations
"""

def stations_level_over_threshold(stations, tol):
	"""
	Returns a list of tuples, where each tuple holds 
	(i) a station (object) at which the latest relative water level is over tol and
	(ii) the relative water level at the station. The returned list is sorted by
	the relative level in descending order and contains only stations with 
	consistent typical low/high data.
	"""
	high_level_stations = []
	for station in stations:
		if station.typical_range_consistent:
			rel_level = station.relative_water_level()
			if rel_level != None and rel_level > tol:
				high_level_stations.append((station, rel_level))
	
	high_level_stations.sort(reverse=True, key=(lambda tup : tup[1]))
	return high_level_stations

def stations_highest_rel_level(stations, N):
	"""
	Returns a list of the N stations (objects) at which the water level,
	relative to the typical range, is highest. The list is sorted in
	descending order by relative level. 
	"""
	# Create a list with each element a list pair [Station, Boulean]
	# where the boulean indicates whether the Station has already been 
	# added to high_level_stations
	stations_with_bool = [[station, False] for station in stations]
	# Initialises count of stations not already added to high_level_stations
	remaining_stations = len(stations)
	high_level_stations = []
	for x in range(N):
		if remaining_stations == 0:
			break
		else:
			highest_rel_level = 0
			for i, (station, added) in enumerate(stations_with_bool):
				# Only considers station if not already in high_level_stations
				if not added:
					rel_level = station.relative_water_level()
					if rel_level != None and rel_level >= highest_rel_level:
						# Records pair index and raises highest_rel_level
						highest_rel_level_index = i
						highest_rel_level = rel_level
			# gets station, added pair at the index recorded for the highest_rel_level
			highest_rel_level_pair = stations_with_bool[highest_rel_level_index]   
			# Adds the station from the pair to high_level_stations
			high_level_stations.append(highest_rel_level_pair[0])
			# Sets added in the pair to True so it will be skipped in future passes
			highest_rel_level_pair[1] = True
			remaining_stations -= 1
	
	return high_level_stations
    


			
	