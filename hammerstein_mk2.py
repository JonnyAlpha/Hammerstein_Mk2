# Hammerstein Mk2 - a mobile robot

# Import the required libraries
import pygame # for playing audio files
import vlc # for playing videos
import cv2
from time import sleep
import os # to run terminal commands
import sys
import keyboard # only for testing 
from threading import Thread

def startup():
    print("Hammerstein MkII \n")
    sleep(0.5)
    print("Starting up. \n")
    sleep(0.5)
    os.system('clear')
    print("Starting up.. \n")
    sleep(0.5)
    os.system('clear')
    print("Starting up... \n")
    sleep(0.5)
    os.system('clear')
    print("Starting up.... \n")
    sleep(0.5)
    os.system('clear')
    print("System ready")

    pygame.mixer.init()
    sound = pygame.mixer.Sound('/Users/BillHarvey/Documents/Electronics_and_Robotics/Hammerstein_Mk2/audio/mac_startup.wav')
    playing = sound.play()
    while playing.get_busy():
        pygame.time.delay(100)
    
    

def play_video(player, media):
    # Play video

    player.set_media(media)
    player.play()
                
    while player.get_state() != vlc.State.Ended:
        sleep(1)

def check_motion():

    if keyboard.read_key() == "m": # waits for a keyboard press, if its 'm' motion is detected   
        motion_detected = True
        print("motion detected!")

    else: # any key other than 'm' has been pressed

        motion_detected = False

    return motion_detected

def holly_still():
    # display the lobby image
    img = cv2.imread("Holly.jpeg", cv2.IMREAD_ANYCOLOR)
    
    cv2.imshow("Holly", img)
    sleep(2)
    cv2.waitKey(0) #wait for ESC key
    #sys.exit()

def welcome():
    # Initialise VLC player
    instance = vlc.Instance()
    player = instance.media_player_new()

    #Create media objects 
    media = instance.media_new('/Users/BillHarvey/Documents/Electronics_and_Robotics/Hammerstein_Mk2/videos/welcome.mp4')
    
    # Play video
    play_video(player, media)
    print("Entering wait mode")
    media1 = instance.media_new('/Users/BillHarvey/Documents/Electronics_and_Robotics/Hammerstein_Mk2/videos/whos_there.mp4')
    media2 = instance.media_new('/Users/BillHarvey/Documents/Electronics_and_Robotics/Hammerstein_Mk2/videos/hello_bill.mp4')
    while True:  
        motion_detected = check_motion()  
        if motion_detected == True:
            play_video(player, media1)
        else:
            #Thread(target = face_detect).start()
            #Thread(target = vid_play).start()
            #os.system("python3 demo_minimal.py")
            #play_video(player, media2)
            #sleep(1)
            #break
            #play_video(player, media)

def face_detect():
    os.system("python3 demo_minimal.py")
def vid_play():
    play_video(player, media2)
    
def main():
    startup()
    holly_still()
    welcome()

main()

cv2.destroyAllWindows() 

