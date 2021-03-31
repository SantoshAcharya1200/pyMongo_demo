import pymongo
from pymongo import MongoClient

cl=MongoClient()
db=cl.mydb
cl=db.names

result=cl.insert_many(posts)
print(result._id)