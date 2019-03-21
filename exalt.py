from dbwriter import DBWriter
from requestsender import RequestSender
import time

MONGO_DB_CONNECT_STRING = 'mongodb+srv://exdunn:exdunn@exaltcluster-e03v8.mongodb.net/test?retryWrites=true'
DB_NAME = 'exaltDB'


def main():
    start = time.time()
    writer = DBWriter(MONGO_DB_CONNECT_STRING, DB_NAME)
    leagues = RequestSender.get_leagues()

    for league in leagues:
        data = RequestSender.get_entries(league, 1000)

        collection = league + '-ladder'
        # writer.overwrite_data(collection, data)

    elapsed = time.time() - start
    print("Runtime: {.3f}".format(elapsed))


main()
