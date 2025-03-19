from pymongo import MongoClient
from pymongo.server_api import ServerApi


def connect_to_mongodb(db_name, collection_name):
    uri = "mongodb+srv://VVBF997:Hefe4976B#@hospitalinformationsyst.rqpcw.mongodb.net/?retryWrites=true&w=majority&appName=HospitalInformationSystem"
    client = MongoClient(uri, server_api=ServerApi('1'))
    db = client["SamplePatientService"]
    collection = db["patients"]
    return collection
