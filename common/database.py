__author__ = "HiroYito B"
__version__ = "0.1.0"
__date__ = "2021-03-06"

from pymongo import MongoClient
import os

'''
    Database class contains data manipulation logic to and from Mongo
    Any issues from the database, this is the initial point of observation
'''


class Database:
        # to set up env in Ubuntu see below
        # sudo gedit ~/.bashrc
        # export MONGO_USERNAME=USERNAME
    uri = f"mongodb+srv://{os.getenv('MONGO_USERNAME')}:{os.getenv('MONGO_PASSWORD')}@cluster0.nxudg.mongodb.net/test"
    client = MongoClient(uri)
    db = client.android


    @staticmethod
    def insert(collection, data):
        # try:
        return Database.db[collection].insert_one(data)
        # except Exception as ex:
        #     print(ex.details['errmsg'])
        #     return False

    @staticmethod
    def find_one(collection, query):
        return Database.db[collection].find_one(query)

    @staticmethod
    def update(collection, query, data):

        print(f"calling update ..., {collection}")
        return Database.db[collection].update(query, data, upsert=True)

    @staticmethod
    def remove(collection, query):
        try:
            return Database.db[collection].remove(query)
        except Exception as ex:
            return ex

