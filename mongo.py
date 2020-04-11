from flask import Flask
import pymongo
import os

app = Flask(__name__)

#app.route("/")
def hello():
    return "Acme Business Directory"

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'), 
    port=int(os.environ.get('PORT')),
    debug=True)



MONGO_URI = os.getenv("MONGO_URI")
DBS_NAME = "acmeBD"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %") % e

conn = mongo_connect(MONGO_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]


documents = coll.find()

for doc in documents:
    print(doc)


