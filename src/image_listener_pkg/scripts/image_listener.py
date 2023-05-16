import numpy as np
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2

palette = np.array([
    [0, 0, 0],      # Class 0: Black
    [255, 0, 0],    # Class 1: Red
    [0, 255, 0],    # Class 2: Green
    [0, 0, 255],    # Class 3: Blue
    [255, 255, 0],  # Class 4: Yellow
    [255, 0, 255],  # Class 5: Magenta
    [0, 255, 255],  # Class 6: Cyan
    [128, 0, 0],    # Class 7: Dark Red
    [0, 128, 0],    # Class 8: Dark Green
    [0, 0, 128],    # Class 9: Dark Blue
    [128, 128, 128] # Class 10: Gray
], dtype=np.uint8)

def image_callback(msg):
    # Convert the image message to a numpy array
    img_arr = np.frombuffer(msg.data, dtype=np.uint8).reshape(msg.height, msg.width, 3)

    # Convert the 3-channel image to a single-channel image by taking the mean along the channel axis
    img = np.mean(img_arr, axis=2).astype(np.uint8)

    # Map the semantic labels to the color palette
    color_img = palette[img]

    # Display the color image
    cv2.imshow("Image window", color_img)
    cv2.waitKey(3)


rospy.init_node('image_listener')
rospy.Subscriber('/airsim/seg', Image, image_callback)
rospy.spin()
