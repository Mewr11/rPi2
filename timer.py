from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

G = (0, 255, 0)
Y = (255, 255, 0)
R = (255, 0, 0)
O = (0,0,0)

#clears array of LEDs
def clear():
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
	s.set_pixels(grid)

#sets LED's that are currently lit to color that reflects amount of time left
#takes a phase value determined by run_timer()
def timer(phase=0):
        if phase == 0:
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
        if phase == 1:
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
        if phase == 2:
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

#changes grid by ticking down for a total of 90 seconds
def run_timer():
	phase = 0
	running = True
	while running:
		#sets array to all green initially
	        s.set_pixels(timer(phase))
	        for r in range(0, 8):
	                for c in range(0,8):
	                        if(r == 3 and c == 0): #if starting 3rd row, set active pixels to yellow
	                                phase = 1
	                                s.set_pixels(timer(phase))
	                        if(r == 5 and c == 0): #if starting 5th row, set active pixels to red
	                                phase = 2
	                                s.set_pixels(timer(phase))
	                        s.set_pixel(c,r,0,0,0)
	                        time.sleep(1.40625) #1.40625 is 90/64, so timer takes 1.5 min to complete
        	running = False

