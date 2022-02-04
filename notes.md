### Board on macOS

- location varies -> `/dev/tty.usbmodem21301` on my M1 Pro

```text
USB JTAG/serial debug unit:

  Product ID:	0x1001
  Vendor ID:	0x303a
  Version:	1.01
  Serial Number:	84:F7:03:A0:F3:80
  Speed:	Up to 12 Mb/s
  Manufacturer:	Espressif
  Location ID:	0x01130000 / 4
  Current Available (mA):	500
  Current Required (mA):	500
  Extra Operating Current (mA):	0
```

**USB ID**	1001:303a

**VID** - 303a - Espressif
**PID** - 1001 - USB JTAG/serial debug / ESP32-C3

Noting that this is not in the [Espressif allocated list of PIDs](https://github.com/espressif/usb-pids/blob/main/allocated-pids.txt)

### Manufacturer:

- https://github.com/01Space/ESP32-C3FH4-RGB
  - works fine using the ESP32 Arduino core v2.0.2 / ESP32C3 Dev Module board in Arduino IDE 2.0
  - code has NeoPixel on pin 8, 800 KHz with GRBW


- https://www.youtube.com/watch?v=m-cgaS6eHv4

```
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


- https://www.cnx-software.com/2022/01/07/board-with-25-rgb-leds-is-offered-with-esp32-c3-or-esp32-pico-d4/


### MicroPython

Flash:

```shell
$ esptool.py --chip esp32c3 --port /dev/tty.usbmodem523201 erase_flash
$ esptool.py --chip esp32c3 --port /dev/ttyUSB0 --baud 460800 write_flash -z 0x0 esp32c3-20220117-v1.18.bin
```

- https://github.com/micropython/micropython/issues/8109

Works fully from the `v1.18-68-g1f04a9a1f` nightly.

Yet to test the pins or the mystery (possibly Qwiic or Grove-compatible?) 4-pin connector on the board.


### CircuitPython

Look into this - similar board
https://circuitpython.org/board/ai_thinker_esp32-c3s/

NB the CP docs list a C3 DevKit for module compat, but no download - ask on Discord

### Ideas

- play with rshell (https://core-electronics.com.au/tutorials/getting-started-with-raspberry-pi-pico.html)
- CheerPixel! (CheerDot? CheerSpot?)
- try the Wordle thing https://twitter.com/ciro/status/1488259161066459142
- GitHub contributions?
- ...


### Reference

![Annotated board](/reference/ESP32-C3FH4-RGB-reference.jpeg)

