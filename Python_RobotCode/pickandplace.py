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

# Create object code here for windows version
mc = MyCobot("/dev/ttyACM0", 115200)
# mc.release_all_servos()
# while True:
#     print(mc.get_angles())
#     mc.release_all_servos()
mc.send_angles([0, 0, 0, 0, 0, 0], 40)
time.sleep(5)
mc.send_angles([10.19, -80.16, -2.02, 125.33, 0.87, -3.51],40)
time.sleep(5)
mc.send_angles([10.19, -46.4, -0.43, 125.33, 0.87, -3.51],40)
time.sleep(5)
mc.send_angles([46.93, -40.4, -0.43, -10.28, -2.98, -16.87],40)
time.sleep(5)

gripper_test(mc)
time.sleep(5)

mc.send_angles([16.93, -40.4, -0.43, -10.28, -2.98, -16.87],20)
time.sleep(5)
gripper_test(mc)
time.sleep(5)

mc.send_angles([46.93, -40.4, -0.43, -10.28, -2.98, -16.87],20)
time.sleep(5)

mc.send_angles([10.19, -46.4, -0.43, 125.33, 0.87, -3.51],40)
time.sleep(5)
mc.send_angles([10.19, -100.16, -2.02, 125.33, 0.87, -3.51],20)
time.sleep(5) 


# mc.send_angles([90.52, 157.67, -28.56, -111.09, 93.07, -0.7],40)
# time.sleep(5)
# #gripper_test(mc)
# #time.sleep(5)
# mc.send_angles([20.39, 96.76, -73.82, 68.29, 167.08, 13.88],40)
# time.sleep(5)
#gripper_test(mc)
#time.sleep(3)

# mc.send_angles([177.01, -29.97, -30.32, -6.76, 2.19, 0.0],40)
# time.sleep(5)
# mc.send_angles([90.26, 67.85, -156.26, 104.06, 2.46, 0.26],40)
# time.sleep(5)
# mc.release_all_servos()
# print(mc.get_angles())
# gripper_test(mc)
# time.sleep(3)
# mc.send_angles([90.61, 155.21, -155.74, 149.15, 83.75, 0.26],40)
# time.sleep(3)
# gripper_test(mc)
# time.sleep(3)
# mc.send_angles([90.96, 155.3, -156.88, 104.06, 2.46, 0.26],40)
# time.sleep(3)
# gripper_test(mc)
# time.sleep(3)
# mc.send_angles([91.66, 158.11, -28.91, -26.27, 2.81, 0.26],40)
# time.sleep(3)
# mc.release_all_servos()