# Traffic Cam Scraper
[![python](https://img.shields.io/badge/python-3-yellow.svg)](https://python.org)

- [Traffic Cam Scraper](#traffic-cam-scraper)
  - [Introduction](#introduction)
  - [Sample Timelapses](#sample-timelapses)
  - [Getting Started](#getting-started)
    - [To use just the basic camera scraper](#to-use-just-the-basic-camera-scraper)
    - [Eliminating broken frames (Ottawa)](#eliminating-broken-frames-ottawa)
    - [Generating gif or video](#generating-gif-or-video)


## Introduction
This script was developed in order to scrape images from multiple traffic camera feeds from one city/organization. 

The idea of this was conceived in order to capture time-lapses or events through traffic cameras that are readily available to the public in many cities. 

## Sample Timelapses
![New York City Sample](samples\nyc-usa1.gif)![Toronto Sample](samples\toronto-canada1.gif)\
![Calgary Sample](samples\calgary-canada1.gif)\


## Getting Started

### To use just the basic camera scraper
1. Download this repository to your computer, and ensure that you have the latest version of python 3 installed.
2. Open `camera_scraper.py`
3. Modify the following variables to suit your needs. Some examples can be [found here](example_configs.md).
   1. url_front
   2. url_end
   3. camera_ids
   4. img_type
   5. img_dir
   6. capture_interval
4. Run the script for as long as you like 
5. End the script when you are satisfied with how many captures you have.


### Eliminating broken frames (Ottawa)
1. Ensure that all prerequisite packages in `requirements.txt` are installed
2. Update the following values to match the ones from `camera_scraper.py`
   1. img_dir
   2. img_type
3. Run `ottawa_clean_set.py`
4. For each camera subdirectory verify the `reject` folder for validity


### Generating gif or video 

