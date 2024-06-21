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

## Hardware

**Chassis** - The chassis is a ThunderBorg chassis supplied by PiBorg. 
**Body** - The body (which is the original from PiWars 2017), is made from the base of an old Macbook. 
**MicroController** - Raspberry Pi 4 (4GB)
**Camera** - Front facing camera
**Speakers** - 2 x old PC speakers, powered by small eBay electronics kit amplifier
**Ancillaries** - 3D printed pan and tilt mount on top / front mountable grabber

## Robotic Elements
The aim of this robot is to have a Raspberry Pi based ‘Telepresence’ robot, incorporating vision, sound, voice recognition for audio commands, face recognition, motion detection, to act as a home security / alarm system. This robot will be autonomous however again, as with the original, it may have a remote control override
This will be a mobile robot that will hopefully be linked to Central AI (another similar non mobile project), to act as its eyes and ears on the ground. 
The project will be broken down into the following modules:
**Mobile Platform** - The chassis, running gear and body.
**Camera** - To enable the robot to see and to be able to pass what the robot sees CentralAI and to the user when in manual control mode
**Computer Vision** - To enable the robot to make use of what it can see with the camera
**Audio** - To give the robot a voice
**Sensors** - To be able to navigate its environment
**Display** - This robot will have a display so that it has a face that interacts with its surroundings, using pre recorded video clips

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
All programs developed for Hammerstein can be found in it’s GitHub Repository here.
Operating System
Since moving to a Pi4, the OS has been upgraded to Bookworm. Bookworm has introduced a lot of changes that have impacted on the previous programming on the original Hammerstein.

Staring with a fresh image of Raspbian Bookworm 64 Bit on a new 32GB SD card following this guide.

First job was to update and upgrade the OS using sudo apt update && sudo apt upgrade

### Virtual Environment
One of the key differences with OS Bookworm is that you cannot install third part packages using pip, this is to preserve the OS. To install packages that are not available in apt / apt-get, you need to be in a virtual environment. At first this seems a pain, but it is a good move to ensure that all the changes are confined to a virtual environment, preserving the OS.
To install a Virtual Environment follow this tutorial.
I created a new virtual environment called “Hammerstein”.
After setting up the virtual environment, I had to amend the config file pyvenv.cfg to include site packages, this ensures that site packages are available from within the virtual environment.


### Video Playback
In earlier testing, to develop a visual front end for a robot, omxplayer was the tool of choice, however, with the release of the latest Raspbian OS (bookworm), omxplayer had been depreciated, so an alternative was needed. 

After some extensive searching, for video playback within python, I found some programs here. These use python-vlc. The first program, 01_basic_vlc.py was problematic testing on a Mac, as it will not display video, however seemed to work without a problem on a Pi, so would be further developed.

To use this program you need to Install python-vlc.

Python VLC will be used to play pre recorded video files that will changed dependent on the interactions with the robot. 

Audio Playback
Occasionally we may need to playback audio files for sound effects, to help I found this guide by the most amazing Jeff Geerling. It includes getting a USB Speaker connected and working, which would be useful. 

For play some of the audio files I used PyGame:
pip install pygame

 
### Voice Commands
For voice commands we will be using VOSK
To set VOSK up I followed these videos:


First Video

Second Video

I then had some problems installing pyaudio, apparently port audio was missing.
install portaudio19-dev
install pyaudio
install pyttsx3

Also had t install espeak (I think).

