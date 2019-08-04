"""SQL database object. Insert the data from the btcTickerDataset() in AZURE database stored in the cloud"""

import pyodbc
import constants


class sqlDatabase:

    def __init__(self):
        server = constants.HOST
        database = constants.DB_NAME
        username = constants.DB_USERNAME
        password = constants.DB_PASSWORD
        self.cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username
            + ';PWD=' + password)
        self.cursor = self.cnxn.cursor()

    def insert_data(self, btc_dataset):
        self.cursor.execute("INSERT INTO BTC_DATA "
                            "(MID, BID, ASK, LAST_PRICE, LOW, HIGH, VOLUME, TIMESTAMP) "
                            "VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (btc_dataset.mid, btc_dataset.bid, btc_dataset.ask,
                                                                btc_dataset.last_price, btc_dataset.low,
                                                                btc_dataset.high,
                                                                btc_dataset.volume, btc_dataset.timestamp))
        self.cnxn.commit()