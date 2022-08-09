from gc import collect
from time import sleep
from xml.dom.minidom import Element
from geopy.geocoders import Nominatim
from geopy import distance
import csv

from pyparsing import line

def get_latitude(x):
    if hasattr(x,'latitude') and (x.latitude is not None): 
        return x.latitude

def get_longitude(x):
    if hasattr(x,'longitude') and (x.longitude is not None): 
        return x.longitude

class Range:
    def __init__(self,address,max_distance):
        locator = Nominatim(user_agent = "myApp")
        location = locator.geocode(address)
        coordinate1 = (get_latitude(location), get_longitude(location))

        self.count = 0
        self.collection = []
        with open('./data/hotel.csv','r') as file:
            reader = csv.reader(file)

            next(reader) # Skips the first iteration

            for line in reader:
                # Getting coordinates of Hotels present in csv file
                coordinate2 = (line[11],line[12]) # (Latitude, Longitude)

                d = distance.geodesic(coordinate1, coordinate2)

                if(d < max_distance):
                    element = {}
                    l = line

                    element["distance_km"] = round(d.km,2)
                    element["latitude"] = l[11]
                    element["longitude"] = l[12]
                    element["property_type"] = l[1]
                    element["property_name"] = l[0]
                    element["address"] = l[7]
                    element["area"] = l[8]
                    element["city"] = l[9]
                    element["check_in"] = l[2]
                    element["check_out"] = l[3]

                    if(l[4] != '' and l[5] != ''): 
                        element["room_type"] = l[4]
                        element["room_count"] = float(l[5])
                    if(l[6] != ''):
                        element["room_area"] = l[6]

                    if (l[13] != ''):
                        element["overall_rating"] = float(l[13])
                        element["max_rating"] = 5
                        element["reviews"] = int(l[14])

                    if(l[15] != ''):
                        l[15] += '|'
                        dic={}
                        ls = ['service_quality', 'amenities', 'food_and_drinks', 'value_for_money', 'location', 'cleanliness']
                        i = 0
                        k = ''
                        for a in l[15]:
                            if a == '|':
                                s = ls[i] + '_rating'
                                dic[s] = float(k)
                                i+=1
                                k = ''
                            else:
                                k+=a
                        element["specific_rating"] = dic;

                    if(l[16] != '' or l[17] != ''): 
                        ls = []
                        o = l[16] + "|" + l[17]
                        p = ''

                        for a in o:
                            if a == '|':
                                if p != '':
                                    ls.append(p.strip())
                                p = ''
                            else:
                                p+=a    

                        element["facilities"] = ls

                    if(l[18] != ''):
                        ls = []
                        p = ''

                        for a in l[18]:
                            if a == '|':
                                if p != '':
                                    ls.append(p.strip())
                                p = ''
                            else:
                                p+=a    

                        element["point_of_interest"] = ls

                    self.count+=1;
                    self.collection.append(element)
