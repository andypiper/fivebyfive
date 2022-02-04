# inspired from https://twitter.com/GeekMomProjects/status/1483695065629224960
# see https://dev.to/andypiper/bringing-the-bling-with-micropython-hn1

# this is a deliberately simple script to test the various board functions

import esp32
from machine import Pin
from neopixel import NeoPixel
import random
import time


# setup the NeoPixels

# esp32.RMT.bitstream_channel(None)  # does *not* work with this board
esp32.RMT.bitstream_channel(0)  # board needs this for NeoPixels to work

neopin = Pin(8, Pin.OUT)  # NeoPixel control on Pin 8
pixels = 25  # we have 25 pixels, set as a constant here for loops

np = NeoPixel(neopin, pixels)

# setup the button and the status LED
button = Pin(9, Pin.IN)
status_led = Pin(10, Pin.OUT)


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
    # Return a randomised RGB tuple, max values of 50 to limit brightness
    r = random.randint(0, 50)
    g = random.randint(0, 50)
    b = random.randint(0, 50)
    return r, g, b


def clear_all():
    # Reset all Neopixels to black / off
    # TODO: could have this use a custom colour
    np.fill((0, 0, 0))
    np.write()


def clear_wipe():
    # Reset all Neopixels to off with a wipe effect
    lights = [0, 1, 2, 3, 4]
    for x in lights:
        np[x] = (0, 0, 0)
        np.write()
    time.sleep(0.2)
    lights = [5, 6, 7, 8, 9]
    for x in lights:
        np[x] = (0, 0, 0)
        np.write()
    time.sleep(0.2)
    lights = [10, 11, 12, 13, 14]
    for x in lights:
        np[x] = (0, 0, 0)
        np.write()
    time.sleep(0.2)
    lights = [15, 16, 17, 18, 19]
    for x in lights:
        np[x] = (0, 0, 0)
        np.write()
    time.sleep(0.2)
    lights = [20, 21, 22, 23, 24]
    for x in lights:
        np[x] = (0, 0, 0)
        np.write()
    time.sleep(0.2)


def test_all_np():
    # Iterate through all Neopixels and blink
    # with random colours in sequence
    clear_all()
    for x in range(pixels):
        np[x] = rand_rgb()
        np.write()
        print("Pixel: " + str(x))
        time.sleep(0.4)
        np[x] = (0, 0, 0)
        np.write()
        time.sleep(0.2)
    print("NeoPixels Test completed.")


def test_led():
    # Blink the status LED five times
    for i in range(5):
        status_led.on()
        time.sleep(0.4)
        status_led.off()
        time.sleep(0.2)


def smile():
    clear_wipe()
    # Light the pixels into a smiley face
    lights = [1, 3, 10, 14, 16, 18, 22]
    for x in lights:
        np[x] = (15, 15, 0)  # pale yellow smiley
    np.write()
    print(":-)")


def heart():
    clear_wipe()
    # Light the pixels into a heart shape
    lights = [1, 3, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 17, 18, 22]
    for x in lights:
        np[x] = (50, 0, 0)  # red heart (TODO: customisable colour)
    np.write()
    print("<3")


# run the functions

test_all_np()
time.sleep(0.5)
test_led()
time.sleep(0.5)
smile()
time.sleep(1.0)
heart()
