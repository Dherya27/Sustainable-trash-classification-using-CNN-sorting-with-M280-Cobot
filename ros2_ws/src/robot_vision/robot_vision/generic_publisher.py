#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class generic_publisher(Node):
    def __init__(self):
        super().__init__("generic_node")
        self.get_logger().info("generic node active")
        self.cmd_vel_pub = self.create_publisher(Twist,"/turtle1/cmd_vel",10)
        self.create_timer(1.0,self.timer_callback)

    def timer_callback(self):
        self.get_logger().info("Node message: Hello")
        message = Twist()
        message.linear.x = 2.0
        message.angular.z = 2.0
        self.cmd_vel_pub.publish(message)

def main(args=None):
    rclpy.init(args=args)       #Initialize ROS2 communications
    publisher = generic_publisher()
    rclpy.spin(publisher)       #Keep running the node code repeatedly, till ctrl-C is pressed
    publisher.destroy_node()
    rclpy.shutdown()            #Shutdown the ROS2 communications


if __name__ == '__main__':
    main()