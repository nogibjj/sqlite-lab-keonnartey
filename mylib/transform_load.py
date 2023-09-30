"""
Transforms and Loads data into the local SQLite3 database
Example:
 Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age,
            Outcome
"""
import sqlite3
import csv
import os

# load the csv file and insert into a new sqlite3 database
def load(dataset="/workspaces/sqlite-lab-keonnartey/data/Diabetes.csv"):
    """ "Transforms and Loads data into the local SQLite3 database"""

    # prints the full working directory and path
    print(os.getcwd())
    payload = csv.reader(open(dataset, newline=""), delimiter=",")
    next(payload)
    conn = sqlite3.connect("DiabetesDB.db")
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS DiabetesDB")
    c.execute(
        """
        CREATE TABLE DiabetesDB(
            Pregnancies,
            Glucose,
            BloodPressure,
            SkinThickness,
            Insulin,
            BMI,
            DiabetesPedigreeFunction,
            Age,
            Outcome
        )"""
    )
    # insert
    c.executemany(
        """
        INSERT INTO DiabetesDB VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""",
        payload,
    )
    conn.commit()
    conn.close()
    return "DiabetesDB.db"
