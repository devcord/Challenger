import sqlite3
from sqlite3 import Error

def create_connection(db_file):
    # Create a new connection to the sqlite database
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        print(sqlite3.version)
    except Error as e:
        print(e)

    return conn

def create_table(conn, create_table_sql):
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)

def create_user(conn, user):

    sql = ''' INSERT INTO users(user_id)
              VALUES(?) '''

    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()

def create_challenge(conn, user):

    sql = ''' INSERT INTO challenges(challenge_id, title, description, created)
              VALUES(?,?,?,?) '''

    cur = conn.cursor()
    cur.execute(sql, user)
    conn.commit()

db_conn = create_connection(r"./db/testdb.db")