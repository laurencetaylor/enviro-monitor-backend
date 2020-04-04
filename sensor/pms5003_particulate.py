import time
from pms5003 import PMS5003

pms5003 = PMS5003()

# readings = pms5003.read()
# print(readings)

# PM1.0
while True:
    readings = pms5003.read()
    print(readings.pm_ug_per_m3(1.0))
    time.sleep(1)

# PM2.5
# while True:
#     readings = pms5003.read()
#     print(readings.pm_ug_per_m3(2.5))
#     time.sleep(1)

# PM10
# while True:
#     readings = pms5003.read()
#     print(readings.pm_ug_per_m3(10))
#     time.sleep(1)
