from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD  # When using the Raspberry Pi version of mycobot, you can refer to these two variables to initialize MyCobot
import time

mc = MyCobot("/dev/ttyACM0", 115200)

record_jointvalues = []
recorded_items = 0
mc.release_all_servos()
while recorded_items < 100:
    print(mc.get_angles())
    record_jointvalues.append(mc.get_angles())
    print(recorded_items)
    recorded_items = recorded_items+1

print(record_jointvalues)