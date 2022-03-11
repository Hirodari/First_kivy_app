__author__ = "HiroYito B"
__version__ = "0.1.0"
__date__ = "2021-03-06"

from common.database import Database


class ConnectivityError(Exception):
    pass


class Model(Database):

    @classmethod
    def save_to_mongo(cls):
        # return cls.update(cls.collection, {"_id": cls._id}, cls.json())
        return cls.insert(cls.collection, cls.json())

    @classmethod
    def remove_from_mongo(cls):
        return cls.remove(cls.collection, {"_id": cls._id})

    @classmethod
    def find_many(cls, attribute, value):
        return [cls(**element) for element in cls.find(cls.collection, {attribute: value})]

    @classmethod
    def get_by_id(cls, id):
        return cls.find_one({"_id": id})

    @classmethod
    def find_by_email(cls, attribute, value):
        try:
            return Database.db[cls.collection].find_one({attribute: value})
        except Exception:
            raise ValueError("Failed: Check your network settings")

    @classmethod
    def find_attr(cls, attribute, value):
        try:
            return Database.db[cls.collection].find_one({attribute: value})
        except Exception as ex:
            return ex

    @classmethod
    def all(cls):
        return [cls(**item) for item in cls.find(cls.collection, {})]


