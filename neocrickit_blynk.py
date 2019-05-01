import blynklib
from adafruit_crickit import crickit

BLYNK_AUTH = '70a5204bd37a40e0a798a8f7e5a4abdb'

blynk = blynklib.Blynk(BLYNK_AUTH, server='192.168.42.1', port='8080')

crickit.init_neopixel(12)

@blynk.handle_event('write V2')
def set_led_colors(pin, value):
    neopix = crickit.neopixel
    neopix.fill((int(value[0]), int(value[1]), int(value[2])))

while True:
    blynk.run()
