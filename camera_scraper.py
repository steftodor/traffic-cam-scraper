#----------------------------------------------------------------------------
# camera_scraper.py
# This script was developed in order to scrape images from multiple traffic camera feeds from one city/organization.
# This script is solely for pulling the latest camera feeds and placing them in folders
#
# Created By: 
#   Stefan Todorovic - github.com/steftodor
#
# version ='0.1'
#
# notes : none

from datetime import datetime
import time, requests, os


# EXAMPLE camera url of https://mycity.com/trafficcameras/camera=22/capture
# url_front = "https://mycity.com/trafficcameras/camera="
# url_end = "/capture" 
# camera_ids = [22]

url_front = "" #portion of url before camera id
url_end = "" # portion url after the camera ID
camera_ids = [] # Camera id (part of url that changes to indicate camera)
img_type = "" # File extention used when saving image files

url_front = "https://traffic.ottawa.ca/beta/camera?id="
url_end = ""
camera_ids = [38, 66, 188]
img_type = "jpeg"



img_dir = "camera" # Directory where subdirectories for each camera will be stored
capture_interval = 10 # Interval between end of last capture and start of current capture

capture_interval = 30 


def capture_all_cameras():
    currentTimeDate = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
    print(f"Capture at {currentTimeDate}")
    for camera in camera_ids:
        # Combines the URL
        url = f'{url_front}{camera}{url_end}'
        try:
            r = requests.get(url, allow_redirects=True)
            open(f'{img_dir}/{camera}/camera{camera}-{currentTimeDate}.{img_type}', 'wb').write(r.content)
            status = "success"
        except requests.ConnectionError:
            status = "ERROR (network)"
        except OSError:
            status = "ERROR (file)"
        except:
            status = "ERROR (other)"
        print(f"\t{camera}  \t\t {status}")


def configure_folders():
     for camera in camera_ids:
        path = f'{img_dir}/{camera}'
        pathExists = os.path.exists(path)
        if not pathExists:
            print(f"Creating path for camera {camera}")
            os.makedirs(path)
        else:
             print(f"Path for camera {camera} exists")


camera_ids.sort()
configure_folders()
while(True):
    capture_all_cameras()
    time.sleep(capture_interval)




