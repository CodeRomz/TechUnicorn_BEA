from pymongo import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://cluster0.wpk3oxf.mongodb.net/?authSource=%24external&authMechanism=MONGODB-X509&retryWrites=true&w=majority"

TubeaClient = MongoClient(uri, tls=True, tlsCertificateKeyFile='X509-cert-4444215937045702419.pem',
                          server_api=ServerApi('1'))
TubeaDb = TubeaClient['TechUnicorn_BEA']

class TubeaDbExec:

    def __init__(self, db_collection):
        self.db_collection = db_collection
        self.collection = TubeaDb[str(self.db_collection)]

    def view_user_data(self, user_id):
        self.user_id = user_id
        self.view_user_data = self.collection.find_one({"_id": self.user_id})
        return self.view_user_data

    def verify_login_data(self, user_name):
        self.user_name = user_name
        self.view_user_data = self.collection.find_one({"user_name": self.user_name})
        return self.view_user_data

    def view_all_data(self):
        db_all_data = list(self.collection.find())
        return db_all_data

    def view_all_access(self, user_access):
        self.user_access = user_access
        db_all_data = list(self.collection.find({"user_access": self.user_access}, {'_id': 1, 'user_name': 1}))
        return db_all_data

    def view_byUser_byAccess(self, user_id, user_access):
        self.user_access = user_access
        self.user_id = user_id
        db_all_data = list(self.collection.find({"user_access": self.user_access, "_id" : self.user_id}, {'_id': 1, 'user_name': 1}))
        return db_all_data

    def view_appointment_byDoctorId(self, doctor_id):
        self.doctor_id = doctor_id
        db_all_data = list(self.collection.find({"doctor_id" : self.doctor_id}))
        return db_all_data

    def add_user_data(self, user_id, user_name, user_password, user_access):
        self.collection.insert_one(
            {
            '_id': user_id,
            'user_name': user_name,
            'user_password': user_password,
            'user_access': user_access
        }
        )

    def book_appointment(self, appointment_id, doctor_id, patient_id, date, start_time, end_time, status):
        self.collection.insert_one(
            {
                "_id": appointment_id,
                "doctor_id": doctor_id,
                "patient_id": patient_id,
                "date": date,
                "start_time": start_time,
                "end_time": end_time,
                "status": status
            }
        )



