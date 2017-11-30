import sms
import ooTemp
import accel_alarm
import ooAlarm
import singular.py

import time
import threading
from sense_hat import SenseHat

class Test_Thread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        print('Starting ' + self.name)
        time.sleep(5)
        print('Ending ' + self.name)

class SMS_Thread(sms.SMS, threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        sms.SMS.__init__(self, autorun=False)
        self.threadID = counter
        self.name = name
        self.counter = counter

    def run(self):
        self.flask.run()

class Temp_Thread(threading.Thread, ooTemp.Temperature):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        ooTemp.Temperature.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        self.arm()

class Accel_Thread(threading.Thread, accel_alarm.Accel_alarm):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        accel_alarm.Accel_alarm.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        self.arm()

class Alarm_Thread(threading.Thread, ooAlarm.Alarm):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        ooAlarm.Alarm.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        self.detection_loop()
        

if __name__ == '__main__':
    singular.sh = SenseHat()
    singular.lock = threading.Lock()
    singular.sms = SMS_Thread("Thread 0 - SMS", 0)
    singular.alarm = Alarm_Thread("Thread 1 - Alarm", 1)
    singular.tmp = Temp_Thread("Thread 2 - Temperature", 2)
    singular.acc = Accel_Thread("Thread 3 - Acceleration", 3)
