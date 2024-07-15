<picture>
 <source media="(prefers-color-scheme: dark)" srcset="https://i.imgur.com/LBxDUjx.png">
 <source media="(prefers-color-scheme: light)" srcset="https://i.imgur.com/LBxDUjx.png">
 <img alt="YOUR-ALT-TEXT" src="https://i.imgur.com/LBxDUjx.png">
</picture>

# HAMMERSTEIN MK2

## Introduction
HammersteinMk2 is a mobile wheeled robot. The actual basis for the robot is, in itself, about 6 years old and has taken various guises. 
It started out as a result of my first entry into PiWars in 2017. I entered a team from a Primary School and this was the Robot that we entered. 
Since then he has entered PiWars a second time as a BumbleBee called DrumbleDrone”. This was a mixed Adult / Youth team entry.
Rather than sit and gather dust, I have decided to re-purpose him into HammerStein Mk2.
This document is not really meant as an in depth guide, more a story of what I have achieved so far and how I did it.
At the time of writing it is far from finished, so it is a work in progress.

## Hardware

### Chassis 
The chassis is a ThunderBorg chassis supplied by PiBorg. 
### Body 
The body (which is the original from PiWars 2017), is made from the base of an old Macbook. 
### MicroController
Started with a Pi 3 now latest Pi is a Raspberry Pi 4 (4GB)
### Camera
Front facing camera
### Speakers
2 x old PC speakers, powered by small eBay electronics kit amplifier
### Ancillaries
3D printed pan and tilt mount on top / front mountable grabber

## Robotic Elements
The aim of this robot is to have a Raspberry Pi based ‘Telepresence’ robot, incorporating vision, sound, voice recognition for audio commands, face recognition, motion detection, to act as a home security / alarm system. This robot will be autonomous however again, as with the original, it may have a remote control override
This will be a mobile robot that will hopefully be linked to Central AI (another similar non mobile project), to act as its eyes and ears on the ground. 
The project will be broken down into the following modules:
### Mobile Platform
The chassis, running gear and body.
### Camera
To enable the robot to see and to be able to pass what the robot sees CentralAI and to the user when in manual control mode
### Computer Vision
To enable the robot to make use of what it can see with the camera
### Audio
To give the robot a voice
### Sensors
To be able to navigate its environment
### Display
This robot will have a display so that it has a face that interacts with its surroundings, using pre recorded video clips

## Mobile Platform

As mentioned earlier, the chassis is a Monsterborg chassis from PiBorg. These chassis have 4x DC Motors in 4WD and designed for robot racing.
The chassis, running gear and body have been in use for a while now and the robot is a veteran of Pi Wars, first entering in 2017 I believe as BillyBot CCP2 and then again in 2021 as Drumbledrone. I have retained the original body, which is made from the power part of an aluminium MacBook.

Upon reassembling the body onto the chassis, after fitting the case and new DSI screen, I noticed that the battery pack for the audio unit is too close to the GPIO header, so I would need to make some modifications.  

To alleviate the issue, I ordered some Female - Male 90 degree GPIO headers. These are designed to fit onto the GPIO header and give new female GPIO headers at 90 degrees, this will prevent the existing Du Port connectors from fouling with the audio battery pack. However, when they arrived I identified that the dupont connectors are loose on them and fall off. 

I also need to lower the Raspberry Pi slightly to enable better access to the upper USB and Ethernet ports as they are partially shrouded by the cut out in the rear of the body. 

To achieve this and to fix the GPIO issue, I aim to use slightly shorter standoffs.

## Display 

For the display I purchased a Waveshare 4.3” DSI LCD Touch Screen. I found a 3D printable case on Thingyverse.
To mount the case on to Robot I designed a bracket and 3D printed a bracket.

## Software

Custom Programs
All programs developed for Hammerstein can be found in it’s GitHub Repository here:
https://github.com/JonnyAlpha/Hammerstein_Mk2

## The Operating System
On the Pi 3 the underlying OS was Raspbian Stretch, however since moving to a Pi4, the OS has been upgraded to Bookworm. Bookworm has introduced a lot of changes that have impacted on the previous programming on the original Hammerstein, lots of code no longer works because things have been depreciated.

