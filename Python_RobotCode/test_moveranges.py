from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD  # When using the Raspberry Pi version of mycobot, you can refer to these two variables to initialize MyCobot
import time

def gripper_test(mc):
    print("Start check IO part of api\n")
    # Check if the gripper is moving
    flag = mc.is_gripper_moving()
    print("Is gripper moving: {}".format(flag))
    time.sleep(1)

    # Set the state of the gripper to quickly open the gripper at a speed of 70
    mc.set_gripper_state(0, 70)
    time.sleep(1)
    # Set the state of the gripper so that it quickly closes the gripper at a speed of 70
    mc.set_gripper_state(1, 70)
    time.sleep(1)

    # Get the value of the gripper
    print("")
    print(mc.get_gripper_value())
velocity = 30
delay = 2
# Create object code here for windows version
mc = MyCobot("/dev/ttyACM0", 115200)
# mc.release_all_servos()
# while True:
#     print(mc.get_angles())
#     mc.release_all_servos()
mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
time.sleep(delay)

#Joint-1
mc.send_angles([90, 20, 0, 0, 0, 0], velocity)
time.sleep(delay)
mc.send_angles([-30, 20, 0, 0, 0, 0], velocity)
time.sleep(delay)
mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
time.sleep(delay)

#Joint-2 
mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
time.sleep(delay)
mc.send_angles([0, -20, 0, 0, 0, 0], velocity)
time.sleep(delay)
mc.send_angles([0, -60, 90, 0, 0, 0], velocity)
time.sleep(delay)

#Joint-2 
mc.send_angles([0, -60, 0, 0, 0, 0], velocity)
time.sleep(delay)

#Lift up a little
mc.send_angles([91.66, 158.11, -28.91, -26.27, 2.81, 0.26],velocity)
time.sleep(5)

mc.release_all_servos()





