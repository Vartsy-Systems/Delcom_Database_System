import sqlite3

def connect():
    con = sqlite3.connect("fees_data.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS fees(
        id INTEGER PRIMARY KEY,
        std_id TEXT,
        name TEXT,
        basic TEXT,
        tot_fees TEXT,
        paid_fees TEXT,
        arrears TEXT,
        date_paid TEXT
        
    )""")
    con.commit()
    con.close()

def insert(std_id, name, basic, tot_fees, paid_fees, arrears, date_paid):
    con = sqlite3.connect("fees_data.db")
    cur = con.cursor()
    cur.execute("INSERT INTO fees VALUES(NULL,?,?,?,?,?,?,?)",
                (std_id, name, basic, tot_fees, paid_fees, arrears, date_paid))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("fees_data.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM fees")
    rows = cur.fetchall()
    con.close()
    return rows

def delete(id):
    con = sqlite3.connect("fees_data.db")
    cur = con.cursor()
    cur.execute("DELETE FROM fees WHERE id=?", (id,))
    con.commit()
    con.close()

def search(std_id="", name="", basic="", tot_fees="", paid_fees="", arrears="", date_paid=""):
    con = sqlite3.connect('fees_data.db')
    cur = con.cursor()
    cur.execute(
        'SELECT * FROM fees WHERE std_id LIKE ? OR name LIKE ? OR basic LIKE ? OR tot_fees LIKE ? OR paid_fees LIKE ? OR arrears LIKE ? OR date_paid LIKE ?',
        ('%' + std_id + '%', '%' + name + '%', '%' + basic + '%', '%' + tot_fees + '%', '%' + paid_fees + '%', '%' + arrears + '%', '%' + date_paid + '%'))
    rows = cur.fetchall()
    con.close()
    return rows

connect()
