#define MICROPY_HW_BOARD_NAME               "01Space ESP32-C3FH4-RGB"
#define MICROPY_HW_MCU_NAME                 "ESP32-C3FH4"

#define MICROPY_HW_USB_VID (0x1001)
#define MICROPY_HW_USB_PID (0x303a)

#define MICROPY_HW_ENABLE_SDCARD            (0)
#define MICROPY_PY_MACHINE_DAC              (0)
#define MICROPY_PY_MACHINE_I2S              (0)

// STEMMA QT / Qwiic on I2C0
#define MICROPY_HW_I2C0_SCL                 (1)
#define MICROPY_HW_I2C0_SDA                 (0)

// Boot button GPIO 9
// Status LED GPIO 10
// NeoPixels GPIO 8
