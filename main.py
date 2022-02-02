# inspired from https://twitter.com/GeekMomProjects/status/1483695065629224960

import esp32
from machine import Pin
from neopixel import NeoPixel
import random
import time

# esp32.RMT.bitstream_channel(None) # does not work without this
esp32.RMT.bitstream_channel(0)  # 01Space board needs this

pin = Pin(8, Pin.OUT)  # NP control on Pin 8
pixels = 25  # we have 25 pixels, set here to use for loops

np = NeoPixel(pin, pixels)

# scratchpad code testing

# np[0] = (0,255,0) # top left green
# np.write()
# np[2] = (0,255,0) # top middle green
# np.write()
# np[4] = (255,0,0) # top right red
# np.write()
# np[24] = (255,0,255) # bottom right magenta
# np.write()

# print(machine.unique_id()) # output board ID

def rand_rgb():
    """Return a randomised RGB tuple with max values of 50 to limit brightness"""
    r = random.randint(0,50)
    g = random.randint(0,50)
    b = random.randint(0,50)
    return r, g, b


def test_all():
    """Iterate through all Neopixels and switch them on and off in sequence"""
    for x in range(pixels):
        np[x] = (rand_rgb())
        np.write()
        print("Test pixel: " + str(x))
        time.sleep(0.3)
        np[x] = (0, 0, 0)
        np.write()
        time.sleep(0.3)
    print("Test completed.")


def clear():
    """Reset all Neopixels to black / off"""
    np.fill((0, 0, 0))
    np.write()


def smile():
    """Light the pixels into a smiley face"""
    lights = [1, 3, 10, 14, 16, 18, 22]
    for x in lights:
        np[x] = (15, 15, 0)  # pale yellow smiley
    np.write()
    print(":-)")


test_all()
smile()
