
import sense_emu
from sense_emu import SenseHat
import time
from time import sleep
import random
from random import seed
from random import randint
"""

  Sense HAT Sensors Display
  
  Select Temperature, Pressure, or Humidity  with the Joystick
  to visualize the current sensor values on the LED.
  
  Note: Requires sense_hat 2.2.0 or later
"""
#used to emulate a thermometer using a random number generator#
 
sense = SenseHat()

green = (0, 255, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)


def show_thigh():
    sense.show_letter("T", back_colour = red)
    sleep(0.5)
def show_tlow():
    sense.show_letter("T", back_colour = green)
    sleep(0.5)

def r():
    return random.randint(0,50)
    #seed(1)
    # sense.clear()


while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            temp = r()
            if temp <= 20:
                #print(randint(0,50))
                print(temp)
                show_tlow()
                selection = True
               # temp = r()
            sense.clear()
                
            if temp > 20:
                #print(randint(0,50))
                print(temp)
                show_thigh()
                selection = True
                #temp = r()
            sense.clear()

sense.clear()                
    
 
 
 