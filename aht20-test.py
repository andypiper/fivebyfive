# uses https://github.com/targetblank/micropython_ahtx0
# ampy -p /dev/cu.usbmodem11301 mkdir lib
# ampy -p /dev/cu.usbmodem11301 put ahtx0.py lib/ahtx0.py

# NB I2C is deprecated, use SoftI2C
from machine import Pin, SoftI2C
import utime
import ahtx0

i2c = SoftI2C(scl=Pin(1), sda=Pin(0))

sensor = ahtx0.AHT10(i2c)

while True:
    print("\nTemperature: %0.2f C" % sensor.temperature)
    print("Humidity: %0.2f %%" % sensor.relative_humidity)
    utime.sleep(5)
