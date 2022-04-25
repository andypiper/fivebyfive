# 01Space C3-RGB MicroPython Helper Library

from micropython import const
from machine import Pin
from neopixel import NeoPixel

# Pin Assignments

# I2C
I2C_SDA = const(0)
I2C_SCL = const(1)

# Status LED and RGB array
LED_PIN = const(10)
WS2812B_PIN = const(8)
PIXELS = const(25)

# Button
BUTTON_PIN = const(9)

# Built-in peripherals
status_led = Pin(LED_PIN, Pin.OUT, value=0)
button = Pin(BUTTON_PIN, Pin.IN)
grid_pin = Pin(WS2812B_PIN, Pin.OUT, value=0)
grid = NeoPixel(grid_pin, PIXELS)
