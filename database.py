import os
import sqlite3

dir = os.path.dirname(__file__)
print(dir)

def save_to_db(string):
    conn = sqlite3.connect("data.db")

    cur = conn.cursor()

    #Create the table
    cur.execute(''' CREATE TABLE IF NOT EXISTS produkte
                    (id INTEGER, name TEXT)''')
    conn.commit()

    # closing
    cur.close()
    conn.close()