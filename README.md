# "Five by Five"

MicroPython code for a 01Space 5x5 Neopixel board (ESP32-C3FH4 with USB-C)

It all started with [this Tweet from @GeekMomProjects](https://twitter.com/GeekMomProjects/status/1479210241807900676)...

## Images

![01Space board](images/board-neopixels.jpeg)

![01Space board reverse](images/board-chips.jpeg)

More images in [`images/`](images/), PDF/JPEG reference cards in [`reference/`](reference/)

![Annotated board](/reference/ESP32-C3FH4-RGB-reference.jpeg)

## Requirements

- board from [here](https://banggood.com/ESP32-C3-Development-Board-RISC-V-WiFi-Bluetooth-IoT-Development-Board-Compatible-with-Python-p-1914005.html)
- MicroPython build from [here](https://micropython.org/download/esp32c3-usb/)

### Installing MicroPython modules

I've used the REPL and `upip` to put the dependencies on the board. If you are using e.g. [Thonny](https://thonny.org/), connect to the REPL and run Python code to join a wifi network from the board. Then:

```python
import upip
upip.install('micropython-umqtt.robust')
upip.install('micropython-umqtt.simple')
```

The modules will be installed to `/lib` on the board. You can also use e.g. `ampy` to copy the modules onto the board.

```text
ampy -p /dev/cu.usbmodem11301 mkdir lib
ampy -p /dev/cu.usbmodem11301 put ahtx0.py lib/ahtx0.py
```

## Programs

- `main.py` will run a series of simple tests on the LEDs.
- `cheerlights-demo.py` will display the [Cheerlights](https://cheerlights.com) colour on an ongoing basis. Needs to be edited with valid Wifi network values for your network.
- `aht20-test.py` reads and prints out values from an e.g. Adafruit AHT20 Temperature and Humidity sensor connected to the Qwiic port.

## More information

- various learnings in the [notes](notes.md) (which I could probably have done as a GH wiki...)
- [Bringing the bling with MicroPython](https://dev.to/andypiper/bringing-the-bling-with-micropython-hn1) (blog post, with background)
- [Making a CheerDot with MicroPython](https://dev.to/andypiper/making-a-cheerdot-with-micropython-3ocf) (blog series, part 2)

### LICENSE

MIT License Copyright (c) 2022 Andy Piper

### CONTRIBUTING

See [Contributing](CONTRIBUTING.md) and follow the [Code of Conduct](.github/CODE_OF_CONDUCT.md). Thanks!
