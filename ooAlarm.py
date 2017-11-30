'''
Object-oriented version of `timer.py`
'''

import time
import pygame

G = (0, 255, 0)
Y = (255, 255, 0)
R = (255, 0, 0)
O = (0,0,0)

class Alarm:
    def __init__(self, senseHat):
        pygame.mixer.init()    #starts audio player
        pygame.mixer.music.load("alarm.wav")    #loads alarm file
        self.sh = senseHat
        self.sh.low_light = True
        self.phase = 0
        self.running = False
    
    def clear(self):
        grid = [
                O,O,O,O,O,O,O,O,
                O,O,O,O,O,O,O,O,
                O,O,O,O,O,O,O,O,
                O,O,O,O,O,O,O,O,
                O,O,O,O,O,O,O,O,
                O,O,O,O,O,O,O,O,
                O,O,O,O,O,O,O,O,
                O,O,O,O,O,O,O,O,
                ] 
        self.sh.set_pixels(grid)
    
    def get_grid(self):
        if self.phase == 0:
            grid = [
                    G,G,G,G,G,G,G,G,
                    G,G,G,G,G,G,G,G,
                    G,G,G,G,G,G,G,G,
                    G,G,G,G,G,G,G,G,
                    G,G,G,G,G,G,G,G,
                    G,G,G,G,G,G,G,G,
                    G,G,G,G,G,G,G,G,
                    G,G,G,G,G,G,G,G,
                    ]
        if self.phase == 1:
            grid = [
                    O,O,O,O,O,O,O,O,
                    O,O,O,O,O,O,O,O,
                    O,O,O,O,O,O,O,O,
                    Y,Y,Y,Y,Y,Y,Y,Y,
                    Y,Y,Y,Y,Y,Y,Y,Y,
                    Y,Y,Y,Y,Y,Y,Y,Y,
                    Y,Y,Y,Y,Y,Y,Y,Y,
                    Y,Y,Y,Y,Y,Y,Y,Y
                    ]
        if self.phase == 2:
            grid = [
                    O,O,O,O,O,O,O,O,
                    O,O,O,O,O,O,O,O,
                    O,O,O,O,O,O,O,O,
                    O,O,O,O,O,O,O,O,
                    O,O,O,O,O,O,O,O,
                    R,R,R,R,R,R,R,R,
                    R,R,R,R,R,R,R,R,
                    R,R,R,R,R,R,R,R
                    ] 
        return grid
    def run_timer(self, lock):
        #sets array to all green initially
        self.sh.set_pixels(self.get_grid())
        for r in range(0, 8):
            for c in range(0,8):
                if(r == 3 and c == 0): #if starting 3rd row, set active pixels to yellow
                    self.phase = 1
                    self.sh.set_pixels(self.get_grid())
                if(r == 5 and c == 0): #if starting 5th row, set active pixels to red
                    self.phase = 2
                    self.sh.set_pixels(self.get_grid())
                self.sh.set_pixel(c,r,0,0,0)
                time.sleep(1.40625) #1.40625 is 90/64, so timer takes 1.5 min to complete
            with lock:
                if not self.running:
                    break
        else:
            for i in range(0,3):	#loops alarm 3 times
                pygame.mixer.music.play()	#starts alarm
                while pygame.mixer.music.get_busy() == True:#plays alarm until completion
                    continue
        