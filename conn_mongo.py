from pymongo import MongoClient
import numpy as np

client = MongoClient("mongodb://localhost:27017")
db = client['test']
cursor = db.inflacao.find()
for document in cursor:
	print(document)


def mmq(x, y):
    x = np.insert(x, 0, 1, axis=1)
    x_t = np.transpose(x)
    xt_x = np.dot(x_t, x)
    inverse_xt_x = np.linalg.inv(xt_x)
    xt_y = np.dot(x_t, y)
    return np.dot(inverse_xt_x, xt_y)
