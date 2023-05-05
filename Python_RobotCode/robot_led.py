from pymycobot.mycobot import MyCobot

from pymycobot import PI_PORT, PI_BAUD      # When using the Raspberry Pi version of mycobot, you can refer to these two variables to initialize MyCobot, if not, you can omit this line of code
import time


# Initialize a MyCobot object
# Create object code here for windows version
mc = MyCobot("/dev/ttyACM0", 115200)

i = 7
#loop 7 times
while i > 0:                            
    mc.set_color(0,0,255) #blue light on
    time.sleep(2)    #wait for 2 seconds                
    mc.set_color(255,0,0) #red light on
    time.sleep(2)    #wait for 2 seconds
    mc.set_color(0,255,0) #green light on
    time.sleep(2)    #wait for 2 seconds
    i -= 1