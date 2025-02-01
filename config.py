import pymongo
import certifi

def get_db():
    client = pymongo.MongoClient("mongodb+srv://aramburoeduardo972:Faramburo01@cluster0.zofne.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0", tlsCAFile=certifi.where())
    db = client["mydatabase"]
    return db