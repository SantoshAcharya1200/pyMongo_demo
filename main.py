#mongodb+srv://santosh1200:<password>@cluster0.gphvu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority


import pymongo
from pymongo import MongoClient
import datetime

new_date= datetime.datetime.now()
old_date=datetime.datetime(2016,8,22)


cluster = MongoClient("mongodb+srv://santosh1200:<password>@cluster0.gphvu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = cluster["test"]
collection = db["test"]
post1 = {"_id":1,"name":"Santosh","age":25}
post2 = {"_id":2,"name":"Ram","age":256}
post6 = {"_id":22,"name":"new","age":256,"date":new_date}

post3={"_id":24,"hobby":["music","movies","pizza"],"age":34}

a=collection.count_documents({"date":{"$gte":old_date}})
print(a)


