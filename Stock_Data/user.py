from database import CursorFromConnectionPool

class User:
    def __init__(self, etf, date, open, high, low, close, volume, openint, id=None):
        self.etf = etf
        self.date = date
        self.open = open
        self.high = high
        self.low = low
        self.close = close
        self.volume = volume
        self.openint = openint

    def __repr__(self):
        return "<User {}>".format(self.email)

    def save_to_db(self):
        # This is creating a new connection pool every time! Very expensive...
        with CursorFromConnectionPool() as cursor:
            cursor.execute('INSERT INTO stock_data (etf,Date,Open,High,Low,Close,Volume,OpenInt) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)',
                            (self.etf, self.date, self.open, self.high, self.low, self.close, self.volume, self.openint))
