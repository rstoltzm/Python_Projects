
import pandas_datareader as pdr
import pandas
import datetime as dt
from database import Database
import pprint
import random

database=Database("stock.db")

class StockLoader():

    def __init__(self, ticker):
        print("Parametrics")
        self.ticker = ticker
        print("Stocks: ")
        print(self.ticker)
        self.start = dt.date.today() - dt.timedelta(days=20)
        self.end = dt.date.today()
        print("\nStart Time: " + str(self.start))
        print("End Time: " + str(self.end))

    def WriteToSql(self, data):
        print(data)

    def loader(self):
        for name in self.ticker:
            data_access='morningstar'
            data = pdr.DataReader(name,data_access,self.start,self.end).reset_index()
            self.WriteToSql(data)
            print(data)

    def AddRandomData(self, ticker, Start):
        Close = Start
        for x in range(30):
            date = dt.date(2018, 4, 10) + dt.timedelta(days=x)
            r = random.randint(-4,1)
            Volume = random.randint(Close * 50, Close * 120)
            Close = Close + r
            High = Start + 10
            Low = Start - 10
            Open = Close
            Open = Open + r
            database.insert(ticker, date, Close , High , Low , Open , Volume)

    def Pandas_Loader(self):
        df = database.sql_to_dataframe()
        pprint.pprint(df)

#print('\nPre-Change')
#print(database.update_ticker())
#pprint.pprint(database.view_ticker('PIT'))

#Useful Commands
#pprint.pprint(database.view())
#database.update(5, 'CC', '2018-05-22', 35 , 40 , 25 , 32 , 30000)
#database.insert('BBB', '2018-04-22', 65 , 70 , 55 , 62 , 8000)
#stockloader.AddRandomData('BIO', 79)
#ticker=['QQQ','SPY','AAPL','AMZN','MSFT','FB','GOOGL','GOOG','INTC','CSCO']
ticker=['QQQ','SPY']

stockloader = StockLoader(ticker)
#stockloader.loader()
stockloader.Pandas_Loader()
