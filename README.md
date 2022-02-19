# "Five by Five"

Multilingual code for a 01Space 5x5 Neopixel RISC V board (ESP32-C3FH4 with USB-C) - sometimes called a "bedazzled" ESP32-C3!

## Background

It all started with [this Tweet from @GeekMomProjects](https://twitter.com/GeekMomProjects/status/1479210241807900676)...

Now, the goal of this project is to aggregate information, and different examples, to enable the community to learn about and use the ESP32-C3FH4-RGB board, created by [01Space](https://github.com/01Space).

## Requirements

- the board, available to purchase [via Banggood](https://banggood.com/ESP32-C3-Development-Board-RISC-V-WiFi-Bluetooth-IoT-Development-Board-Compatible-with-Python-p-1914005.html)
  - a USB-A to USB-C data cable

## Contents

- [`arduino/`](./arduino) updated version of the original Arduino code for the board (may need to populate via `git pull --recurse-submodules`)
- [`micropython/`](./micropython) MicroPython code examples
- [`tinygo/`](./tinygo) TinyGo code examples

Each language subdirectory contains more information specific to build and installation.

- [`images/`](./images) various images to illustrate functionality and the board itself
- [`reference/`](./reference) annotated images and schematics

### More information

- various learnings in the [notes](notes.md) (will be organised into a GH wiki soon)
- [YouTube playlist](https://www.youtube.com/watch?v=SQO4Dn0vE3k&list=PLBlxSZoETPB-GN-FPKTdkK5IxIUz5LEIO) showing some of these samples

### Images

![01Space board](images/board-neopixels.jpeg)

![01Space board reverse](images/board-chips.jpeg)

![Annotated board](/reference/ESP32-C3FH4-RGB-reference.jpeg)

More images in [`images/`](images/), PDF/JPEG reference cards in [`reference/`](reference/) (schematic to come)

## License

MIT License Copyright (c) 2022 Andy Piper

## Contributing

See [Contributing](./CONTRIBUTING.md), and follow the [Code of Conduct](.github/CODE_OF_CONDUCT.md). Thanks!
