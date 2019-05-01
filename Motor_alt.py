import blynklib
from adafruit_crickit import crickit

BLYNK_AUTH = '9fbbe3ae7f2a4a16827b6d4682bc0b2e'

# initialize Blynk
blynk = blynklib.Blynk(BLYNK_AUTH, server='10.1.0.124', port='8080')


@blynk.handle_event('write V0')
def virt_0_input(pin, value):
    speed = float(value[0])
    momo1 = crickit.dc_motor_1
    print("mo1 speed is: " + str(speed))
    momo1.throttle = speed

@blynk.handle_event('write V1')
def virt_1_input(pin, value):
    speed = float(value[0])
    momo2 = crickit.dc_motor_2
    print("mo2 speed is: " + str(speed))
    momo2.throttle = speed


while True:
    blynk.run()
