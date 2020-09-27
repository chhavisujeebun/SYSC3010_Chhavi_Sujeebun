from sense_emu import SenseHat
from time import sleep
import time
sense = SenseHat()
blue = (0,0,255)
# My initial CS
#defining function to display C
def show_C():
  sense.show_letter("C", back_colour =blue )
#function to display S
def show_S():
  sense.show_letter("S", back_colour = blue)





# when press is odd C will be displayed, when press is even S will be displayed
## Main Program

press = 1
while True:
    for event in sense.stick.get_events():
        if event.action == "pressed":
            if press % 2 != 0 :
                show_C()
                press = press + 1
                selection = True
        
        
            elif press % 2 == 0:
                show_S()
                press = press + 1
                selection = True
        
   
        sleep(0.5)
sense.clear()  