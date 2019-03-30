from modules.dbwriter import DBWriter
from modules.requestsender import RequestSender as rq
import time

MONGO_DB_CONNECT_STRING = 'mongodb+srv://exdunn:exdunn@exaltcluster-e03v8.mongodb.net/test?retryWrites=true'
DB_NAME = 'exaltDB'


def main():
    start = time.time()
    writer = DBWriter(MONGO_DB_CONNECT_STRING, DB_NAME)
    leagues = rq.get_leagues()

    writer.update_data('Synthesis')

    # for league in leagues:
    #     # data = rq.get_entries(league, 10)
    #
    #     collection = league
    #     # writer.overwrite_data(collection, data)
    #
    #     writer.update_data(league)

    elapsed = time.time() - start
    print("Runtime: {}".format(elapsed))


main()
