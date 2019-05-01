import blynklib
from adafruit_crickit import crickit

BLYNK_AUTH = 'eeb9358de3be47d6b4364d7f81ac247d'

blynk = blynklib.Blynk(BLYNK_AUTH, server='192.168.42.1', port='8080')

@blynk.handle_event('write V5')
def move_servo1(pin, value):
    crickit.servo_1.angle = int(value[0])

@blynk.handle_event('write V6')
def move_servo2(pin, value):
    crickit.servo_2.angle = int(value[0])


while True:
    blynk.run()
