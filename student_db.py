import sqlite3


def connect():
    con = sqlite3.connect("student_info.db")
    cur = con.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS student(
    id INTEGER PRIMARY KEY,
    name text,
    gender text,
    dob text,
    gender text,
    guardian text,
    telephone text,
    level text,
    sickness text,
    student_id text
    
    )""")

    con.commit()
    con.close()

def Insert(name = "",gender = "",dob = "",pob = "",guardian = "",telephone = "",level = "",sickness = "",student_id = ""):
    con = sqlite3.connect("student_info.db")
    cur = con.cursor()
    cur.execute("INSERT INTO student VALUES(NULL,?,?,?,?,?,?,?,?,?)",(name,gender,dob,pob,guardian,telephone,level,sickness,student_id))
    con.commit()
    con.close()

def view():
    con = sqlite3.connect("student_info.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM student")
    row = cur.fetchall()
    return row

def delete(id):
    con = sqlite3.connect("student_info.db")
    cur = con.cursor()
    cur.execute("DELETE FROM student WHERE id=?", (id,))
    con.commit()
    con.close()


def search(name = "",gender = "",dob = "",pob = "",guardian = "",telephone = "",level = "",sickness = "",student_id = ""):
    con = sqlite3.connect('student_info.db')
    cur = con.cursor()

    cur.execute(
        'SELECT * FROM students WHERE name = ? OR gender = ? OR dob = ? OR pob = ? OR guardian = ? OR telephone = ? OR level = ? OR sickness = ? OR student_id = ?',
        (name,gender, dob, pob, guardian,telephone,level,sickness,student_id))
    row = cur.fetchall()
    return row

    con.commit()
connect()