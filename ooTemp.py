import singular

import time

class Temperature:
    def __init__(self, delta=5):
        self.base = singular.sh.get_temperature()
        self.delta = delta
        self.running = False
    
    def arm(self):
        self.running = True
        self.loop()
    
    def disarm(self):
        singular.sms.call("+1<Your Number Here>", '''
                 We Have detected an unexpected change in temperature.
                 Respond with "Shut Up" (without the quotes) to disarm.
                 ''')
        self.running = False
    
    def loop(self, lock=singular.lock):
        while self.running:
            time.sleep(2)
            curr_temp = singular.sh.get_temperature()
            if abs(self.base - curr_temp) >= self.delta:
                with lock:
                    if not singular.alarm.running:
                        singular.alarm.running = True
  