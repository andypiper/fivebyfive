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

- from `ioreg -p IOUSB -l`

```text
    |   +-o USB JTAG/serial debug unit@01114000  <class IOUSBHostDevice, id 0x10001c6b3, registered, matched, active, busy 0 (234 ms), retain 46>
    |       {
    |         "sessionID" = 4586099087818
    |         "USBSpeed" = 1
    |         "idProduct" = 4097
    |         "iManufacturer" = 1
    |         "bDeviceClass" = 239
    |         "IOPowerManagement" = {"PowerOverrideOn"=Yes,"DevicePowerState"=2,"CurrentPowerState"=2,"CapabilityFlags"=32768,"MaxPowerState"=2,"DriverPowerState"=0}
    |         "bcdDevice" = 257
    |         "bMaxPacketSize0" = 64
    |         "iProduct" = 2
    |         "iSerialNumber" = 3
    |         "bNumConfigurations" = 1
    |         "USB Product Name" = "USB JTAG_serial debug unit"
    |         "USB Address" = 10
    |         "locationID" = 17907712
    |         "bDeviceSubClass" = 2
    |         "bcdUSB" = 512
    |         "kUSBSerialNumberString" = "84:F7:03:A0:EF:84"
    |         "kUSBCurrentConfiguration" = 1
    |         "IOCFPlugInTypes" = {"9dc7b780-9ec0-11d4-a54f-000a27052861"="IOUSBHostFamily.kext/Contents/PlugIns/IOUSBLib.bundle"}
    |         "bDeviceProtocol" = 1
    |         "USBPortType" = 0
    |         "IOServiceDEXTEntitlements" = (("com.apple.developer.driverkit.transport.usb"))
    |         "USB Vendor Name" = "Espressif"
    |         "Device Speed" = 1
    |         "idVendor" = 12346
    |         "kUSBProductString" = "USB JTAG/serial debug unit"
    |         "USB Serial Number" = "84:F7:03:A0:EF:84"
    |         "IOGeneralInterest" = "IOCommand is not serializable"
    |         "kUSBAddress" = 10
    |         "kUSBVendorString" = "Espressif"
    |       }
```

- from `ioreg -r -c IOUSBHostDevice -l | rg /dev`

```text
  | |   |     |         "IOCalloutDevice" = "/dev/cu.usbmodem111401"
  | |   |     |         "IODialinDevice" = "/dev/tty.usbmodem111401"
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

### Board manufacturer info

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
esptool.py --chip esp32c3 --port /dev/tty.usbmodem523201 --baud 460800 write_flash -z 0x0 esp32c3-usb-20220209-unstable-v1.18-121-gd8a7bf83c.bin
```

- [NeoPixel RMT issue](https://github.com/micropython/micropython/issues/8109)
  - Now works fully with bitstream channel manually set to 0 (as from the `v1.18-68-g1f04a9a1f` MicroPython nightly).

Yet to test the GPIO pins. I2C detects sensors, data in untested.

### CircuitPython

Look into this - [potentially similar board](https://circuitpython.org/board/ai_thinker_esp32-c3s/)

NB the CP docs list a C3 DevKit for module compat, but no download - ask on Adafruit Discord...

From Discord conversation:

```text
we are just getting started with the C3. Correct, it can't present CIRCUITPY. The RMT code in MicroPython may or may not be used in CircuitPython: we may have our own version anyway.

we are working on a BLE workflow for the C3. It's very early for C3 support now.
```

## Videos

### YouTube

- my [playlist](https://www.youtube.com/playlist?list=PLBlxSZoETPB-GN-FPKTdkK5IxIUz5LEIO)

- original [Video](https://www.youtube.com/watch?v=m-cgaS6eHv4)
  - [same thing, different channel](https://www.youtube.com/watch?v=9GeGNKnFHJw)
- [Windows driver installation (Chinese)](https://www.youtube.com/watch?v=QsQvsG6elDM)
- [ESP32 C3 RGB LED blinker](https://www.youtube.com/watch?v=6XdavE2z5hk)
- [ESP32 C3 RISC-V Wi-Fi Bluetooth](https://www.youtube.com/watch?v=WwOiEF_vm8g)

### Twitter

- [Tweet](https://twitter.com/yongxiangxu251/status/1455866140165509121)
- [Tweet](https://twitter.com/GeekMomProjects/status/1483695065629224960)
- [Tweet](https://twitter.com/GeekMomProjects/status/1489168933709967366)
- [Tweet](https://twitter.com/GeekMomProjects/status/1490163560688672768)
- [Tweet](https://twitter.com/ciro/status/1488259161066459142)
- [Tweet](https://twitter.com/tablatronix/status/1488629644823871495)
- [Tweet](https://twitter.com/andypiper/status/1493237488667795456)

## Ideas / TODO

- build out more tests and effects for the basic code
  - Bluetooth, Wifi, button
  - more patterns
  - replicate the [Arduino samples](https://github.com/01Space/ESP32-C3FH4-RGB) in Mpy
- learn about the power draw
  - [from @matt_trentini](https://twitter.com/matt_trentini/status/1490475943059542019): "Take care about how many and how brightly you drive those Neopixels. Last I checked they can consume up to 60mA *each* and 20mA is common. Given the micro can consume a couple of hundred mA you can easily exceed your power limit (presumably max 500mA)."
  - try out various brightness options, per pixel analysis, etc.
- tooling
  - played with [`rshell`](https://core-electronics.com.au/tutorials/getting-started-with-raspberry-pi-pico.html)
    - issues holding a stable REPL connection. Power? USB reliability?
  - `ampy` (maintained?)
    - works for copy to device / list contents
  - try a PlatformIO setup
  - learn about `mpremote`
- ~~CheerPixel! (CheerDot? CheerSpot?)~~
  - initial implementation in `cheerlights-demo.py` ([blog post](https://dev.to/andypiper/making-a-cheerdot-with-micropython-3ocf))
  - improve colour matching (pink etc - seems white)
  - CheerPixel(s) with history etc still todo
  - brightness adjustment (divide by 10)
  - pattern palette
- ~~test out the [Wordle thing](https://twitter.com/ciro/status/1488259161066459142)~~
- GitHub contributions graph?
- try out Qwiic I2C connections ~~(identify pins)~~
  - e.g. Qwiic twist to drive pixel intensity
- on-board web server for drawing / updating designs, setting and configuring pattern display and online source; also config wifi
- ...

### investigate

- RTC missing irq
- how to deepsleep
- esp32 temperature functions

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

```python
# needs non-zero keepalive for mosquitto 2.0.12+
c = MQTTClient("umqtt_client", "homebridge.local", keepalive=1)
```
