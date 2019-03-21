from requests import get
from time import sleep
import logging

LEAGUE_API_URL = 'http://api.pathofexile.com/leagues'


class RequestSender:
    @staticmethod
    def get_leagues():
        try:
            r = get(url=LEAGUE_API_URL)
            data = r.json()
            return list(i['id'] for i in data if 'Synthesis' in i['id'])
        except Exception as e:
            logging.exception(e)

    @staticmethod
    def __send_request(league, offset=0, limit=1):
        """
        :param league:
        :param offset:
        :param limit:
        :return: return entries parsed from a single ladder API response
        """
        try:
            ladderURL = 'http://api.pathofexile.com/ladders/{}?offset={}&limit={}'.format(league, offset, limit)
            print('Sending API request:', ladderURL)

            r = get(url=ladderURL)
            data = r.json()
            entries = data['entries']
            return entries
        except Exception as e:
            logging.exception("Error in send_request: " + e)

    @staticmethod
    def get_entries(league, number):
        """
        :param league:
        :param number:  number of entries returned
        :return: entries from multiple ladder API responses to "bypass" the API entry limit
        """
        entries = []
        offset = 0
        while offset < number:
            limit = min(200, number)
            entries += RequestSender.__send_request(league, offset, limit)
            offset += limit

        return entries
