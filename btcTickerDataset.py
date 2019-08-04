"""Object class for a BTC ticker dataset"""
class btcTickerDataset:
    def __init__(self, mid, bid, ask, last_price, low, high, volume, timestamp):
        self.mid = mid
        self.bid = bid
        self.ask = ask
        self.last_price = last_price
        self.low = low
        self.high = high
        self.volume = volume
        self.timestamp = timestamp

    def set_mid(self, mid):
        self.mid = mid

    def set_bid(self, bid):
        self.bid = bid

    def set_ask(self, ask):
        self.ask = ask

    def set_last_price(self, last_price):
        self.last_price = last_price

    def set_low(self, low):
        self.low = low

    def set_high(self, high):
        self.high = high

    def set_volume(self, volume):
        self.volume = volume

    def set_timestamp(self, timestamp):
        self.timestamp = timestamp
