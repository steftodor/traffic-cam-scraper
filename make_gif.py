#----------------------------------------------------------------------------
# ottawa_cleanset.py
# This script was developed to combine images for each camera subfolder into a gif.
#
# Created By: 
#   Stefan Todorovic - github.com/steftodor
#
# version ='0.1'
#
# notes:    THIS IS VERY MUCH A WORK IN PROGRESS, nowhere near polished and could be very buggy
#           requirements.txt must be installed   

from email.mime import image
import imageio
import os

img_dir = "camera" # Directory where subdirectories for each camera will be stored
img_type = "jpeg" # File extention without period






def run_camera(camera_dir):
    print(camera_dir)
    images_list = os.listdir(camera_dir)
    images_list.sort()
    images = []
    for img in images_list:
        if img.endswith(img_type):
            try:
                images.append(imageio.imread(camera_dir+ "/"+img))
                status = "IMG ADDED"
            except:
               status = "Something went wrong"
        else:
            status = "NOT A VALID IMG FILE"
        print(f"\t{img}\t\t\t\t\t{status}")
    if len(images) > 0:
        print(f"\tBuilding file for {camera_dir}")
        imageio.mimsave(camera_dir+ "/"+'movie.gif', images)
    else:
        print(f"\tThere are zero valid images in {camera_dir}")
    



def run_folder():
    for camera in camera_folders:
        print(f"current folder: {camera}")
        run_camera(camera)


camera_folders = [ f.path for f in os.scandir(img_dir) if f.is_dir() ]
camera_folders.sort()
run_folder()
