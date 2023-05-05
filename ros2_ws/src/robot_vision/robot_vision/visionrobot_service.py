from tutorial_interfaces.srv import VisionToRobot

import rclpy
from rclpy.node import Node
from pymycobot.mycobot import MyCobot
import time

delay = 5
velocity = 30
m1 = MyCobot("/dev/ttyACM0", 115200)
class visionrobot_service(Node):
    def __init__(self):
        super().__init__("visionrobot_service")
        self.get_logger().info("generic node active")
        # Initialize a MyCobot object
        # Create object code here for windows version
        m1 = self.mc = MyCobot("/dev/ttyACM0", 115200)

        #Initialize the stating point:
        self.mc.set_color(0,0,0) #red light on
        time.sleep(2)    #wait for 2 seconds

        self.mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
        time.sleep(delay)

        self.srv = self.create_service(VisionToRobot, 'visionrobot_service', self.visiontorobot_callback)       # CHANGE

    def visiontorobot_callback(self, request, response):
        if(request.str == 'recyclable'):
            self.mc.set_color(0,255,0)
            self.get_logger().info('Inside recyclable case \nstr: %s' % (request.str))  # CHANGE
            #time.sleep(5)
            self.mc.send_coords([-208.4, -61.9, 296.0, -150.49, 3.71, 105.5],velocity,1) #center
            time.sleep(5)
            self.mc.send_coords([-254.3, -118.2, 206.5, -154.0, -0.95, 130.33],velocity,1) #Go down
            time.sleep(5)



            # Set the state of the gripper to quickly open the gripper at a speed of 70
            self.mc.set_gripper_state(0, 70)
            time.sleep(1)
            # Set the state of the gripper so that it quickly closes the gripper at a speed of 70
            self.mc.set_gripper_state(1, 70)
            time.sleep(1)


            self.mc.send_coords([-189.8, -60.5, 304.7, -152.91, -10.65, 134.32],velocity,1) #Go up
            time.sleep(5)
            self.mc.send_coords([-239.1, -18.2, 266.5, -157.46, -11.09, 121.86],velocity,1) #Go down
            time.sleep(5) #Recycle


            # Set the state of the gripper to quickly open the gripper at a speed of 70
            self.mc.set_gripper_state(1, 70)
            time.sleep(1)
            # Set the state of the gripper so that it quickly closes the gripper at a speed of 70
            self.mc.set_gripper_state(0, 70)
            time.sleep(1)

            self.mc.send_coords([-189.8, -60.5, 304.7, -152.91, -10.65, 134.32],velocity,1) #Go up
            #time.sleep(5)

            ###### End of Recycle stage######
            
            # self.mc.send_coords([130.9, -167.3, 178.5, 158.42, -12.33, -153.54],velocity,1)
            # #self.mc.set_gripper_state(0, 70)
            # time.sleep(1)
            # self.mc.send_coords([-89.0, -228.3, 263.2, -160.12, 14.44, 133.19],velocity,1)
            # time.sleep(1)
            # self.mc.send_coords([112.1, -256.9, 198.2, -165.03, 10.97, 174.86],velocity,1)
            # time.sleep(1)
            # #self.mc.set_gripper_state(1, 70)
            # time.sleep(1)
            # self.mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
            # time.sleep(5)
            #time.sleep(3)
            #self.mc.set_color(255,0,0) #red light on
            #time.sleep(2)    #wait for 2 seconds

            #self.mc.send_angles([0, 20, 0, 0, 90, 0], velocity)
            # self.mc.send_coords([-142.8, -239.8, 204.7, -160.22, 5.46, 149.16],velocity,1)
            # time.sleep(delay)
            
            # self.mc.set_color(255,0,0) #red light on
            # time.sleep(2)    #wait for 2 seconds

            # #Cartesian control

            # #Approach: Location-2 directly:

            # self.mc.send_coords([160.3, 179.6, 272.9, -150.89, -6.13, -8.37],velocity,1)
            # time.sleep(delay)

            # #Back to start
            # self.mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
            # time.sleep(delay)
            
            
            response.str = request.str                                           
            return response 
        elif(request.str == 'nonrecyclable'):

            self.mc.set_color(255,0,0)
            self.mc.send_coords([-189.8, -60.5, 304.7, -152.91, -10.65, 134.32],velocity,1) #Go up
            time.sleep(5)
            self.mc.send_coords([-254.3, -118.2, 206.5, -154.0, -0.95, 130.33],velocity,1) #Go down
            time.sleep(5)

            # Set the state of the gripper to quickly open the gripper at a speed of 70
            self.mc.set_gripper_state(0, 70)
            time.sleep(1)
            # Set the state of the gripper so that it quickly closes the gripper at a speed of 70
            self.mc.set_gripper_state(1, 70)
            time.sleep(1)



            self.mc.send_coords([-189.8, -60.5, 304.7, -152.91, -10.65, 134.32],velocity,1) #Go up
            time.sleep(5)
            self.mc.send_coords([-71.4, -209.6, 287.9, -152.96, -7.27, -172.14],velocity,1) #Go up
            time.sleep(5)

            # Set the state of the gripper to quickly open the gripper at a speed of 70
            self.mc.set_gripper_state(1, 70)
            time.sleep(1)
            # Set the state of the gripper so that it quickly closes the gripper at a speed of 70
            self.mc.set_gripper_state(0, 70)
            time.sleep(1)

            self.mc.send_coords([-189.8, -60.5, 304.7, -152.91, -10.65, 134.32],velocity,1) #Go up
            time.sleep(5)



            
            # self.get_logger().info('Inside rremote control\nstr: %s' % (request.str))  # CHANGE
            # self.mc.set_gripper_state(1, 70)
            # time.sleep(1)
            # self.mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
            # time.sleep(5)
            # self.mc.set_gripper_state(0, 70)
            # time.sleep(1)            #time.sleep(3)
            # #self.mc.set_color(0,255,0) #green light on
            # #time.sleep(2)    #wait for 2 seconds
            
            # self.mc.send_angles([0, 20, 0, 0, 90, 0], velocity)
            # time.sleep(delay)
            
            # self.mc.set_color(0,0,255) #red light on
            # time.sleep(2)    #wait for 2 seconds

            # #Cartesian control

            # #Approach: Location-2 directly:

            # self.mc.send_coords([215.7, 68.5, 263.6, -155.42, -10.56, -58.3],velocity,1)
            # time.sleep(delay)

            # #Back to start
            # self.mc.send_angles([0, 20, 0, 0, 0, 0], velocity)
            # time.sleep(delay)

            # m1.send_coords([77.6, -189.8, -14.0, 13.93, -4.22, 4.04], velocity,1)
            # time.sleep(delay) 
            
            response.str = request.str                                            
            return response 
        else:
            self.get_logger().info('Invalid \nstr: %s' % (request.str))  # CHANGE
            response.str = request.str                                           
            return response 
            

"""     def visiontorobot_callback(self, request, response):
        if(request.str == "rule"):
            self.get_logger().info('Inside rule case \nstr: %s' % (request.str))  # CHANGE 
            response.str = "rule"
        elif(request.str == "remote control"):
            self.get_logger().info('Inside calculatorcase \nstr: %s' % (request.str))  # CHANGE 
            response.str = "remote control"                                               
        return response  """


def main(args=None):
    rclpy.init(args=args)       #Initialize ROS2 communications
    publisher = visionrobot_service()
    rclpy.spin(publisher)       #Keep running the node code repeatedly, till ctrl-C is pressed
    rclpy.shutdown()            #Shutdown the ROS2 communications


if __name__ == '__main__':
    main()