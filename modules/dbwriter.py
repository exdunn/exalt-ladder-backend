import pymongo
import logging

MONGO_DB_CONNECT_STRING = 'mongodb+srv://exdunn:exdunn@exaltcluster-e03v8.mongodb.net/test?retryWrites=true'
DB_NAME = 'exaltDB'


class DBWriter:
    def __init__(self, connect_string, db_name):
        print("CONNECT STRING: " + connect_string)
        self.client = pymongo.MongoClient(connect_string)
        self.db_name = db_name
        self.db = self.client[self.db_name]

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

    def update_data(self, col_name):
        print("DBWriter update_data")
        try:
            new_db = self.client[self.db_name]
            new_collection = new_db[col_name]
            old_collection = self.db[col_name]

            for i in range(1, 10):
                new_collection.update_one({'rank': i}, {"$set": {"character.name": i}})

            # for entry in new_collection.find({}):
            #     rank = 11 - entry['rank']
            #     print(new_collection.update(
            #         {"$set": {"character.name": 'alex'},
            #          '$set': {"dead": False}}))
        except Exception as e:
            logging.exception(e)


def clear(self, col_name):
    print("DBWriter Clear")
    try:
        collection = self.fetch_collection(col_name)
        collection.delete_many({})
    except Exception as e:
        logging.exception("Error caught in clear: " + e)
