try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

print(bme280.get_temperature())
print(bme280.get_pressure(), bme280.get_humidity())
