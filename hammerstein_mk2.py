# Hammerstein Mk2 - a mobile robot
# To use this file, you will need to supply your own videos and audio files and amend the full paths / names within this code
# Before running install somne dependencies:
# pip install pygame
# pip install python-vlc
# pip install gpiozero - if using any gpio pins
# pip install vosk
# pip3 install pyaudio
# pip3 install pyttsx3

# Import the required libraries
import pygame # for playing audio files
import vlc # for playing videos
from time import sleep
import os # to run terminal commands
from gpiozero import MotionSensor
from vosk import Model, KaldiRecognizer
import pyaudio
import pyttsx3

# Setup the motion sensor
pir = MotionSensor(23)

# Initialise VLC player
instance = vlc.Instance()
player = instance.media_player_new()

# Setup voice recognition
model = Model(r"/home/pi/HammersteinMk2/vosk-model-small-en-us-0.15")
recognizer = KaldiRecognizer(model, 16000)

mic = pyaudio.PyAudio()

engine = pyttsx3.init()

listening = False

def get_command():
    listening = True
    stream = mic.open(format=pyaudio.paInt16, channels=1, rate=16000, input=True, frames_per_buffer=8192)
    while listening:
        stream.start_stream()
        try:
            data = stream.read(4096)
            if recognizer.AcceptWaveform(data):
                result = recognizer.Result()
                response = result[14:-3]
                listening = False
                stream.close()
                return response
        except OSError:
            pass


def startup():
    print("HAMMERSTEIN MKII \n")
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
    sound = pygame.mixer.Sound('/home/pi/HammersteinMk2/audio/mac_startup.wav')
    playing = sound.play()
    while playing.get_busy():
        pygame.time.delay(100)
    
def welcome():
    #Create media objects 
    media = instance.media_new('/home/pi/HammersteinMk2/videos/welcome.mp4')
    
    # Play video
    #player.toggle_fullscreen()
    play_video(player, media)

    
def play_video(player, media):
    # Play video

    player.set_media(media)
    player.play()
                
    while player.get_state() != vlc.State.Ended:
        sleep(5)

def wait_motion():
    media = instance.media_new('/home/pi/HammersteinMk2/videos/whos_there.mp4')

    while True:
        # Check for motion
        #if pir.motion_detected:
         #   play_video(player, media)
        #pir.when_motion = print("motion"), play_video(player, media)
        #pir.when_no_motion = print("still"), sleep(1)
        pir.wait_for_motion()
        play_video(player, media)
        break

def hello():
    media = instance.media_new('/home/pi/HammersteinMk2/videos/hello_bill.mp4')
    play_video(player, media)
    media = instance.media_new('/home/pi/HammersteinMk2/videos/what_would_you_like.mp4')
    play_video(player, media)

def normal_operation():
    hello()
    while True:
        print("Waiting for voice command...")
        command = get_command()
        if command == "":
            pass
        elif command == "hello":
            #engine.say("Hello to you too")
            #engine.runAndWait()
            media = instance.media_new('/home/pi/HammersteinMk2/videos/hello_bill.mp4')
            play_video(player, media)
        elif command == "say something":
            engine.say("something")
            engine.runAndWait()
        elif command == "what is your name":
            engine.say("Holly")
            engine.runAndWait()
        elif command == "end":
            media = instance.media_new('/home/pi/HasmmersteinMk2/videos/I_can_do_that.mp4')
            sleep(4)
            break
        else:
            #engine.say("Sorry I don't understand that yet")
            #engine.runAndWait()
            media = instance.media_new('/home/pi/HammersteinMk2/videos/I_cant_do_that.mp4')
            play_video(player, media)
            
def main():
    startup()
    welcome()
    wait_motion()
    normal_operation()
    
    
    

main()
