from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://cluster0.wpk3oxf.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"

TubeaClient = MongoClient(uri, tls=True, tlsCertificateKeyFile='X509-cert-5961867564190636061.pem',
                          server_api=ServerApi('1'))
TubeaDb = TubeaClient['TechUnicorn_BEA']

class TubeaDbExec:

    def __init__(self, db_collection):
        self.db_collection = db_collection
        self.collection = TubeaDb[str(self.db_collection)]

    def view_data(self, user_id):
        self.user_id = user_id
        self.view_user_data = self.collection.find_one({"_id": self.user_id})
        return self.view_user_data
    def verify_login_data(self, user_name):
        self.user_name = user_name
        self.view_user_data = self.collection.find_one({"user_name": self.user_name})
        return self.view_user_data

    # add/post data in mongo
    def add_data(self, user_id, user_name, user_password):
        self.collection.insert_one(
            {
            '_id': user_id,
            'user_name': user_name,
            'user_password': user_password
        }
        )

    # def update_data(self):
    #     print("update data" , self.view_user)
    #
    # def delete_data(self):
    #     print("delete data", self.view_user)

