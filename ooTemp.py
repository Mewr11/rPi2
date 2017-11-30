import time

class Temperature:
    def __init__(self, sms, senseHat, alarm, delta=5):
        self.sms = sms
        self.sh = senseHat
        self.base = self.sh.get_temperature()
        self.alarm = alarm
        self.delta = delta
    
    def temperature(self, lock):
        while True:
            time.sleep(.5)
            curr_temp = self.sh.get_temperature()
            if abs(self.base - curr_temp) >= self.delta:
                with lock:
                    if not self.alarm.running:
                        self.alarm.running = True
  