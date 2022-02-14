#----------------------------------------------------------------------------
# ottawa_cleanset.py
# This script was developed to remove the "Timeout" or "Camera Unavailable" frames that often appear in these scrapes.
# 
#
# Created By: 
#   Stefan Todorovic - github.com/steftodor
#
# version ='0.1'
#
# notes:    THIS IS VERY MUCH A WORK IN PROGRESS, nowhere near polished and could be very buggy
#           requirements.txt must be installed   

import os
from PIL import Image
import pytesseract
import numpy as np
import shutil

img_dir = "camera" # Directory where subdirectories for each camera will be stored
img_type = "jpeg" # File extention without period



def configure_reject_folders():
    for camera in camera_folders:
        pathExists = os.path.exists(f"{camera}/reject")
        if not pathExists:
            print(f"Creating path for {camera}")
            os.makedirs(f"{camera}/reject")
        else:
             print(f"Path for {camera} exists")


def sort_images():
    for camera in camera_folders:
        print(camera)
        images = os.listdir(camera)
        for img in images:
            if img.endswith(img_type):
                current_image = np.array(Image.open(f"{camera}/{img}"))
                image_text = pytesseract.image_to_string(current_image)
                if(("Unavailable" in image_text) or ("Timed" in image_text)):
                    status = "Filed was rejected"
                    shutil.move(f"{camera}/{img}", f"{camera}/reject/{img}")
                else:
                    status = "Not rejected"
            else:
                status = "NOT A VALID IMG FILE"
            print(f"\t{img}\t\t\t\t\t{status}")


camera_folders = [ f.path for f in os.scandir(img_dir) if f.is_dir() ]
configure_reject_folders()
sort_images()

