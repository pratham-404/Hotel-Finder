import pymongo

client = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = client["hotel"]
mycol = mydb["property"]

def print_col(c):
    for i in c:
        print(i["latitude"])

# findAll
y = mycol.find()
print_col(y)