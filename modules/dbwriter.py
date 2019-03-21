import pymongo
import logging

MONGO_DB_CONNECT_STRING = 'mongodb+srv://exdunn:exdunn@exaltcluster-e03v8.mongodb.net/test?retryWrites=true'
DB_NAME = 'exaltDB'


class DBWriter:
    def __init__(self, connect_string, db_name):
        print("CONNECT STRING: " + connect_string)
        client = pymongo.MongoClient(connect_string)
        self.db = client[db_name]

    def fetch_collection(self, col_name):
        try:
            return self.db[col_name]
        except Exception as e:
            logging.exception("Error caught in fetch_collection: " + e)

    def write_data(self, col_name, data):
        print("DBWriter write_data")
        try:
            collection = self.fetch_collection(col_name)
            for item in data:
                result = collection.insert_one(item)
        except Exception as e:
            logging.exception("Error caught in write_data: " + e)

    def overwrite_data(self, col_name, data):
        print("DBWriter overwrite_data")
        self.clear(col_name)
        self.write_data(col_name, data)

    def clear(self, col_name):
        print("DBWriter Clear")
        try:
            collection = self.fetch_collection(col_name)
            collection.delete_many({})
        except Exception as e:
            logging.exception("Error caught in clear: " + e)
