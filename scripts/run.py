from geopy.geocoders import Nominatim
from geopy import distance
import csv

from app import min_distance


def hotels(address,distance=999999.99):

    result = {
        "address":address,
        "distance":distance
    }

    return result

