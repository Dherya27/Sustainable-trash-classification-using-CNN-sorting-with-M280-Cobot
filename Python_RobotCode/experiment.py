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

    # Set the current position to (2048).
    # Use it when you are sure you need it.
    # Gripper has been initialized for a long time. Generally, there
    # is no need to change the method.
    # mc.set_gripper_ini()
    # Set joint point 1 to rotate to the position of 2048
    #mc.set_encoder(1, 2048)
    #time.sleep(2)
    # Set six joint positions and let the robotic arm rotate to this position at a speed of 20
    #mc.set_encoders([1024, 1024, 1024, 1024, 1024, 1024], 20)
    #time.sleep(3)
    # Get the position information of joint point 1
    #print(mc.get_encoder(1))
    # Set the gripper to rotate to the position of 2048
    #mc.set_encoder(7, 2048)
    #time.sleep(3)
    # Set the gripper to rotate to the position of 1300
    #mc.set_encoder(7, 1300)
    #time.sleep(3)

    # Let the gripper reach the state of 2048 at a speed of 70
    #mc.set_gripper_value(2048, 70)
    #time.sleep(3)
    # Let the gripper reach the state of 1500 at a speed of 70
    #mc.set_gripper_value(1500, 70)
    #time.sleep(3)

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
mc.send_angles([90.26, 67.85, -156.26, 104.06, 2.46, 0.26],40)
time.sleep(5)
print(mc.get_angles())
gripper_test(mc)
time.sleep(3)
mc.send_angles([90.61, 155.21, -155.74, 149.15, 83.75, 0.26],40)
time.sleep(3)
gripper_test(mc)
time.sleep(3)
mc.send_angles([90.96, 155.3, -156.88, 104.06, 2.46, 0.26],40)
time.sleep(3)
gripper_test(mc)
time.sleep(3)
mc.send_angles([91.66, 158.11, -28.91, -26.27, 2.81, 0.26],40)
time.sleep(3)
mc.release_all_servos()



