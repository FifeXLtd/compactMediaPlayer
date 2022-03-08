from moviepy.editor import *
import pygame
import RPi.GPIO as GPIO
import subprocess
import time
from glob import glob
import os
from os import walk

video_path = '/home/pi/video.mp4'
thumbnail_path = '/home/pi/thumbnail.jpg'
audio_path = '/home/pi/audio.mp3'

embeddedAudio = True # assume the video file has audio for now

start_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(start_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

exit_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(exit_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def wait_for_mounts():
    # routine that gives system time to find a USB if avaialable
    mount_status = False
    while(mount_status == False):
        for i in range(500):
            mount_check = glob('/volume/*/', recursive = True)
            #print(mount_check)
        mount_status = True

def get_revision(): # find out pi version - there are a few differences we need to take into account 
    myrevision = "0000"
    try:
        f = open('/proc/cpuinfo','r')
        for line in f:
            if line[0:8] == 'Revision':
                length = len(line)
                myrevision = line[11:length-1]
        f.close()
    except:
        myrevision = "0000"
    print("Board Revision: " + str(myrevision))
    return myrevision

wait_for_mounts()
version = get_revision()

if(version != 'c03112'): # not the pi 4
    from screeninfo import get_monitors
    for m in get_monitors():
        print(m)
        screen_width = m.width
        screen_height = m.height

else: # pi 4
    screen = pygame.display.set_mode()
    screen_width = screen.get_width()
    screen_height = screen.get_height()
    pygame.quit()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mouse.set_cursor((8, 8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))


def check_for_usb():
    top_path = "/media/pi/"
    resolved_path = "/volume"
    
    check_path = top_path + "*/"
    usb_check = glob(check_path, recursive = True)
    
    no_usb_devices = len(usb_check)
    if(no_usb_devices == 0):
        print("No USB detected")
        return False
    else:
        print("USB detected!")
        #usb_check = usb_check[0].split("/")
        #device_id = usb_check[-2]
        path = resolved_path + "/"
        print("USB path:" + str(path))
        
        
        file_status = []
        for i in range(1, 4): # loop through checking
            file = check_usb_status(i, path)
            file_status.append(file)
        
        if(file_status == [None, None, None]):
            print("Unrecognised device on mount space - executing script to update UUID")
            rc = subprocess.call("/home/pi/update_UUID.sh") 
            #new_UUID = os.system("ls -l /dev/disk/by-uuid/")
        return(file_status)
        
        
def check_usb_status(file_type, path): # looks for certain files with directories on USB
    if(file_type == 1): # look for video file
        path = path + "video/"
        extension = '.mp4'
    if(file_type == 2): # look for video file
        path = path + "thumbnail/"
        extension = '.jpg'
    if(file_type == 3): # look for video file
        path = path + "audio/"
        extension = '.mp3'
    files = []
    for(dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
    
    if(len(files) != 0):
        return(str(path) + str(files[0]))
    else:
        return None
   
def check_for_audio(path):
    global embeddedAudio
    
    print("Looking for embedded audio at: " + str(path))
    
    try:
        audio = VideoFileClip(path)
        audio.audio.write_audiofile('/home/pi/audio_holder.mp3')
    except:
        print("No audio to extract")
        embeddedAudio = False

def play_video(path):
    global embeddedAudio
    
    clip = VideoFileClip(path).resize((screen_width, screen_height))
    if(embeddedAudio == True):
        print("No audio detected, attaching sound source")
        audioclip = AudioFileClip('/home/pi/audio_holder.mp3')
    else:
        audioclip = AudioFileClip(audio_path)
    newClip = clip.set_audio(audioclip)
    newClip.preview(fullscreen = True)
     
def load_thumbnail(path):
    image = pygame.image.load(path).convert()
    image = pygame.transform.scale(image, (screen_width, screen_height))
    screen.blit(image, (0, 0))
    pygame.display.update()
    return True
     
# start of routine

drive_files = check_for_usb()

if(drive_files != False):
    if(drive_files[0] != None): # video
        video_path = drive_files[0]
    if(drive_files[1] != None): # video
        thumbnail_path = drive_files[1]
    if(drive_files[2] != None): # video
        audio_path = drive_files[2]   
print(video_path, thumbnail_path, audio_path) 
 
check_for_audio(video_path) # determine if the video has embedded audio      
while True:
    wait_for_play = load_thumbnail(thumbnail_path)
    while(wait_for_play == True):
        if GPIO.input(start_pin) == GPIO.LOW:
            wait_for_play = False
            play_video(video_path)
        if GPIO.input(exit_pin) == GPIO.LOW:
            wait_for_play = False
            pygame.quit()


