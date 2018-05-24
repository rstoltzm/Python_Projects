import datetime as dt
import random

Close = 65
print(Close)


for x in range(10):
    date = dt.date(2007, 12, 5) + dt.timedelta(days=x)
    r = random.randint(-2,2)
    Volume = random.randint(5000,10000)
    Close = Close + r
    High = 75
    Low = 55
    Open = Close
    Open = Open + r
    print('BBB', date, Close , High , Low , Open , Volume)

#(Symbol, Date, Close , High , Low , Open , Volume ))

# Testing branch update in atom using git
