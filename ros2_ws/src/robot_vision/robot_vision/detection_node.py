import rclpy
from rclpy.node  import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
import cv2
import time
import PIL
import json
#from torchvision.models.resnet import resnet50, ResNet50_Weights
#from torchvision.io import read_image
from PIL import Image as img_handle
#from torchvision import transforms as T
#import torch
import urllib
import os
from tutorial_interfaces.srv import VisionToRobot
from functools import partial
import time

import numpy as np
import argparse
import tensorflow as tf
import cv2

from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

# patch tf1 into `utils.ops`
utils_ops.tf = tf.compat.v1

# Patch the location of gfile
tf.gfile = tf.io.gfile

#Legacy code just for preliminary testing:
bridge = CvBridge ()
#print(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
print(os.path.dirname(__file__)+'/labelmap.pbtxt')
model_path = os.path.dirname(__file__)+'/inference_graph_3/saved_model'
label_path = os.path.dirname(__file__)+'/labelmap.pbxt'

dontcall = False


def load_model(model_path):
    model = tf.saved_model.load(model_path)
    return model


def run_inference_for_single_image(model, image):
    image = np.asarray(image)
    # The input needs to be a tensor, convert it using `tf.convert_to_tensor`.
    input_tensor = tf.convert_to_tensor(image)
    # The model expects a batch of images, so add an axis with `tf.newaxis`.
    input_tensor = input_tensor[tf.newaxis,...]
    
    # Run inference
    output_dict = model(input_tensor)

    # All outputs are batches tensors.
    # Convert to numpy arrays, and take index [0] to remove the batch dimension.
    # We're only interested in the first num_detections.
    num_detections = int(output_dict.pop('num_detections'))
    output_dict = {key: value[0, :num_detections].numpy()
                for key, value in output_dict.items()}
    output_dict['num_detections'] = num_detections

    # detection_classes should be ints.
    output_dict['detection_classes'] = output_dict['detection_classes'].astype(np.int64)

    # Handle models with masks:
    if 'detection_masks' in output_dict:
        # Reframe the the bbox mask to the image size.
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
                                    output_dict['detection_masks'], output_dict['detection_boxes'],
                                    image.shape[0], image.shape[1])      
        detection_masks_reframed = tf.cast(detection_masks_reframed > 0.5, tf.uint8)
        output_dict['detection_masks_reframed'] = detection_masks_reframed.numpy()
        
    
    
    return output_dict




def run_inference(model, category_index, cap):
    image_np = cap
    # Actual detection.
    output_dict = run_inference_for_single_image(model, image_np)
    # Visualization of the results of a detection.
    vis_util.visualize_boxes_and_labels_on_image_array(
        image_np,
        output_dict['detection_boxes'],
        output_dict['detection_classes'],
        output_dict['detection_scores'],
        category_index,
        instance_masks=output_dict.get('detection_masks_reframed', None),
        use_normalized_coordinates=True,
        line_thickness=8)
    cv2.imshow('object_detection', cv2.resize(image_np, (800, 600)))
    if cv2.waitKey(25) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
    
    
    if(output_dict['detection_scores'][0] > 0.85):
        print("Inside class run inference")
        return output_dict['detection_classes'][0]
    else:
        print("Inside blank run inference")
        return "blank"


detection_model = load_model(model_path)
category_index = label_map_util.create_category_index_from_labelmap(label_path, use_display_name=True)


class camera_detection(Node):
    def __init__(self):
        
        super().__init__("camera_subscriber") #Node name
        self.get_logger().info("camera_subscriber node started")
        self.camera_subscriber = self.create_subscription(Image,'/robotCyclops/image',self.displayImageCallback,0)
        
    def set_call_service(self,str):
        self.cli = self.create_client(VisionToRobot,"visionrobot_service")
        while not self.cli.wait_for_service(1.0):
            self.get_logger().warn("Waiting for service ....") 



        if(dontcall == False):
            request = VisionToRobot.Request()
            request.str = str
            future = self.cli.call_async(request)
            future.add_done_callback(partial(self.callback_call_service))
        else:
            request = VisionToRobot.Request()
            request.str = "donothing"
            future = self.cli.call_async(request)
            future.add_done_callback(partial(self.callback_call_service))

    def callback_call_service(self,future):
        try:
            response = future.result()
            if(response.str == 'recyclable'):
                dontcall = True
                print("Returning from the recyclable")
                time.sleep(1.0)
                dontcall  = False
            elif(response.str == 'nonrecyclable'):
                dontcall = True
                print("Returning from the nonrecyclable")
                time.sleep(1.0)
                dontcall  = False                
        except Exception as e:
            self.get_logger().error("Service call failed")

    def displayImageCallback(self,msg:Image):
            img_to_cv2 = bridge.imgmsg_to_cv2(msg,"passthrough")
            result = run_inference(detection_model, category_index, img_to_cv2)
            
            if result == 1:
                print('recyclable')
                
                self.set_call_service('recyclable')
                time.sleep(20.0)
               
                
            elif result == 2:
                print('nonrecyclable')
                
                self.set_call_service('nonrecyclable')
                time.sleep(20.0)
                
            else:
                print('Below detection threshold')



def main(args=None):
    rclpy.init(args=args)
    node = camera_detection()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()


# python .\detect_from_webcam.py -m ssd_mobilenet_v2_320x320_coco17_tpu-8\saved_model -l .\data\mscoco_label_map.pbtxt