"""Query the database"""

import sqlite3


def query(query):
    """Query the database for the top 5 rows of the DiabetesDB table"""
    conn = sqlite3.connect("DiabetesDB.db")
    cursor = conn.cursor()
    cursor.execute(query)
    q_result = cursor.fetchall()
    print(q_result)
    conn.close()
    return q_result
    
    # cursor.execute("SELECT * FROM DiabetesDB LIMIT 5")
    # print("Top 5 rows of the DiabetesDB table:")
    # print(cursor.fetchall())
    # conn.close()
    # return "Success"
