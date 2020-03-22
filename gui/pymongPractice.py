import pymongo
from pprint import pprint

username = "passwordHell"
password = r"XR9lYeOp036C%25%40%26%40cQn%2A8z3BU4%5C"
global client, db, categoryNames
client = pymongo.MongoClient(f"mongodb+srv://{username}:{password}@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority")
db = client.Innoventory
categoryNames = db.list_collection_names()

dicta= {}
for name,i in zip(categoryNames, range(0,len(categoryNames))):
    print(i, name)
    dicta[i] = name

# collection = dicta[1]
# print(type(collection))

# cursor = db[collection].find({})
# for curse in cursor:
#     print (curse)

vehic = db
x = db["vehicles"].find( { "$text": { "$search": "Honda" } } )
print(x)