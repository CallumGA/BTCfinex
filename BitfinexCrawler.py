"""Run the application from here..."""

import time
from Bitfinex_Request import bitfinexRequest
from Parser import Parser

while True:
    try:
        API = bitfinexRequest()
        request = API.send_request()
        response = API.get_response()
        parser = Parser(response)
        parser.parse_response()
        time.sleep(5)
    finally:
        print("BTC data captured and stored!")
