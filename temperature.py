from sense_hat import SenseHat
from timer import run_timer
from timer import clear
import time

cancelled = False
def temperature():
	sense = SenseHat()
	running = True
	baseTemperature = sense.get_temperature() #temperature of pi when initially started
	while running and not cancelled:
		time.sleep(.5)
		currTemperature = sense.get_temperature() #updated temperature
		if(abs(baseTemperature-currTemperature) >= .5): #checks if temperature has changed by .5 degrees since system started
			securityProtocol(baseTemperature - currTemperature)
			break

def cancel():
	cancelled = True
def securityProtocol(temperatureDifference):
	#text("Temperature change of: " + temperatureDifference + "detected!\nText this number your password if this was you.")
	run_timer()

if __name__ == '__main__':
    clear() # Clears the LED array
    temperature()
