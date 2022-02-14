# Sample Configurations for Cities
- [Sample Configurations for Cities](#sample-configurations-for-cities)
  - [Ottawa, Canada](#ottawa-canada)
    - [Configuration](#configuration)
    - [Specifications](#specifications)
    - [Sample](#sample)
    - [Note](#note)
  - [Toronto, Canada](#toronto-canada)
    - [Configuration](#configuration-1)
    - [Specifications](#specifications-1)
    - [Sample](#sample-1)
    - [Note](#note-1)
  - [Calgary, Canada](#calgary-canada)
    - [Configuration](#configuration-2)
    - [Specifications](#specifications-2)
    - [Sample](#sample-2)
    - [Note](#note-2)
  - [New York City, United States](#new-york-city-united-states)
    - [Configuration](#configuration-3)
    - [Specifications](#specifications-3)
    - [Sample](#sample-3)
    - [Note](#note-3)
  - [Belgrade, Serbia](#belgrade-serbia)
    - [Configuration](#configuration-4)
    - [Specifications](#specifications-4)
    - [Sample](#sample-4)
    - [Note](#note-4)



## Ottawa, Canada
### Configuration 
```
url_front = "https://traffic.ottawa.ca/beta/camera?id=c"
url_end = ""
camera_ids = [87, 33, 48, 95]
img_type = "jpeg"
capture_interval = 30 
```
### Specifications
 * Resolution: Varied, but low.
 * Refresh Rate: Varied, Generally under 30 seconds
 * Default Image type: jpeg
 * Other Stream options available: n/a
 * PTZ: Some (May occasionally move)
 * Source URL: [City of Ottawa](https://traffic.ottawa.ca/map/)
### Sample
![Ottawa Sample](samples\ottawa-canada1.gif)
### Note
 Known issue, sometime they will just randomly go offline. The image set collected afterwards will need to be cleaned before it can be used for a timelapse to avoid random flashing. Use `ottawa_cleanset.py` to remove most of these broken frames.




## Toronto, Canada
### Configuration 
```
url_front = "https://www.toronto.ca/data/transportation/roadrestrictions/CameraImages/loc"
url_end = ".jpg"
camera_ids = [9116, 9104, 8048, 8049, 8061, 8063, 8042]
img_type = "jpg"
capture_interval = 300 
```
### Specifications
 * Resolution: 400x225
 * Refresh Rate: Varied, Generally around 5 minutes 
 * Default Image type: jpg
 * Other Stream options available: n/a
 * PTZ: Unknown
 * Source URL: [City of Toronto](https://gtaupdate.com/traffic/) *This is a third party site that allows cameras to be found easier*
### Sample
![Toronto Sample](samples\toronto-canada1.gif)
### Note
n/a

## Calgary, Canada
### Configuration 
```
url_front = "https://trafficcam.calgary.ca/loc"
url_end = ".jpg"
camera_ids = [143, 71, 122, 5, 8]
img_type = "jpg"
capture_interval = 60 
```
### Specifications
 * Resolution: 840x630
 * Refresh Rate: Around 1 minute
 * Default Image type: jpg
 * Other Stream options available: n/a
 * PTZ: Unknown
 * Source URL: [City of Calgary](https://trafficcam.calgary.ca)
### Sample
![Calgary Sample](samples\calgary-canada1.gif)
### Note
n/a


## New York City, United States
### Configuration 
```
url_front = "https://511ny.org/map/Cctv/"
url_end = ""
camera_ids = ['4616685--17', '4616502--17', '4616501--17']
img_type = "jpeg"
capture_interval = 30 
```
### Specifications
 * Resolution: 240x352
 * Refresh Rate: less than 30 seconds
 * Default Image type: jpeg
 * Other Stream options available: n/a
 * PTZ: Unknown
 * Source URL: [511 ny](https://511ny.org/map/)
### Sample
![New York City Sample](samples\nyc-usa1.gif)
### Note
n/a


## Belgrade, Serbia
### Configuration 
```
url_front = "https://stream.uzivobeograd.rs/live/cam_"
url_end = ".jpg"
camera_ids = [1,2,3]
img_type = "jpg"
capture_interval = 10
```
### Specifications
 * Resolution: 576x704
 * Refresh Rate: 5 - 15 seconds 
 * Default Image type: jpg
 * Other Stream options available: Yes, available on their website. (Haven't looked into these)
 * PTZ: Some (Some Can often change positions)
 * Source URL: [Naxi Radio](https://www.naxi.rs/kamere)
### Sample
![Beograd Sample](samples\beograd-serbia1.gif)
### Note
n/a