Starting with a fresh image of Raspbian Bookworm 64 Bit on a new 32GB SD card following this guide:
https://raspberrytips.com/install-raspbian-raspberry-pi/

First job was to update and upgrade the OS using sudo apt update && sudo apt upgrade

### Virtual Environment
One of the key differences with OS Bookworm is that you cannot install third part packages using pip, this is a safety feature to preserve the OS. To install packages that are not available in apt / apt-get, you need to be in a virtual environment. At first this seems a pain, but it is a good move to ensure that all the changes are confined to a virtual environment, preserving the OS.
To install a Virtual Environment follow this tutorial:
https://learn.adafruit.com/python-virtual-environment-usage-on-raspberry-pi?view=all

I created a new virtual environment called “Hammerstein”.
After setting up the virtual environment, I had to amend the config file pyvenv.cfg to include site packages, this ensures that site packages are available from within the virtual environment.


### Video Playback
In earlier testing, to develop a visual front end for a robot, I found and was using omxplayer and OMXPlayer Wrapper, it allowed control of video playback and seamless switching between videos, which is exactly what I wanted for the visual front end of this robot. However, with the release of the latest Raspbian OS (bookworm), omxplayer and OMXPlayer Wrapper had been depreciated, so an alternative was needed :-( 

After some extensive searching for video playback within python, I found some programs here. 
https://github.com/iadjedj/lgp_rpi_video/blob/main/README.md

These use python-vlc. The first program, 01_basic_vlc.py was problematic testing on a Mac, as it will not display video, however seemed to work without a problem on a Pi, so would be further developed.

To use this program you need to Install python-vlc.

Python VLC will be used to play pre recorded video files that will changed dependent on the interactions with the robot. 

### Audio Playback
To playback audio files for sound effects I found this guide by the most amazing Jeff Geerling:
https://www.jeffgeerling.com/blog/2022/playing-sounds-python-on-raspberry-pi
It includes getting a USB Speaker connected and working, which would be useful. 

For playing some of the audio files I used PyGame:
`pip install pygame`

 
### Voice Commands
For voice commands I chose VOSK. I came across this whilst competeing in PiWars a few years ago. One of the competitors did a video of voice commands and the one they opted for was VOSK. It was simple and required no live Internet connection.

To set VOSK up I followed these videos:

**First Video**
https://www.youtube.com/watch?v=3Mga7_8bYpw

**Second Video**
https://www.youtube.com/watch?v=-0W_AxSD_t8

I then had some problems installing pyaudio, apparently port audio was missing.
install portaudio19-dev
install pyaudio
install pyttsx3

I also had to install espeak (I think).

Niel Stevenson on VOSK:
https://www.youtube.com/watch?v=LqFYmXaXBdQ

https://github.com/SaraEye/SaraKIT-Speech-Recognition-Vosk-Raspberry-Pi/blob/main/SpeechRecognition.py


### Computer Vision On The Mac Testing

Computer Vision for this robot will rely on OpenCV. To test on my Mac I had to install OpenVC. Without specifying the actual version I ran into errors but this worked flawlessly:

`pip3 install opencv-python==4.6.0.66`


To install OpenCV onto a raspberry Pi I found this up to date guide.

To test OpenCv I searched for a guide on Face Recognition in Python and found this simple guide:
https://www.datacamp.com/tutorial/face-detection-python-opencv

Running the code below, on a MacBook, opens the video camera and draws a green bonding box around any faces in the images.

`import cv2
face_classifier = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
video_capture = cv2.VideoCapture(0)
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40)) 
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces
while True:
    result, video_frame = video_capture.read() 
    if result is False:
        break
    faces = detect_bounding_box(video_frame)
    cv2.imshow("Face Detection", video_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
video_capture.release()
cv2.destroyAllWindows`

Now that I could detect the presence of a face in a video camera, for the purpose of this project, I needed to be able to confirm that the owner of the face was friend of foe :-) for this I needed to research further.
I found a simple (ish) tutorial here:

https://www.youtube.com/watch?v=pQvkoaevVMk

There is another more in depth tutorial here:
 
https://www.youtube.com/watch?v=pQvkoaevVMk

For the first tutorial you need to ensure that opencv and deepface are installed.

https://github.com/serengil/deepface

https://github.com/manish-9245/Facial-Emotion-Recognition-using-OpenCV-and-Deepface/blob/main/README.md

