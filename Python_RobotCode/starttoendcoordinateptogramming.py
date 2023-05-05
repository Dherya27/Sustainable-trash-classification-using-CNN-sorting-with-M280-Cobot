from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot.genre import Coord 
from pymycobot import PI_PORT, PI_BAUD  # When using the Raspberry Pi version of mycobot, you can refer to these two variables to initialize MyCobot
import time

velocity = 30
delay = 5

mc = MyCobot("/dev/ttyACM0", 115200)

#Initialize the stating point:
mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
time.sleep(delay)


#Cartesian control

#Location-1 : Drop-off
mc.send_coords([215.7, 68.5, 263.6, -155.42, -10.56, -58.3],velocity,1)
time.sleep(delay)


#Location-2: Drop-off
mc.send_coords([160.3, 179.6, 272.9, -150.89, -6.13, -8.37],velocity,1)
time.sleep(delay)

#Joint space control:
mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
time.sleep(delay)

#Go back rest:
mc.send_coords([77.6, -189.8, -14.0, 13.93, -4.22, 4.04], velocity,1)
time.sleep(delay)

#Approach: Location-2 directly:
mc.send_coords([160.3, 179.6, 272.9, -150.89, -6.13, -8.37],velocity,1)
time.sleep(delay)

#Back to Starting point:
mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
time.sleep(delay)

#Back to rest
mc.send_coords([77.6, -189.8, -14.0, 13.93, -4.22, 4.04], velocity,1)
time.sleep(delay)

#Approach: Location-1 directly:
mc.send_coords([215.7, 68.5, 263.6, -155.42, -10.56, -58.3],velocity,1)
time.sleep(delay)

#Back to Starting point:
mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
time.sleep(delay)

#Back to rest
mc.send_coords([77.6, -189.8, -14.0, 13.93, -4.22, 4.04], velocity,1)
time.sleep(delay)

