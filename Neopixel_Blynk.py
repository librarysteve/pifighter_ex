import blynklib
from adafruit_crickit import crickit

BLYNK_AUTH = 'apikeyhere'
# Exclude server and port for use with Blynk server
blynk = blynklib.Blynk(BLYNK_AUTH, server='SERVER_IP_HERE', port='8080')

crickit.init_neopixel(12)

@blynk.handle_event('write V2')
def set_led_colors(pin, value):
    neopix = crickit.neopixel
    neopix.fill((int(value[0]), int(value[1]), int(value[2])))

while True:
    blynk.run()
