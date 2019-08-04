"""Parse the response object, split the array into separate values/variables, create btcTickerDataset() object with the
 data, send btcTickerDataset() object to regex to be processed, pass btcTickerDataset() object to SQL database object
 to be inserted into the Azure database holding our table.
"""
from btcTickerDataset import btcTickerDataset
from sqlDatabase import sqlDatabase
from Regex import Regex
import constants


class Parser:
    def __init__(self, response_object):
        self.response_object = response_object
        self.mid = ''
        self.bid = ''
        self.ask = ''
        self.last_price = ''
        self.low = ''
        self.high = ''
        self.volume = ''
        self.timestamp = ''
        self.parsed = ''

    def parse_response(self):
        self.parsed = self.response_object.decode(constants.UNICODE).split(',')
        (self.mid, self.bid, self.ask, self.last_price, self.low, self.high, self.volume, self.timestamp) = self.parsed
        btc_dataset = btcTickerDataset(self.mid,
                                       self.bid,
                                       self.ask,
                                       self.last_price,
                                       self.low,
                                       self.high,
                                       self.volume,
                                       self.timestamp)
        Regex(btc_dataset)
        sqlDatabase().insert_data(btc_dataset)
        return self.parsed
