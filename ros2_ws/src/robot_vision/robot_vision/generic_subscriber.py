#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class generic_subscriber(Node):
    def __init__(self):
        super().__init__("generic_subscriber") #Node name
        self.create_subscription(Twist,"/turtle1/cmd_vel",self.subscribeMessageDisplay,10)


    def subscribeMessageDisplay(self,msg:Twist):
        print("Linear value:(x,y,z)"+str(msg.linear.x)+str(msg.linear.y)+str(msg.linear.z))
        print("Angulat value:(x,y,z)"+str(msg.angular.x)+str(msg.angular.y)+str(msg.angular.z))
        

def main(args=None):
    rclpy.init(args=args) #Start ROS2 communication
    node = generic_subscriber()
    rclpy.spin(node)
    rclpy.shutdown()    #Shutdown ROS2 communication