import rclpy
from rclpy.node  import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import time
import PIL
import json
from torchvision.models.resnet import resnet50, ResNet50_Weights
from torchvision.io import read_image
from PIL import Image as img_handle
from torchvision import transforms as T
import torch
import urllib
import os
from tutorial_interfaces.srv import VisionToRobot
from functools import partial
import time


bridge = CvBridge ()

#Change to the labels path
print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
label_path = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))+'/labels/resnet50_labels.txt'

#Load the resnet 50 imagenet 1000 labels
labels = [] #Define an empty list

with open(label_path,'r') as filehandle:
    for line in filehandle:
        remove_linebreak_item = line[:-1]
        #print(remove_linebreak_item)
        labels.append(remove_linebreak_item)


# Load the resnet 50 model and the weights here
weights = ResNet50_Weights.DEFAULT
transforms = weights.transforms()
model = resnet50(weights=weights,progress=False)
model = model.eval ()

class camera_subscriber(Node):
    def __init__(self):
        self.dontcall = False
        super().__init__("camera_subscriberResnet50") #Node name
        self.get_logger().info("camera_subscriberResnet50 node started")
        self.camera_subscriber = self.create_subscription(Image,'/robotCyclops/image',self.displayImageCallback,0)

    def set_call_service(self,str):
        self.cli = self.create_client(VisionToRobot,"visionrobot_service")
        while not self.cli.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service ....") 

        request = VisionToRobot.Request()
        request.str = str

        if(self.dontcall == False):
            future = self.cli.call_async(request)
            future.add_done_callback(partial(self.callback_call_service))

    def callback_call_service(self,future):
        try:
            response = future.result()
            if(response.str == 'blue_brick'):
                self.dontcall = True
                time.sleep(4.0)
                self.dontcall = False
                
            
        except Exception as e:
            self.get_logger().error("Service call failed")



    def displayImageCallback(self,msg:Image):
        img_to_cv2 = bridge.imgmsg_to_cv2(msg,"passthrough")


        #put the resent code in here:

        d = img_to_cv2
        color_converted = cv2.cvtColor(d,cv2.COLOR_BGR2RGB)

        pil_image = img_handle.fromarray(color_converted)

        preprocess = T.Compose([
            T.Resize(256),
            T.CenterCrop(224),
            T.ToTensor(),
            T.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225])
        ])
    
        # Transform the image to the input format
        img_dog_processed = preprocess (pil_image)
        batch_img_dog_tensor = torch.unsqueeze(img_dog_processed, 0)
    
        pred_output = model(batch_img_dog_tensor)

        top5_labels = []



        _, indices = torch.sort(pred_output, descending=True)
        for idx in indices[0][:1]:
            temp_idx = str(idx.numpy())

            top5_labels.append(labels[idx.numpy()])
        
        cv2.putText(img_to_cv2,top5_labels[0],(100,100),0,1,(255,0,0),3)
        print(top5_labels)
        self.set_call_service(str(top5_labels[0]))
        cv2.imshow('something',img_to_cv2) #render the camera output in a window
        cv2.waitKey(1)
       




def main(args=None):
    rclpy.init(args=args)
    node = camera_subscriber()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main ()