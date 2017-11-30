'''
This provides a way to ensure we only ever have one SenseHat, alarm thread, lock, etc.
See http://effbot.org/pyfaq/how-do-i-share-global-variables-across-modules.htm for more information
'''

alarm = None
sms = None
acc = None
tmp = None
lock = None
sh = None