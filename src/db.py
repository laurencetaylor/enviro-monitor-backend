import sqlite3
from datetime import datetime

conn = sqlite3.connect('air_quality.db')
cursor = conn.cursor()


def create_table():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS air_quality (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime TEXT,
        temperature INTEGER,
        pressure INTEGER,
        humidity INTEGER,
        pm25 INTEGER
    )
    """)


def insert_readings(temperature, pressure, humidity, pm25):
    with conn:
        datetime_string = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(f"""
        INSERT INTO air_quality(datetime, temperature, pressure, humidity, pm25) VALUES (
            '{datetime_string}', {temperature}, {pressure}, {humidity}, {pm25}
        )
        """)


def get_readings(limit=100):
    with conn:
        cursor.execute(f"""
        SELECT * FROM air_quality LIMIT {limit}
        """)
        return cursor.fetchall()
