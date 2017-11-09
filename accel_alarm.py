from sense_hat import SenseHat
from time import sleep

class accel_alarm():
	def __init__():
		self.sensor = SenseHat()
		self.running = False
		self.trigger_force = .01
	def arm():
		self.running = True
		self.loop()
	def disarm():
		self.running = False
	def loop():
		while(running):
			data = sensor.get_accelerometer_raw()
			if(data["x"] > self.trigger_force or data["y"] > self.trigger_force or data["z" > self.trigger_force]):
				print("SOUND THE ALARM")
			sleep(1)
if(__name__ == "__main__"):
	alarm = accel_alarm()
	alarm.arm()
