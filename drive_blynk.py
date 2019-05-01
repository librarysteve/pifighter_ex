import blynklib
from adafruit_crickit import crickit

# Copy and paste api key between single quotes:
BLYNK_AUTH = ''

# For LexPubLib class this does not need to be altered
blynk = blynklib.Blynk(BLYNK_AUTH, server='192.168.42.1', port='8080')

# Recommended settings for 5V solenoid
crickit.drive_1.frequency = 1000


@blynk.handle_event('write V5')
def actuate_solinoid(pin, value):
    drive = crickit.drive_1
    drive.fraction = int(value[0])


while True:
    blynk.run()
