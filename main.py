# inspired from https://twitter.com/GeekMomProjects/status/1483695065629224960

import esp32
from machine import Pin
from neopixel import NeoPixel
import random
import time


# setup the NeoPixels
# esp32.RMT.bitstream_channel(None) # does not work with this
esp32.RMT.bitstream_channel(0)  # 01Space board needs this

neopin = Pin(8, Pin.OUT)  # NeoPixel control on Pin 8
pixels = 25  # we have 25 pixels, set as a constant here to use for loops

np = NeoPixel(neopin, pixels)

# setup the button and the status LED
button = Pin(9, machine.Pin.IN)
status_led = Pin(10, machine.Pin.OUT)

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
    # Return a randomised RGB tuple with max values of 50 to limit brightness
    r = random.randint(0,50)
    g = random.randint(0,50)
    b = random.randint(0,50)
    return r, g, b


def test_all():
    # Iterate through all Neopixels and switch them on and off
    # with random colours in sequence
    # Also output the chip internal temperature in centigrade
    for x in range(pixels):
        np[x] = (rand_rgb())
        np.write()
        print("Test pixel: " + str(x))
        time.sleep(0.3)
        np[x] = (0, 0, 0)
        np.write()
        time.sleep(0.3)
    print("NeoPixels Test completed.")
    # print("ESP32 temp measures: " + str((esp32.raw_temperature()-32)/1.8) + " degrees C")


def clear():
    # Reset all Neopixels to black / off
    np.fill((0, 0, 0))
    np.write()


def smile():
    # Light the pixels into a smiley face
    lights = [1, 3, 10, 14, 16, 18, 22]
    for x in lights:
        np[x] = (15, 15, 0)  # pale yellow smiley
    np.write()
    print(":-)")


def heart():
    # Light the pixels into a heart shape
    lights = [1, 3, 5, 6, 8, 9, 11, 12, 13, 17, 22]
    for x in lights:
        np[x] = (50, 0, 0)  # red heart (TODO: customisable colour)
    np.write()
    print("<3")


# run the functions
test_all()
smile()
