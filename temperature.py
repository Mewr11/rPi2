from sense_hat import SenseHat
from timer import run_timer
from timer import clear
import time

clear() #clears led array

def temperature():
	sense = SenseHat()
	running = True
	baseTemperature = sense.get_temperature() #temperature of pi when initially started
	while running:
		time.sleep(.5)
		currTemperature = sense.get_temperature() #updated temperature
		if(abs(baseTemperature-currTemperature) >= .5):#checks if temperature has changed by .5 degrees since system started
			securityProtocol(baseTemperature - currTemperature)
			break

def securityProtocol(temperatureDifference):
	#text("Temperature change of: " + temperatureDifference + "detected!\nText this number your password if this was you.")
	run_timer()
temperature()