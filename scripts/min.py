from geopy.geocoders import Nominatim
from geopy import distance
import csv

def get_latitude(x):
  if hasattr(x,'latitude') and (x.latitude is not None): 
     return x.latitude

def get_longitude(x):
  if hasattr(x,'longitude') and (x.longitude is not None): 
     return x.longitude

class Min:
    def __init__(self,address):
        locator = Nominatim(user_agent = "myApp")
        location = locator.geocode(address)
        coordinate1 = (get_latitude(location), get_longitude(location))

        with open('./data/hotel.csv','r') as file:
            reader = csv.reader(file)

            next(reader) # Skips the first iteration

            min_distance = 99999999.99

            for line in reader:
                # Getting coordinates of Hotels present in csv file
                coordinate2 = (line[11],line[12]) # (Latitude, Longitude)

                d = distance.geodesic(coordinate1, coordinate2)

                if(min_distance > d):
                    min_distance = d
                    l = line

        self.distance_km = round(min_distance.km,2)
        self.latitude = l[11]
        self.longitude = l[12]
        self.property_type = l[1]
        self.property_name = l[0]
        self.address = l[7]
        self.area = l[8]
        self.city = l[9]
        self.check_in = l[2]
        self.check_out = l[3]

        if(l[4] != '' and l[5] != ''): 
            self.room_type = l[4]
            self.room_count = float(l[5])
        if(l[6] != ''):
            self.room_area = l[6]

        if (l[13] != ''):
            self.overall_rating = float(l[13])
            self.max_rating = 5
            self.reviews = int(l[14])

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
            self.specific_rating = dic;

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

            self.facilities = ls

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

            self.point_of_interest = ls

    # def to_json(self):
    #     j = json.dumps(self.__dict__,indent=4)
    #     # print(j)
    #     return j

# r1 = Min("Matunga, Mumbai")
# r1.to_json()