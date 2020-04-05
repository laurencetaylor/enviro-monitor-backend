import time
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280
from pms5003 import PMS5003

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)
pms5003 = PMS5003()


def get_readings():
    readings = pms5003.read()
    return {"temperature": bme280.get_temperature(), "pressure": bme280.get_pressure(), "humidity": bme280.get_humidity(), "pm25": readings.pm_ug_per_m3(2.5)}
