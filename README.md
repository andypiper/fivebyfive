# "Five by Five"

MicroPython code for a 01Space 5x5 Neopixel board (ESP32-C3FH4 with USB-C)

It all started with [this Tweet from @GeekMomProjects](https://twitter.com/GeekMomProjects/status/1479210241807900676)...

## Images

![01Space board](images/board-neopixels.jpeg)

![01Space board reverse](images/board-chips.jpeg)

## Requirements

- board from [here](https://banggood.com/ESP32-C3-Development-Board-RISC-V-WiFi-Bluetooth-IoT-Development-Board-Compatible-with-Python-p-1914005.html)
- MicroPython build from [here](https://micropython.org/download/esp32c3-usb/)

### Installing MicroPython modules

I've used the REPL and `upip`. Using e.g. [Thonny](https://thonny.org/), connect to the REPL and connect to the wifi from the board. Then:

```python
import upip
upip.install('micropython-umqtt.robust')
upip.install('micropython-umqtt.simple')
```

The modules will be installed to `/lib` on the board. You can also use e.g. `ampy` to copy the modules onto the board.

## More information

- learnings in the [notes](notes.md) (which I could probably have done as a GH wiki...)
- [blog post](https://dev.to/andypiper/bringing-the-bling-with-micropython-hn1) with background
