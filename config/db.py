from pymongo import MongoClient
from urllib.parse import quote_plus
from config.settings import settings

uri = "mongodb://%s:%s@%s" % (
    quote_plus(settings.MONGO_USERNAME), 
    quote_plus(settings.MONGO_PASSWORD), 
    settings.MONGO_HOST)

conn = MongoClient(uri)
users = conn[settings.MONGO_DATABASE].users