from dotenv import load_dotenv
load_dotenv(r'C:\Users\alici\Documents\estudiar\invencao\api\Repository\.env')  

from pymongo import MongoClient
from pymongo.collection import Collection
import os
   
url = f"mongodb+srv://{str(os.environ.get('DB_USER'))}:{str(os.environ.get('DB_PWD'))}@cluster0.gsi3dxn.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.get_database(str(os.environ.get('DB_NAME')))
collection = Collection(db, 'synonyms_coll')

def add(word):
    collection.insert_one(word.__dict__)

def find(word):
    return collection.find_one({ "word": word })

    