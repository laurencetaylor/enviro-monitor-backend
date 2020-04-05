import time
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280
from pms5003 import PMS5003
import db

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)
pms5003 = PMS5003()


def take_readings():
    readings = pms5003.read()
    return {"temperature": bme280.get_temperature(), "pressure": bme280.get_pressure(), "humidity": bme280.get_humidity(), "pm25": readings.pm_ug_per_m3(2.5)}


def run(interval):
    db.create_table()

    while True:
        data = take_readings()
        db.insert_readings(data["temperature"], data["pressure"],
                           data["humidity"], data["pm25"])
        time.sleep(interval)


run(300)
