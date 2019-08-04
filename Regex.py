"""Regex class strips the data of characters we dont want in our data like commas, brackets, colons etc. then sets
the btcTickerDataset() object data members to the new stripped down version
"""
class Regex:
    def __init__(self, btc_dataset):
        self.mid = btc_dataset.mid.split(':', 1)[-1].replace('"', '')
        self.bid = btc_dataset.bid.split(':', 1)[-1].replace('"', '')
        self.ask = btc_dataset.ask.split(':', 1)[-1].replace('"', '')
        self.last_price = btc_dataset.last_price.split(':', 1)[-1].replace('"', '')
        self.low = btc_dataset.low.split(':', 1)[-1].replace('"', '')
        self.high = btc_dataset.high.split(':', 1)[-1].replace('"', '')
        self.volume = btc_dataset.volume.split(':', 1)[-1].replace('"', '')
        self.timestamp = btc_dataset.timestamp.split(':', 1)[-1].replace('"', '')

        btc_dataset.set_mid(self.mid)
        btc_dataset.set_bid(self.bid)
        btc_dataset.set_ask(self.ask)
        btc_dataset.set_last_price(self.last_price)
        btc_dataset.set_low(self.low)
        btc_dataset.set_high(self.high)
        btc_dataset.set_volume(self.volume)
        btc_dataset.set_timestamp(self.timestamp)
