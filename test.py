import numpy as np
from python_tsp.distances import great_circle_distance_matrix
from python_tsp.exact import solve_tsp_dynamic_programming
import config
from Geofence_Checker import Geofence_Checker
import requests
import config

Checker = Geofence_Checker()

def get_all_stops():
    SucheLink = config.SERVER+"/pokestops"
    all_stops = requests.get(SucheLink).json()
    return(all_stops)

def get_latitude(stop):
    return(stop[2])

def get_longitude(stop):
    return(stop[3])

def check_stops(all_stops):
    in_fence = []
    for pokestop in all_stops:
        if Checker.is_point_in_fence(latitude=get_latitude(pokestop), longitude=get_longitude(pokestop)):
            in_fence.append(pokestop)

    print("Stops found: "+str(len(in_fence)))

    return(in_fence)

def create_sources(stops):
    coordinates = []
    for pokestop in stops:
        test = [get_latitude(pokestop),get_longitude(pokestop)]
        coordinates.append(test)
        
    sources = np.asarray(coordinates)
    print(sources)
    return(sources)

all_stops = get_all_stops()
in_fence = check_stops(all_stops)
#sources = create_sources(in_fence)

distance_matrix = great_circle_distance_matrix(sources)
print(str(distance_matrix))
permutation, distance = solve_tsp_dynamic_programming(distance_matrix)
print(permutation)
print(distance)