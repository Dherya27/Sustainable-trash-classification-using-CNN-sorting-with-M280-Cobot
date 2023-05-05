from pymycobot.mycobot import MyCobot
from pymycobot.genre import Angle
from pymycobot import PI_PORT, PI_BAUD  # When using the Raspberry Pi version of mycobot, you can refer to these two variables to initialize MyCobot
import time

#List for storing Joint Angles:
record_joint_angles = []

#List for storing End-Effector Co-ordinates:
record_endeffector_coordinates = []

# Initiate a MyCobot object
# Create object code here for windows version
mc = MyCobot("/dev/ttyACM0", 115200)

#By passing the angle parameter, let each joint of the robotic arm move to the position corresponding to [0, 0, 0, 0, 0, 0]
mc.send_angles([0, 0, 0, 0, 0, 0], 20)
record_joint_angles.append(mc.get_angles())
record_endeffector_coordinates.append(mc.get_coords())

# Set the waiting time to ensure that the robotic arm has reached the specified position
time.sleep(2.5)
record_joint_angles.append(mc.get_angles())
record_endeffector_coordinates.append(mc.get_coords())

# Move joint 1 to the 90 position
mc.send_angle(Angle.J1.value, 90, 20)
record_joint_angles.append(mc.get_angles())
record_endeffector_coordinates.append(mc.get_coords())
# Set the waiting time to ensure that the robotic arm has reached the specified position
time.sleep(2)
record_joint_angles.append(mc.get_angles())
record_endeffector_coordinates.append(mc.get_coords())

# The following code can make the robotic arm swing left and right
# set the number of loops
num = 1
while num > 0:

     # Move joint 2 to the 50 position
    mc.send_angle(Angle.J2.value, 50, 20)
    record_joint_angles.append(mc.get_angles())
    record_endeffector_coordinates.append(mc.get_coords())

    # Set the waiting time to ensure that the robotic arm has reached the specified position
    time.sleep(1.5)
    record_joint_angles.append(mc.get_angles())
    record_endeffector_coordinates.append(mc.get_coords())

    # Move joint 2 to the -50 position
    mc.send_angle(Angle.J2.value, -50, 20)
    record_joint_angles.append(mc.get_angles())
    record_endeffector_coordinates.append(mc.get_coords())

    # Set the waiting time to ensure that the robotic arm has reached the specified position
    time.sleep(1.5)
    record_joint_angles.append(mc.get_angles())
    record_endeffector_coordinates.append(mc.get_coords())

    num -= 1

#Make the robotic arm retract. You can manually swing the robotic arm, and then use the get_angles() function to get the coordinate sequence, 
# use this function to let the robotic arm reach the position you want.
mc.send_angles([88.68, -138.51, 155.65, -128.05, -9.93, -15.29], 20)
record_joint_angles.append(mc.get_angles())
record_endeffector_coordinates.append(mc.get_coords())

# Set the waiting time to ensure that the robotic arm has reached the specified position
time.sleep(10.5)
record_joint_angles.append(mc.get_angles())
record_endeffector_coordinates.append(mc.get_coords())


# Let the robotic arm relax, you can manually swing the robotic arm
mc.release_all_servos()

#Write the recorded values into lists:
# open file in write mode
with open(r'record_joint_angles.txt', 'w') as fp:
    for item in record_joint_angles:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')

# open file in write mode
with open(r'record_endeffector_coordinates.txt', 'w') as fp:
    for item in record_endeffector_coordinates:
        # write each item on a new line
        fp.write("%s\n" % item)
    print('Done')
