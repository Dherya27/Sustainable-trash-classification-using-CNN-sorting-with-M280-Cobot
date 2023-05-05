import matplotlib.pyplot as plt


# empty list to read list from a file
record_endeffector_coordinates = []
record_joint_angles = []

#End effector X,Y,Z values
endeffector_x = [68.7,185.3,176.6,134.5,123.8,61.4,60.6,66.9,67.2,73.1]
endeffector_y = [-55.2,-65.6,-66.1,134.2,144.1,-74.9,-95.9,145.0,162.9,112.2]
endeffector_z = [-52.2,327.0,336.5,332.0,332.3,393.8,387.4,359.5,346.4,102.4]

#Endeffector Roll , Pitch , Yaw
endeffector_roll = [62.66,-138.16,-134.55,-137.19,-137.01,77.43,-72.6,-126.38,-131.48,171.58]
endeffector_pitch = [0.71,-0.96,-0.92,-0.95,-0.95,-0.02,0.06,-0.83,-0.89,-7.64]
endeffector_yaw = [-81.18,-90.94,-91.18,25.83,-21.44,-3.28,3.28,-1.74,-1.67,15.57]

#joint angles J1,J2,J3,J4,J5,J6
joint_1 = [-0.26,-0.61,63.8,87.8,88.94,88.94]
joint_2 = [-24.78,-22.85,-21.79,32.95,-13.09,-121.72]
joint_3 = [-10.98,10.28,-10.89,-9.05,-10.28,153.28]
joint_4 = [-13.79,-12.91,-14.5,-12.04,-12.39,-127.52]
joint_5 = [-1.05,-1.05,-1.05,-1.05,-1.05,-9.66]
joint_6 = [-0.26,-0.26,0.26,-0.26,-0.26,15.55]

#End effector X,Y,Z
plt.plot(endeffector_x)
plt.title('End Effector X position')
plt.xlabel('Sampling value')
plt.ylabel('End Effector X Co-ordinate')
plt.show()

plt.plot(endeffector_y)
plt.title('End Effector Y position')
plt.xlabel('Sampling value')
plt.ylabel('End Effector Y Co-ordinate')
plt.show()

plt.plot(endeffector_z)
plt.title('End Effector Z position')
plt.xlabel('Sampling value')
plt.ylabel('End Effector Z Co-ordinate')
plt.show()

#End Effector Roll, Pitch, Yaw
plt.plot(endeffector_roll)
plt.title('End Effector Roll position')
plt.xlabel('Sampling value')
plt.ylabel('End Effector Roll')
plt.show()

plt.plot(endeffector_pitch)
plt.title('End Effector Pitch position')
plt.xlabel('Sampling value')
plt.ylabel('End Effector Pitch')
plt.show()

plt.plot(endeffector_yaw)
plt.title('End Effector Yaw position')
plt.xlabel('Sampling value')
plt.ylabel('End Effector Yaw')
plt.show()

#Joint angles:
fig, axs = plt.subplots(3, 2)
axs[0, 0].plot(joint_1)
axs[0, 0].set_title('Joint-1 angle')
axs[0, 0].set_ylabel('Joint1 angle')

axs[0, 1].plot(joint_2, 'tab:orange')
axs[0, 1].set_title('Joint-2 angle')
axs[0, 1].set_ylabel('Joint2 angle')

axs[1, 0].plot(joint_3, 'tab:green')
axs[1, 0].set_title('Joint-3 angle')
axs[1, 0].set_ylabel('Joint3 angle')

axs[1, 1].plot(joint_4,'tab:red')
axs[1, 1].set_title('Joint-4 angle')
axs[1, 1].set_ylabel('Joint4 angle')

axs[2, 0].plot(joint_5, 'tab:orange')
axs[2, 0].set_title('Joint-5 angle')
axs[2, 0].set_ylabel('Joint5 angle')

axs[2, 1].plot(joint_6, 'tab:green')
axs[2, 1].set_title('Joint-6 angle')
axs[2, 1].set_ylabel('Joint6 angle')

fig.suptitle('M280 Joint Angles over tested Trajectory')
fig.subplots_adjust(top=0.88)
fig.tight_layout()
plt.show()

# open file and read the content in a list
#with open(r'record_endeffector_coordinates.txt', 'r') as fp:
#    for line in fp:
#        # remove linebreak from a current name
#        # linebreak is the last character of each line
#        x = line[:-1]

#        # add current item to the list
#        record_endeffector_coordinates.append(x)

# display list
#print(record_endeffector_coordinates)

# open file and read the content in a list
#with open(r'record_joint_angles.txt', 'r') as fp:
#    for line in fp:
        # remove linebreak from a current name
        # linebreak is the last character of each line
#        x = line[:-1]

        # add current item to the list
#        record_joint_angles.append(x)

# display list
#print(record_joint_angles)

#Shift values manually in for plotting

