#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from gpiozero import MotionSensor, LEDBoard
from signal import pause
import time
from time import sleep
import os
import os.path as osp
import shutil
import pygame
# import pibooth
import random
pygame.init()


__version__ = "1.0.0"


pir = MotionSensor("BOARD32")
led = LEDBoard("BOARD23")

delay = 6 # set number of seconds delay with no motion before Reset

def sounddelay(time):
    # set number of seconds before sound starts after motion detected
    # THIS WILL BE ADDED AS EXTRA-TIME TO THE LIGHTOFF TIMER
    time.sleep(2)
    
def lightoff(time):
    # set number of seconds before light turn off
    time.sleep(10)


while True:
    #wait for pir to trigger.
    print("Waiting for motion\n")
    pir.wait_for_motion()
    time.sleep (0.5)
    print("There are motion\nTurn on light and play Sound with delay\n")
    pir.when_motion
    led.on()
    sounddelay(time)
    
    # Play random sounds 
    _songs = ('/home/pi/Documents/mp3/K.wav','/home/pi/Documents/mp3/B.wav')
    _currently_playing_song = None
    def play_a_different_song():
        global _currently_playing_song, _songs
    next_song = random.choice(_songs)
    while next_song == _currently_playing_song:
        next_song = random.choice(_songs)
    _currently_playing_song = next_song
    pygame.mixer.music.load(next_song)
    pygame.mixer.music.play(0)

    # Timer turn light off
    lightoff(time)

    count = 0
    print ("Turn light off and start countdown\n")
    led.off()

    #start count down
    print ("count down started\n")
    while count < delay:
        count = count + 1
        
    # here if the input goes high again we reset the counter to 0
        if pir.motion_detected:
            count = 0
        
        print ("Count down now ",  (delay - count))
        time.sleep(1)

    print("")
    print ("Motion NOT detected for",  (delay), "Sec.\n")

pause(2)
