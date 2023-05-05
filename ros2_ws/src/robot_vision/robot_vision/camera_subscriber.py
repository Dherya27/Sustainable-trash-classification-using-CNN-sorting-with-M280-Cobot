import rclpy
from rclpy.node  import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2

bridge = CvBridge ()

class camera_subscriber(Node):
    def __init__(self):
        super().__init__("camera_subscriber") #Node name
        self.get_logger().info("camera_subscriber node started")
        self.camera_subscriber = self.create_subscription(Image,'/robotCyclops/image',self.displayImageCallback,0)

    def displayImageCallback(self,msg:Image):
        img_to_cv2 = bridge.imgmsg_to_cv2(msg,"passthrough")
        cv2.imshow('something',img_to_cv2) #render the camera output in a window
        cv2.waitKey(1)





def main(args=None):
    rclpy.init(args=args)
    node = camera_subscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main ()