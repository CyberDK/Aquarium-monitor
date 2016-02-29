import webiopi
import datetime

# Enable debug output
webiopi.setDebug()

# Retrieve GPIO lib
GPIO = webiopi.GPIO

diagnostics = True

def setup():
	print ("Setting up...")
	#STATE VARIABLES
	global Relay1, Relay2, Relay3, Relay4, Relay5, Relay6, Relay7, Relay8, diagnostics
	#SETUP GPIO
	GPIO.setFunction(2, GPIO.OUT) #Relay1
	GPIO.setFunction(3, GPIO.OUT) #Relay2
	GPIO.setFunction(4, GPIO.OUT) #Relay3
	GPIO.setFunction(17, GPIO.OUT) #Relay4
	GPIO.setFunction(27, GPIO.OUT) #Relay5
	GPIO.setFunction(22, GPIO.OUT) #Relay6
	GPIO.setFunction(10, GPIO.OUT) #Relay7
	GPIO.setFunction(9, GPIO.OUT) #Relay8
	# ENSURE ALL OFF
	GPIO.digitalWrite(2, GPIO.HIGH) #Relay1
	GPIO.digitalWrite(3, GPIO.HIGH) #Relay2
	GPIO.digitalWrite(4, GPIO.HIGH) #Relay3
	GPIO.digitalWrite(17, GPIO.HIGH) #Relay4
	GPIO.digitalWrite(27, GPIO.HIGH) #Relay5
	GPIO.digitalWrite(22, GPIO.HIGH) #Relay6
	GPIO.digitalWrite(10, GPIO.HIGH) #Relay7
	GPIO.digitalWrite(9, GPIO.HIGH) #Relay8

def destroy():
    GPIO.digitalWrite(2, GPIO.HIGH) #Relay1
    GPIO.digitalWrite(3, GPIO.HIGH) #Relay2
    GPIO.digitalWrite(4, GPIO.HIGH) #Relay3
    GPIO.digitalWrite(17, GPIO.HIGH) #Relay4
    GPIO.digitalWrite(27, GPIO.HIGH) #Relay5
    GPIO.digitalWrite(22, GPIO.HIGH) #Relay6
    GPIO.digitalWrite(10, GPIO.HIGH) #Relay7
    GPIO.digitalWrite(9, GPIO.HIGH) #Relay8

@webiopi.macro
def relayControl(number):
    if diagnostics:
        print("Toggle light: %s" % int(number))
        
    if int(number) == 1:
        GPIO.digitalWrite(2, GPIO.LOW) #Relay1

    if int(number) == 2:
        GPIO.digitalWrite(3, GPIO.LOW) #Relay2
        
    if int(number) == 3:
        GPIO.digitalWrite(17, GPIO.LOW) #Relay3        
        
    return ()