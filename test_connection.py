__author__ = "HiroYito B"
__version__ = "0.1.0"
__date__ = "2021-03-06"

'''
    Test database connectivity  and other functionalities
'''

from models.users import User


class TestMyDatabase(User):

    def signup(self):
        email = input("Enter email: ")
        password = input("Enter password: ")
        # collection = "users"
        try:
            if self.register(email, password):
                print(f"{email} registered!")
            else:
                print("not register")
        except ValueError as ex:
            print(ex)


if __name__ == "__main__":
    TestMyDatabase().signup()
