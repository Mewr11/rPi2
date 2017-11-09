from sense_hat import SenseHat
from time import sleep
from timer import timer 

class accel_alarm():
	def __init__(self):
		self.sensor = SenseHat()
		self.running = False
		self.trigger_force = 2
	def arm(self):
		self.running = True
		self.loop()
	def disarm(self):
		self.running = False
	def loop(self):
		while(self.running):
			data = self.sensor.get_accelerometer_raw()
			print(data)
			if(data["x"] > self.trigger_force or data["y"] > self.trigger_force or data["z"] > self.trigger_force):
				print("SOUND THE ALARM")
				self.disarm()
				run_timer()
			sleep(1)

if(__name__ == "__main__"):
	alarm = accel_alarm()
	alarm.arm()
