import ST7735
from PIL import Image, ImageDraw, ImageFont
from fonts.ttf import RobotoMedium as UserFont
try:
    from smbus2 import SMBus
except ImportError:
    from smbus import SMBus
from bme280 import BME280

bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)

disp = ST7735.ST7735(
    port=0,
    cs=1,
    dc=9,
    backlight=12,
    rotation=270,
    spi_speed_hz=10000000
)

disp.begin()

WIDTH = disp.width
HEIGHT = disp.height

img = Image.new('RGB', (WIDTH, HEIGHT), color=(0, 0, 0))
draw = ImageDraw.Draw(img)

rect_colour = (0, 180, 180)
draw.rectangle((0, 0, 160, 80), rect_colour)

font_size = 18
font = ImageFont.truetype(UserFont, font_size)

colour = (255, 255, 255)
temperature = "Temperature: {:.2f} *C".format(bme280.get_temperature())

x = 0
y = 0
draw.text((x, y), temperature, font=font, fill=colour)

disp.display(img)
