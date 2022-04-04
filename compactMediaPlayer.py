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

screen = pygame.display.set_mode()
screen_width = screen.get_width()
screen_height = screen.get_height()
pygame.quit()

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.mouse.set_cursor((8, 8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))


def check_for_usb():
    top_path = "/media/pi"
    resolved_path = "/volume"
    
    USB_stat = 0 # assume there is no connected USB
    try:
        output = subprocess.check_output("sudo blkid -s UUID -o value /dev/sda1", shell=True)
        print("Output: " + str(output))
        USB_stat = 1 # overwrite variable and declare there is a USB
    except:
        print("No connected USB")
   
    check_path = top_path + "*/"
    usb_check = glob(check_path, recursive = True)
    no_usb_devices = len(usb_check)
    
    if(USB_stat == 0):
        print("No USB detected")
        print("Loading media from home directory")
        return False
    else:
        print("USB detected!")
        path = resolved_path + "/"
        print("USB path:" + str(path))
        
        file_status = []
        for i in range(1, 4): # loop through checking
            file = check_usb_status(i, path)
            file_status.append(file)
        print(file_status)
        
        if(file_status == [None, None, None]):
            print("Unrecognised device on mount space - executing script to update UUID")
            rc = subprocess.call("/home/pi/update_UUID.sh") 
            #new_UUID = os.system("ls -l /dev/disk/by-uuid/")
        return(file_status)
        
        
def check_usb_status(file_type, path): # looks for certain files with directories on USB
    if(file_type == 1): # look for video file
        path = path + "video/"
        extension = '.mp4'
    if(file_type == 2): # look for thumbnail file
        path = path + "thumbnail/"
        extension = '.jpg'
    if(file_type == 3): # look for audio file
        path = path + "audio/"
        extension = '.mp3'
    files = []
    for(dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)
    
    if(len(files) != 0):
        return(str(path) + str(files[0]))
    else:
        return None
   
def play_video(path):
    print("Playing video")
    video_call = "omxplayer -p -o local " + str(path)
    subprocess.check_output(video_call, shell=True)
     
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
    if(drive_files[1] != None): # thumbnail
        thumbnail_path = drive_files[1]
    if(drive_files[2] != None): # audio
        audio_path = drive_files[2]   
print(video_path, thumbnail_path, audio_path) 
    
while True:
    wait_for_play = load_thumbnail(thumbnail_path)
    while(wait_for_play == True):
        if GPIO.input(start_pin) == GPIO.LOW:
            wait_for_play = False
            play_video(video_path)
        if GPIO.input(exit_pin) == GPIO.LOW:
            wait_for_play = False
            pygame.quit()
