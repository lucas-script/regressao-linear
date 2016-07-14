from pymongo import MongoClient
import numpy

client = MongoClient("mongodb://localhost:27017")
db = client['quali']
cursor = db.turmas.find()
for document in cursor:
	print(document['_id'])
