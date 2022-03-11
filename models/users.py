__author__ = "HiroYito B"
__version__ = "0.1.0"
__date__ = "2021-03-06"

from .model import Model
from common.utils import Utils
from datetime import datetime
import uuid


class User(Model):
    email = None
    password = None
    created = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    _id = uuid.uuid4().hex
    collection = "users"

    @classmethod
    def register(cls, email, password):
        cls.email = email
        cls.password = Utils.hash_password(password)

        if not Utils.valid_email(cls.email):
            raise ValueError("Email not valid")

        if isinstance(cls.find_by_email("email", cls.email), dict):
            # print("calling find by email")
            raise ValueError("Email exists, please login")

        if isinstance(cls.find_by_email("email", cls.email), int):
            raise ValueError("There is a connectivity issue")

        if cls.save_to_mongo():
            return True
        else:
            return False

    @classmethod
    def login(cls, email, password):
        if Utils.valid_email(email) and cls.find_by_email("email", email):
            hash_password = cls.find_attr("email", email)['password']
            return Utils.check_hashed_password(password, hash_password)
        print("login check did not valid")
        return False

    @classmethod
    def json(cls):
        return {
            '_id': cls._id,
            'email': cls.email,
            'password': cls.password,
            'created': cls.created
        }
