# MicroPython examples

## Requirements

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

Another option is to [use `mpremote`](https://docs.micropython.org/en/latest/reference/mpremote.html), the official MicroPython command-line tool.

## Programs

- `main.py` will run a series of simple tests on the LEDs.
- `cheerlights-demo.py` will display the [Cheerlights](https://cheerlights.com) colour on an ongoing basis. Needs to be edited with valid Wifi network values for your network.
- `aht20-test.py` reads and prints out values from an Adafruit AHT20 Temperature and Humidity sensor connected to the I2C port.

## More information

- [Bringing the bling with MicroPython](https://dev.to/andypiper/bringing-the-bling-with-micropython-hn1) (blog post, with background)
- [Making a CheerDot with MicroPython](https://dev.to/andypiper/making-a-cheerdot-with-micropython-3ocf) (blog series, part 2)
- [Using I2C in MicroPython](https://dev.to/andypiper/using-i2c-in-micropython-4b9n) (blog series, part 3)
- [MicroPython on ESP32 Forum](https://forum.micropython.org/viewforum.php?f=18)
- [MicroPython community Slack](https://slack-micropython.herokuapp.com/) (get an invite)
