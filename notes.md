# Notes

## Hardware

### Board on macOS

- location varies -> `/dev/tty.usbmodem21301` on my M1 Pro

```text
USB JTAG/serial debug unit:

  Product ID: 0x1001
  Vendor ID: 0x303a
  Version: 1.01
  Serial Number: 84:F7:03:A0:F3:80
  Speed: Up to 12 Mb/s
  Manufacturer: Espressif
  Location ID: 0x01130000 / 4
  Current Available (mA): 500
  Current Required (mA): 500
  Extra Operating Current (mA): 0
```

### USB info

**USB ID** - 1001:303a
**VID** - 303a - Espressif
**PID** - 1001 - USB JTAG/serial debug / ESP32-C3

Noting that this is not in the [Espressif allocated list of PIDs](https://github.com/espressif/usb-pids/blob/main/allocated-pids.txt)

### Pins

- 0/1 I2C SDA/SCL
- 8 NeoPixels
- 9 Button
- 10 Status LED, GPIO
- 11 Reset (?) tbc
- 2/3/4/5/6/7/18/19/20/21 GPIO

### I2C

```python
>>> from machine import I2C
>>> i2c = I2C(0,sda=Pin(0),scl=Pin(1))
>>> i2c.scan()
[63] # <-- this is a SparkFun Qwiic Twist
>>> i2c.scan()
[56] # <- this is Adafruit AHT20
>>> i2c = I2C(0,sda=Pin(0),scl=Pin(1), freq=100000)
>>> i2c.readfrom(0x38, 4)
b'\x18\x00\x00\x00'
```

These are the Qwiic/Stemma QT boards I have on hand / identified with the code.

- [35] Adafruit BH1750
- [56] Adafruit AHT20
- [57] Adafruit APDS-9960
- [63] SparkFun Qwiic Twist

(appears to work fine with BCRobotics expander)

### Reference card

![Annotated board](/reference/ESP32-C3FH4-RGB-reference.jpeg)

## Other materials

### Espressif chip reference docs

- [ESP32-C3 Datasheet](https://www.espressif.com/sites/default/files/documentation/esp32-c3_datasheet_en.pdf)
- [ESP32-C3 Technical Reference Manual](https://www.espressif.com/sites/default/files/documentation/esp32-c3_technical_reference_manual_en.pdf)

### Manufacturer info

- [Arduino sketch](https://github.com/01Space/ESP32-C3FH4-RGB)
  - works fine using the ESP32 Arduino core v2.0.2 / ESP32C3 Dev Module board in Arduino IDE 2.0
  - code has NeoPixel on pin 8, 800 KHz with GRBW

- [Video](https://www.youtube.com/watch?v=m-cgaS6eHv4)

From the notes with the YouTube video:

```text
ESP32-C3FH4, 2.4GHz Wi-Fi and supporting long-distance Bluetooth 5
built-in 400 KB SRAM and 4 MB Flash
USB Type-C,USB OnThe-Go
Including 2 channels of 5V -3.3V DC / DC
Integrated 5X5 ws2812b-1515 and 2 buttons
3V power LED and status LED
Ceramic Antenna
Size: 21 x 18 mm
Weight: 2.3g
```

- [CNX News item](https://www.cnx-software.com/2022/01/07/board-with-25-rgb-leds-is-offered-with-esp32-c3-or-esp32-pico-d4/)

### MicroPython

Flash to board:

```shell
esptool.py --chip esp32c3 --port /dev/tty.usbmodem523201 erase_flash
esptool.py --chip esp32c3 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x0 esp32c3-20220117-v1.18.bin
```

- [NeoPixel RMT issue](https://github.com/micropython/micropython/issues/8109)

Now works fully (from the `v1.18-68-g1f04a9a1f` nightly).

Yet to test the GPIO pins, or the mysterious (Qwiic/JST-SH) 4-pin connector on the board.

### CircuitPython

Look into this - [potentialy similar board](https://circuitpython.org/board/ai_thinker_esp32-c3s/)

NB the CP docs list a C3 DevKit for module compat, but no download - ask on Discord

## Ideas / TODO

- build out more tests and effects for the basic code
  - Bluetooth, Wifi, button
  - more patterns
  - replicate the Arduino samples
- learn about the power draw
  - [from @matt_trentini](https://twitter.com/matt_trentini/status/1490475943059542019): "Take care about how many and how brightly you drive those Neopixels. Last I checked they can consume up to 60mA *each* and 20mA is common. Given the micro can consume a couple of hundred mA you can easily exceed your power limit (presumably max 500mA)."
  - try out various brightness options, per pixel analysis, etc.
- tooling
  - played with [rshell](https://core-electronics.com.au/tutorials/getting-started-with-raspberry-pi-pico.html)
    - issues holding a stable REPL connection. Power? USB reliability?
  - ampy (maintained?)
  - PlatformIO
- ~~CheerPixel! (CheerDot? CheerSpot?)~~
  - initial implementation in `cheerlights-demo.py` ([blog post](https://dev.to/andypiper/making-a-cheerdot-with-micropython-3ocf))
  - CheerPixel(s) with history etc still todo
  - brightness adjustment (divide by 10)
  - patterns
- test out the [Wordle thing](https://twitter.com/ciro/status/1488259161066459142)
- GitHub contributions graph?
- try out Qwiic I2C connections (identify pins)
  - e.g. Qwiic twist to drive pixel intensity
- on-board web server for drawing / updating designs, setting and configuring pattern display and online source; also config wifi
- ...

### errors

```text
network config: ('172.16.0.50', '255.255.255.0', '172.16.0.1', '172.16.0.1')
message received
(0, 0, 255)
message received
(0, 128, 0)
message received
(253, 245, 230)
message received
(255, 0, 255)
Build:Feb  7 2021
rst:0x7 (TG0WDT_SYS_RST),boot:0xc (SPI_FAST_FLASH_BOOT)
Saved PC:0x4038f9c6
SPIWP:0xee
mode:DIO, clock div:1
load:0x3fcd6100,len:0xe3c
load:0x403ce000,len:0x6dc
load:0x403d0000,len:0x28c4
entry 0x403ce000
W (24) boot.esp32c3: PRO CPU has been reset by WDT.
MicroPython v1.18 on 2022-02-01; ESP32C3 module with ESP32C3
Type "help()" for more information.
>>>
```

WDT = Watchdog Timer
Maybe a sleep / wol thing? looks like ESP core crash. Only happened once, but after receiving several MQTT messages.

### code scratchpad

```python
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
```
