from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot.genre import Coord 
from pymycobot import PI_PORT, PI_BAUD  # When using the Raspberry Pi version of mycobot, you can refer to these two variables to initialize MyCobot
import time

velocity = 30
m1 = MyCobot("/dev/ttyACM0", 115200)
m1.send_angles([0, 20, 0, 0, 0, 0], velocity)
time.sleep(5)
m1.send_coords([-208.4, -61.9, 296.0, -150.49, 3.71, 105.5],velocity,1) #center
time.sleep(5)
m1.send_coords([-254.3, -118.2, 206.5, -154.0, -0.95, 130.33],velocity,1) #Go down
time.sleep(5)



# Set the state of the gripper to quickly open the gripper at a speed of 70
m1.set_gripper_state(0, 70)
time.sleep(3)
# Set the state of the gripper so that it quickly closes the gripper at a speed of 70
m1.set_gripper_state(1, 70)
time.sleep(3)


m1.send_coords([-189.8, -60.5, 304.7, -152.91, -10.65, 134.32],velocity,1) #Go up
time.sleep(5)
m1.send_coords([-239.1, -18.2, 266.5, -157.46, -11.09, 121.86],velocity,1) #Go down
time.sleep(5) #Recycle


# Set the state of the gripper to quickly open the gripper at a speed of 70
m1.set_gripper_state(1, 70)
time.sleep(3)
# Set the state of the gripper so that it quickly closes the gripper at a speed of 70
m1.set_gripper_state(0, 70)
time.sleep(3)

###### End of Recycle stage######

m1.send_coords([-189.8, -60.5, 304.7, -152.91, -10.65, 134.32],velocity,1) #Go up
time.sleep(5)
m1.send_coords([-254.3, -118.2, 206.5, -154.0, -0.95, 130.33],velocity,1) #Go down
time.sleep(5)

# Set the state of the gripper to quickly open the gripper at a speed of 70
m1.set_gripper_state(0, 70)
time.sleep(3)
# Set the state of the gripper so that it quickly closes the gripper at a speed of 70
m1.set_gripper_state(1, 70)
time.sleep(3)



m1.send_coords([-189.8, -60.5, 304.7, -152.91, -10.65, 134.32],velocity,1) #Go up
time.sleep(5)
m1.send_coords([-71.4, -209.6, 287.9, -152.96, -7.27, -172.14],velocity,1) #Go up
time.sleep(5)

# Set the state of the gripper to quickly open the gripper at a speed of 70
m1.set_gripper_state(1, 70)
time.sleep(3)
# Set the state of the gripper so that it quickly closes the gripper at a speed of 70
m1.set_gripper_state(0, 70)
time.sleep(3)



m1.send_angles([0, 20, 0, 0, 0, 0], velocity)


""" m1.send_coords([-205.3, -21.4, 287.8, -162.75, -12.97, 134.57],velocity,1) #Go down
time.sleep(5)
m1.send_coords([-203.5, 29.3, 294.7, -156.99, -10.26, 120.08],velocity,1) #Go down
time.sleep(5) """






# m1.send_coords([-202.6, -80.4, 296.8, -154.24, -20.87, 164.86],velocity,1) #Go NR
# time.sleep(5)
# m1.send_coords([-119.0, -180.0, 293.3, -152.55, -11.64, -177.06],velocity,1) #center
# time.sleep(5)
# m1.send_coords([-49.9, -225.4, 269.5, -157.22, 2.65, -159.49],velocity,1) #Go R
# time.sleep(5)



