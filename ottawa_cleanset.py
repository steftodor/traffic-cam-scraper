# NOTE THIS IS VERY MUCH A WORK IN PROGRESS, HAS WORKED EVERY TIME I'VE TRIED IT SO FAR BUT IS NOWHERE NEAR POLISHED

import os
from PIL import Image
import pytesseract
import numpy as np
import shutil

img_dir = "camera" # Directory where subdirectories for each camera will be stored
img_type = "jpeg" # File extention without period
camera_folders = [ f.path for f in os.scandir(img_dir) if f.is_dir() ]

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
        images = os.listdir(camera)
        for img in images:
            if img_type in img:
                print(f"{camera}/{img}")
                current_image = np.array(Image.open(f"{camera}/{img}"))
                image_text = pytesseract.image_to_string(current_image)
                print(image_text)
                if(("Unavailable" in image_text) or ("Timed" in image_text)):
                    print("FILE HAS BEEN MOVED")
                    shutil.move(f"{camera}/{img}", f"{camera}/reject/{img}")
            else:
                print("NOT A VALID IMG FILE")

configure_reject_folders()
sort_images()

