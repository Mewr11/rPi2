from time import sleep

import singular

class Accel_alarm:
    def __init__(self):
        self.running = False
        self.trigger_force = 2
    def arm(self):
        self.running = True
        self.loop()
    def disarm(self):
        singular.sms.call("+1<Your Number Here>", '''
                 We Have detected an unexpected door opening.
                 Respond with "Shut Up" (without the quotes) to disarm.
                 ''')
        self.running = False
    def loop(self, lock=singular.lock):
        while(self.running):
            data = singular.sh.get_accelerometer_raw()
            if self.debug:
                print(data)
            if(data["x"] > self.trigger_force or data["y"] > self.trigger_force or data["z"] > self.trigger_force):
                print("SOUND THE ALARM")
                self.disarm()
                with lock:
                    if not singular.alarm.running:
                        singular.alarm.running = True
            sleep(1)

if(__name__ == "__main__"):
	alarm = Accel_alarm()
	alarm.arm()
