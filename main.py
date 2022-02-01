# $ esptool.py --chip esp32c3 --port /dev/tty.usbmodem523201 erase_flash
# esptool.py v3.2
# Serial port /dev/tty.usbmodem523201
# Connecting...
# Chip is ESP32-C3 (revision 3)
# Features: Wi-Fi
# Crystal is 40MHz
# MAC: 84:f7:03:a0:f3:80
# Uploading stub...
# Running stub...
# Stub running...
# Erasing flash (this may take a while)...
# Chip erase completed successfully in 18.7s
# Hard resetting via RTS pin...
#
# $ esptool.py --chip esp32c3 --port /dev/tty.usbmodem523201 --baud 460800 write_flash -z 0x0 esp32c3-usb-20220117-v1.18.bin
# esptool.py v3.2
# Serial port /dev/tty.usbmodem523201
# Connecting...
# Chip is ESP32-C3 (revision 3)
# Features: Wi-Fi
# Crystal is 40MHz
# MAC: 84:f7:03:a0:f3:80
# Uploading stub...
# Running stub...
# Stub running...
# Changing baud rate to 460800
# Changed.
# Configuring flash size...
# Flash will be erased from 0x00000000 to 0x00161fff...
# Compressed 1446992 bytes to 863628...
# Wrote 1446992 bytes (863628 compressed) at 0x00000000 in 20.1 seconds (effective 575.3 kbit/s)...
# Hash of data verified.
# 
# Leaving...
# Hard resetting via RTS pin...

# https://twitter.com/GeekMomProjects/status/1483695065629224960

import esp32
esp32.RMT.bitstream_channel(None) # does not work without this

from machine import Pin
from neopixel import NeoPixel

pin = Pin(8, Pin.OUT) # NP control on Pin 8

np = NeoPixel(pin,25) # we have 25 pixels!

# np[0] = (0,255,0) # top left green
# np.write()
# np[2] = (0,255,0) # top middle green
# np.write()
# np[4] = (255,0,0) # top right red
# np.write()
# np[24] = (255,0,255) # bottom right magenta
# np.write()

# lights = [1,3,10,14,16,18,22]
# for x in lights:
# np[x] = (255,255,0)

# print(machine.unique_id()) # output board ID


def clear():
    np.fill((0,0,0))
    np.write()
    
def smile():
    lights = [1,3,10,14,16,18,22]
    for x in lights:
        np[x] = (15,15,0) # pale yellow smiley
    np.write()
    
smile()

