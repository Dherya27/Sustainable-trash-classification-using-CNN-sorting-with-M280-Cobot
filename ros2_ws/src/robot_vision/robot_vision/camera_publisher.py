import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import time


bridge = CvBridge ()

class camera_publisher(Node):
    def __init__(self):
        super().__init__("camera_publisher") #Node name
        self.get_logger().info("camera_publisher active")

        #Start video Capture
        #cap = cv2.VideoCapture(0)
        cap = cv2.VideoCapture('http://192.168.50.14:4747/video')
        self.get_logger().info("Start VideoCapture")
        self.camera_publisher = self.create_publisher(Image,'/robotCyclops/image',0)


        while(cap.isOpened()):
             

             ret,frame = cap.read() #read the camera input
             
             cv2.imshow('Frame-window',frame) #render the camera output in a window

            # convert the cv2 image to sensor_msgs Image type using CV Bridge function cv2_to_imgmsg
             
             img = bridge.cv2_to_imgmsg(frame, encoding="passthrough")
             
             self.camera_publisher.publish(img)
            
   
             if cv2.waitKey(1) & 0xFF == ord('q') :   #Use this to break out
                 break

        #Release the Device
        cap.release()
        self.get_logger().info("VideoCapture is closed")

        #Close all windows
        cv2.destroyAllWindows()


def main(args=None):
    rclpy.init(args=args) #start ROS2 communication
    node = camera_publisher()
    rclpy.spin(node)
    rclpy.shutdown() #stop ROS2 communcation

if __name__ == '__main__':
    main()