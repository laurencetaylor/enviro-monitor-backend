import time
from ltr559 import LTR559

ltr559 = LTR559()

while True:
    print(ltr559.get_lux(), ltr559.get_proximity())
    time.sleep(1)
