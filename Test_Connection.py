import blynklib

'''
Non CrickitHAT test. Will print to std out with pin number and value.
This is useful for testing the stack for connectivity to the blynk server
also for testing the blynk app widgets and what values are sent.
'''

#Obtained from the app or server admin page
BLYNK_AUTH = 'authkeyhere'

#initialize Blynk in this script. The server IP for a local instance is 0.0.0.0, port is 8080
blynk = blynklib.Blynk(BLYNK_AUTH, server='server_ip_address', port='8080')


# Add whatever widget you want, just remember that the returned value is formatted as a list. 
# Default is a generic virtual imput handler
@blynk.handle_event('write V0')
def generic_input(pin, value):
    msg = "Virtual Pin Number {0} Value: {1}".format(pin, value)
    print(msg)

# If you wanted to use the zeRGBa color picker widget I think merge mode works best (setting in the app)
# uncomment to test :D
'''
@blynk.handel_event('write V1')
def zeRGBa_handler(pin, value):
# The msg in this line slices the list into thier individual RGB values
# This way you only have to use one vpin
    msg = "Red Value:{0} Green Value:{1} Blue Value:{3}".format(value[0], value[1], value[2])
    print(msg)
'''

# Run forever or until keyboard interrupt. 
while True:
    blynk.run()
