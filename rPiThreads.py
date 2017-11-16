import sms

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

if __name__ == '__main__':
    t1 = Test_Thread('Myself', 0)
    t2 = Test_Thread('This', 1)

    t1.start()
    t2.start()

    t1.join()
    t2.join()
    print('Exiting the program')
