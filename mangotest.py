import pymongo
client = pymongo.MongoClient("mongodb+srv://GOVARDHAN:mangodbgovu@govardhan.wrmjwgs.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)
d = {
    "name" : "Govardhan",
    "email" : "govu@92",
    "surname" : "govu"

}

db1 = client['mangotest']
cell = db1['test']
cell.insert_one(d )