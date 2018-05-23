import sqlite3

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
        self.cur.execute("SELECT Symbol, Date, Close FROM stock WHERE Symbol=? ORDER BY Date",(ticker, ))
        rows=self.cur.fetchall()
        return rows

    def delete(self, id):
        self.cur.execute("DELETE FROM stock WHERE id=?",(id,))
        self.conn.commit()

    def update_ticker(self):
        self.cur.execute("SELECT max(Close) FROM stock WHERE Symbol='PIT'")
        rows=self.cur.fetchone()[0]
        print(rows)

    def update(self, id, Symbol, Date, Close , High , Low , Open , Volume):
        self.cur.execute("UPDATE stock SET Symbol=?, Date=?, Close=?, High=?,  \
        Low =?, Open=?, Volume=? WHERE id=?",(Symbol, Date, Close , High , Low \
        , Open , Volume, id ))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
