from Geofence_Checker import Geofence_Checker
import requests
import config

Checker = Geofence_Checker()
in_fence = []
final_list = []
SucheLink = config.SERVER+"/pokestops"
allpokemon = requests.get(SucheLink).json()


def get_latitude(stop):
    return(stop[2])

def get_longitude(stop):
    return(stop[3])


for pokestop in allpokemon:
    print(pokestop)

    pokestopid =pokestop[0]
    enabled =pokestop[1]
    latitude=pokestop[2]
    longitude=pokestop[3]
    last_modified=pokestop[4]
    lure_expiration=pokestop[5]
    active_fort_modifier=pokestop[6]
    last_updated=pokestop[7]
    name =pokestop[8]
    image=pokestop[9]
    incident_start=pokestop[10]
    incident_expiration=pokestop[11]
    incident_grunt_type=pokestop[12]
    is_ar_scan_eligible=pokestop[13]

    if Checker.is_point_in_fence(latitude=latitude, longitude=longitude):
        print("In Fence")
        in_fence.append(pokestop)

print(len(in_fence))

in_fence.sort(key=get_latitude)
print(in_fence)

for stop in in_fence:
    #test = (get_latitude(stop),get_longitude(stop))
    #final_list.append(test)
    string_to_write = str(get_latitude(stop))+","+str(get_longitude(stop))+"\n"
    f = open("route.txt", "a")
    f.write(str(string_to_write))
    f.close()

