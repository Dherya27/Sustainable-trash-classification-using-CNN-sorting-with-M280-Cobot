from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot.genre import Coord 
from pymycobot import PI_PORT, PI_BAUD  # When using the Raspberry Pi version of mycobot, you can refer to these two variables to initialize MyCobot
import time

mc = MyCobot("/dev/ttyACM0", 115200)
mc.release_all_servos()
while True:
    print(mc.get_coords())
    mc.release_all_servos()