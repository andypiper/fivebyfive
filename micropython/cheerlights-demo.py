# Cheerlights - all pixels
# Uses the Cheerlights MQTT API to switch the LED colours to the
# current RGB value from Twitter / Cheerlights
#
# Update via a Tweet with the content "#cheerlights <colour>"
# see https://cheerlights.com for more information
#
# blog: https://dev.to/andypiper/making-a-cheerdot-with-micropython-3ocf
#
# requires umqtt - e.g. in REPL, with wifi connected on board
#
# import upip
# upip.install('micropython-umqtt.robust')
# upip.install('micropython-umqtt.simple')

import machine
import network
from umqtt.robust import MQTTClient
from machine import Pin
from neopixel import NeoPixel

# config network and broker
my_ssid = "network_name"
my_pass = "pass_word"
cl_broker = "mqtt.cheerlights.com"

neopin = Pin(8, Pin.OUT)  # NeoPixel control on Pin 8
pixels = 25  # we have 25 pixels, set as a constant here for loops
np = NeoPixel(neopin, pixels)

# setup the status LED
status_led = Pin(10, Pin.OUT)


def do_connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.config(dhcp_hostname=client_name())
    if not wlan.isconnected():
        status_led.off()
        print("connecting to network...")
        wlan.connect(my_ssid, my_pass)
        while not wlan.isconnected():
            pass
    status_led.on()  # status LED shows connected
    print("network config:", wlan.ifconfig())


def cl_callback(topic, payload):
    cl_rgb = hex_to_rgb(payload)
    print("message received: " + str(cl_rgb))
    light_up(cl_rgb)


def hex_to_rgb(hex_string):
    str_len = len(hex_string)
    if hex_string.startswith("#"):
        if str_len == 7:
            r_hex = hex_string[1:3]
            g_hex = hex_string[3:5]
            b_hex = hex_string[5:7]
        elif str_len == 4:
            r_hex = hex_string[1:2] * 2
            g_hex = hex_string[2:3] * 2
            b_hex = hex_string[3:4] * 2
    elif str_len == 3:
        r_hex = hex_string[0:1] * 2
        g_hex = hex_string[1:2] * 2
        b_hex = hex_string[2:3] * 2
    else:
        r_hex = hex_string[0:2]
        g_hex = hex_string[2:4]
        b_hex = hex_string[4:6]

    return int(r_hex, 16), int(g_hex, 16), int(b_hex, 16)


def client_name():
    m_id = machine.unique_id()
    client_id = (
        "{:02x}{:02x}{:02x}{:02x}".format(m_id[0], m_id[1], m_id[2], m_id[3])
        + "-cl-dot"
    )
    return client_id


def light_up(rgb):
    # Set all Neopixels to colour
    np.fill(rgb)
    np.write()


# the main code
# connect to network and broker and subscribe to Cheerlights RGB topic

do_connect()
mqtt = MQTTClient(client_name(), cl_broker)
mqtt.connect()
mqtt.set_callback(cl_callback)
mqtt.subscribe("cheerlightsRGB")

while True:
    mqtt.check_msg()
