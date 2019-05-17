import blynklib

'''
Non CrickitHAT test. Will print to std out with pin number and value.
This is useful for testing the stack for connectivity to the blynk server
also for testing the blynk app widgets.
'''

#Obtained from the app or server admin page
BLYNK_AUTH = 'authkeyhere'

#initialize Blynk in this script. The port for a local instance is 8080
blynk = blynklib.Blynk(BLYNK_AUTH, server='server_ip_address', port='8080')

@blynk.handle_event('write V0')
def when_button_is_pressed(pin, value):
    msg = "Virtual Pin Number {0} Value: {1}".format(pin, value)
    print(msg)

# Run forever or until keyboard interrupt. 
while True:
    blynk.run()
