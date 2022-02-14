# Traffic Cam Scraper
[![python](https://img.shields.io/badge/python-3.9-yellow.svg)](https://python.org)

## Introduction
This script was developed in order to scrape images from multiple traffic camera feeds from one city/organization. 

The idea of this was conceived in order to capture time-lapses or events through traffic cameras that are readily available to the public in many cities. 

## Sample Timelapses
![Ottawa Sample](samples\ottawa-canada1.gif)
![Toronto Sample](samples\toronto-canada1.gif)
![New York City Sample](samples\nyc-usa1.gif)
![Beograd Sample](samples\beograd-serbia1.gif)

## Getting Started



## Workflow of Script

### Scraping workflow
1. Check that all required folders are created
2. Download latest images from all selected cameras
3. Wait for the specified amount of time
4. Go to step 2
   
### Image Set Cleaning Workflow (Currently Ottawa Only)
1. Go through each camera folder
2. Using OCR locate all images that state "Time out" or "Camera unavailable"
3. Move images that contain these messages to a rejected subfolder for manual review 
   
### Convert to gif or video file Workflow
1. Go through each camera folder
2. Produce file with format of camera_id.gif or camera_id.mp4 at the resolution of the source files