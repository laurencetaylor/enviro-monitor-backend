import sqlite3
from datetime import datetime


def create_table():
    conn = sqlite3.connect('enviro_data.db')
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enviro_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime TEXT,
        temperature INTEGER,
        pressure INTEGER,
        humidity INTEGER,
        pm25 INTEGER
    )
    """)


def insert_readings(temperature, pressure, humidity, pm25):
    conn = sqlite3.connect('enviro_data.db')
    cursor = conn.cursor()
    with conn:
        datetime_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(f"""
        INSERT INTO enviro_data(datetime, temperature, pressure, humidity, pm25) VALUES (
            '{datetime_string}', {temperature}, {pressure}, {humidity}, {pm25}
        )
        """)


def get_readings(limit=100):
    conn = sqlite3.connect('enviro_data.db')
    cursor = conn.cursor()
    with conn:
        cursor.execute(f"""
        SELECT * FROM enviro_data LIMIT {limit}
        """)
        return cursor.fetchall()
