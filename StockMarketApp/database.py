import sqlite3
import pprint
import pandas

class Database:

    def __init__(self, db):
        self.conn=sqlite3.connect(db)
        self.cur=self.conn.cursor()
        self.cur.execute("CREATE TABLE IF NOT EXISTS stock (id INTEGER PRIMARY \
        KEY, Symbol text, Date date, Close integer, High integer, Low integer, \
        Open integer, Volume integer)")
        self.conn.commit()

    def insert(self, Symbol, Date, Close , High , Low , Open , Volume):
        self.cur.execute("INSERT INTO stock VALUES (NULL,?,?,?,?,?,?,?)",      \
        (Symbol, Date, Close , High , Low , Open , Volume ))
        self.conn.commit()

    def view(self):
        self.cur.execute("SELECT * from stock")
        rows=self.cur.fetchall()
        return rows

    def view_ticker(self, ticker):
        self.cur.execute("SELECT Symbol, Date, Close, High, Low FROM stock WHERE Symbol=? ORDER BY Date",(ticker, ))
        rows=self.cur.fetchall()
        return rows

    def sql_to_dataframe(self,):
        df = pandas.read_sql_query("\
        SELECT * \
        FROM stock \
        WHERE Date BETWEEN '2018-03-11' AND '2018-08-11' \
        ",self.conn)
        #pprint.pprint(df)
        return df

    def delete(self, id):
        self.cur.execute("DELETE FROM stock WHERE id=?",(id,))
        self.conn.commit()

    def update_ticker(self):
        # Updates the High and Low Column for all symbols.
        # Select all the potential symbols and feed into for loop
        self.cur.execute("SELECT DISTINCT Symbol FROM stock")
        Symbol_List=self.cur.fetchall()
        print(Symbol_List)

        for name in Symbol_List:
            name = name[0]
            # Select Max
            self.cur.execute("SELECT max(Close) FROM stock WHERE Symbol=?",(name,))
            max=self.cur.fetchone()[0]
            # Select Min
            self.cur.execute("SELECT min(Close) FROM stock WHERE Symbol=?",(name,))
            min=self.cur.fetchone()[0]
            # Update each symbol 'name' with max, min
            self.cur.execute("UPDATE stock SET High=?, Low=? WHERE Symbol=?",(max,min,name))
            pprint.pprint(self.view_ticker(name))


    def update(self, id, Symbol, Date, Close , High , Low , Open , Volume):
        self.cur.execute("UPDATE stock SET Symbol=?, Date=?, Close=?, High=?,  \
        Low =?, Open=?, Volume=? WHERE id=?",(Symbol, Date, Close , High , Low \
        , Open , Volume, id ))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
