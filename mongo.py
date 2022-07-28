import pymongo
client = pymongo.MongoClient("mongodb+srv://rishcool:Rishcool#8691@cluster0.h5d5h.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

d = {
   "name" : "akki",
   "email" : "akkigpt688@gmail.com",
   "surname" : "gupta"
}
db1= client['mongotest']
coll=db1['test']
coll.insert_one(d)
