from turfpy.measurement import boolean_point_in_polygon
from geojson import Point, Polygon, Feature

import config


class Geofence_Checker():
    def __init__(self):
        self.my_geofende = Polygon(config.polygon)


    def is_point_in_fence(self,latitude,longitude):
        point = Feature(geometry=Point((float(latitude),float(longitude))))
        Ergebnis = boolean_point_in_polygon(point, self.my_geofende)
        #print(Ergebnis)
        return(Ergebnis)


#TEST = Geofence_Checker()
#TEST.is_point_in_fence("52.345285","14.5427683")