pip install deepface
pip install --no-deps deepface (to fix package version errors)

pip install pandas

As well as this, you needs the VGG-Face model weights file. 

https://github.com/serengil/deepface_models/releases/download/v1.0/vgg_face_weights.h5/

I had trouble on the Pi with numpy and cv2 
ImportError: numpy.core.multiarray failed to import

I followed advice on this thread:

https://numpy.org/devdocs/user/troubleshooting-importerror.html

I had to uninstall numpy and re-install using:
apt install python3-numpy

Again I had trouble on the Pi and had to install / upgrade pandas

pip install --upgrade pandas

Now when the face detection program is run it will open a video window and show a red NO MATCH or green MATCH if it recognises the face against the reference jpeg image.

python3 -m pip uninstall protobuf

When trying to reinstalling OpenCV to resolve some module errors, using this guide:

https://raspberrytips.com/install-opencv-on-raspberry-pi/

I noticed during the pip install of opencv the following lines:

`Requirement already satisfied: numpy>=1.19.3 in ./.local/lib/python3.9/site-packages (from opencv-python) (1.26.2)`

This may suggest that a newer version of numpy has not been installed as the requirement already satisfied with version 1.19.3 from opencv-python  version 1.26.2 

DeepFace
https://towardsdatascience.com/using-deepface-for-face-recognition-5f8d1e43f2a6

More Computer Vision On The Pi

Whilst developing the software for Hammerstein, I have been discussing successes and issues with a friend at a local Pi Jam. Fortunately he is an accomplished programmer, with a background in Computer Vision, he also discovered some very effective lightweight face recognition software. 

https://github.com/opencv/opencv_zoo/tree/main

He stripped down the Face Recognition and within a venv on a Pi4 I was able to run the program successfully.
 
Computer Vision Research - Trial and Error
All of the following has now been superseded, as we are now using a Pi4 running Raspbian Bookworm and Virtual Environments. It has been left for info.
 
Now to get this working on a Raspberry Pi I transferred my test code and tried to run it. It produced a ‘no module named cv2’ error. OpenCV was on this Pi, but installed for python2. I now wanted to run everything in Python3 so using this guide I installed OpenCV:

https://raspberrypi-guide.github.io/programming/install-opencv

To get the picamera working as long as it is setup in rasps-config you may need to install picamera array:

pip install “picamera[array]”

I could not work out how to incorporate the PiCamera lines of code into the programs that I had already used and in the end found that the line:

`cv2.VideoCapture(0)` 

Activates the picamera, what I need to do is research whether using the PiCamera commands helps to optimise the camera as with the existing code on the Pi it was very slow to respond.

Maybe setting lower resolutions, as described here:
https://raspberrypi.stackexchange.com/questions/110820/opencv-camera-resolution


`import cv2

cap = cv2.VideoCapture(0)

cap.set(3, 640)  # Set horizontal resolution
cap.set(4, 480)  # Set vertical resolution

_, img = cap.read()
cv2.imwrite("lower_res.jpeg", img)`

https://bobbyhadz.com/blog/python-no-module-named-pandas


Installing collected packages: keras
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
deepface 0.0.79 requires fire>=0.4.0, which is not installed.
deepface 0.0.79 requires gunicorn>=20.1.0, which is not installed.
deepface 0.0.79 requires mtcnn>=0.1.0, which is not installed.
deepface 0.0.79 requires retina-face>=0.0.1, which is not installed.
deepface 0.0.79 requires Flask>=1.1.2, but you have flask 1.0.2 which is incompatible.
deepface 0.0.79 requires opencv-python>=4.5.5.64, but you have opencv-python 4.5.3.56 which is incompatible.

https://raspberrypi.stackexchange.com/questions/107483/error-installing-tensorflow-cannot-find-libhdfs-so

Once I finally got it working the camera was inverted and needed to be rotated 180 clockwise. I tried to find how to do this in the setting to no avail, I then opted to use cv2.rotate

https://www.educative.io/answers/opencv-rotate-image

https://stackoverflow.com/questions/58910779/how-to-rotate-camera-recorded-video

However, when running the program it struggled to identify faces as they were upside down. To resolve this, luckily, I physically rotated the camera.

