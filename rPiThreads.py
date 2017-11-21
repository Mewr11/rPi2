import sms
import temperature
import accel_alarm

import time
import threading

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

class Temp_Thread(threading.Thread):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        temperature.temperature()

class Accel_Thread(threading.Thread, accel_alarm.accel_alarm):
    def __init__(self, name, counter):
        threading.Thread.__init__(self)
        accel_alarm.accel_alarm.__init__(self)
        self.threadID = counter
        self.name = name
        self.counter = counter
    def run(self):
        self.arm()

if __name__ == '__main__':
    global smsThread = SMS_Thread("Thread 1 - SMS", 0)
    global tmpThread = Temp_Thread("Thread 2 - Temperature", 1)
    global accThread = Accel_Thread("Thread 3 - Acceleration", 2)
