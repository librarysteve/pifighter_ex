from adafruit_crickit import crickit
import blynklib

BLYNK_AUTH = 'ADD_API_KEY_HERE'

blynk = blynklib.Blynk(BLYNK_AUTH, server='SERVER_IP_HERE', port='8080')

momo1 = adafruit.dc_motor_1
momo2 = adafruit.dc_motor_2

@bynk.handle_event('write V0')
def go_forward{pin, value):
    if int(value[0]) == 1:
        momo1.throttle = 1
        momo2.throttle = 1
    else:
        momo1.throttle = 0
        momo2.throttle = 0

@bynk.handle_event('write V1')
def go_back(pin, value):
    if int(value[0]) == 1:
        momo1.throttle = -1
        momo2.throttle = -1
    else:
        momo1.throttle = 0
        momo2.throttle = 0

@bynk.handle_event('write V2')
def turn_right(pin, value):
    if int(value[0]) == 1:
        momo1.throttle = -1
        momo2.throttle = 1
    else:
        momo1.throttle = 0
        momo2.throttle = 0

@bynk.handle_event('write V3')
def turn_left(pin, value):
    if int(value[0]) == 1:
        momo1.throttle = 1
        momo2.throttle = -1
    else:
        momo1.throttle = 0
        momo2.throttle = 0
		
		
		
while True:
    blynk.run()
