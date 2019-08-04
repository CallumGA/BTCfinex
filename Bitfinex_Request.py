"""API request sent from this object"""

import urllib.request
import constants


class bitfinexRequest:
    def send_request(self):
        try:
            self.request = urllib.request.urlopen(constants.API_URL).read()
        except:
            print("Cannot reach web service. Check internet connection or API availability.")

    def get_response(self):
        return self.request
