
from datetime import datetime
import time
import requests
import os


# EXAMPLE camera url of https://mycity.com/trafficcameras/camera=22/capture
# url_front = "https://mycity.com/trafficcameras/camera="
# url_end = "/capture" 
# camera_ids = [22]

url_front = "" #portion of url before camera id
url_end = "" # portion url after the camera ID
camera_ids = [] # Camera id (part of url that changes to indicate camera)
img_type = "" # File extention used when saving image files

img_dir = "camera" # Directory where subdirectories for each camera will be stored
capture_interval = 10 # Interval between end of last capture and start of current capture



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




