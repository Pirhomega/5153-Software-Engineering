from pymongo import MongoClient
from bson.objectid import ObjectId
import random
connection = "mongodb+srv://cmatamoros:M20143170!@innoventory-vvoxp.azure.mongodb.net/test?retryWrites=true&w=majority"

client = MongoClient(connection)
db = client.Innoventory
collection = db.Products

count = 0

# for doc in collection.find():
#     print(count)
#     pk = ObjectId(str(doc.get("_id")))
#     g = doc.get('item')
#     if g:
#         g = g.lower()
#         collection.update({"_id": pk}, {"$set":{"item":g}})
#         count += 1

for doc in collection.find():
    print(count)
    pk = ObjectId(str(doc.get("_id")))
    if 'quantity' not in doc:
        collection.update({"_id": pk}, {"$set":{"quantity":random.randint(0, 999999)}})
        count += 1
