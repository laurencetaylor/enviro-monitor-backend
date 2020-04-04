import time
from enviroplus import gas

while True:
    readings = gas.read_all()
    print(readings)
    time.sleep(1.0)

# Get specific values with readings.reducing, readings.oxidising, readings.nh3
# while True:
#     readings = gas.read_all()
#     print(readings.reducing)
#     time.sleep(1.0)