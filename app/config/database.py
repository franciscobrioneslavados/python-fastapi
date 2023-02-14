from pymongo import mongo_client
import pymongo
from app.config import settings

client = mongo_client.MongoClient(settings.MONGO_URL)
print('Connected to MongoDB...')

db = client[settings.MONGO_DATABASE]
Todo = db.todo