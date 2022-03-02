from moviepy.editor import *
import pygame
import screeninfo
import RPi.GPIO as GPIO
import subprocess
from glob import glob
from os import walk

video_path = 'video.mp4'
thumbnail_path = 'thumbnail.jpg'
audio_path = 'audio.mp3'

embeddedAudio = True # assume the video file has audio for now

start_pin = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(start_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

exit_pin = 24
GPIO.setmode(GPIO.BCM)
GPIO.setup(exit_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

from screeninfo import get_monitors
for m in get_monitors():
    print(m)
    screen_width = m.width
    screen_height = m.height

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
pygame.mouse.set_cursor((8, 8),(0,0),(0,0,0,0,0,0,0,0),(0,0,0,0,0,0,0,0))

def check_for_usb():
    top_path = "/media/pi/"
    check_path = top_path + "*/"
    usb_check = glob(check_path, recursive = True)
    
    no_usb_devices = len(usb_check)
    if(no_usb_devices == 0):
        print("No USB detected")
        return False
    else:
        usb_check = usb_check[0].split("/")
        device_id = usb_check[-2]
        path = top_path + str(device_id) + "/"
        
        file_status = []
        for i in range(1, 4): # loop through checking
            file = check_usb_status(i, path)
            file_status.append(file)

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
    result = subprocess.run(["ffprobe", "-v", "error", "-show_entries",
                             "format=nb_streams", "-of",
                             "default=noprint_wrappers=1:nokey=1", path],
                            stdout = subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    no_streams = (int(result.stdout) -1)
    if(no_streams == 1): # 1 stream = video WITHOUT audio
        embeddedAudio = False # overwrite global
    # anything else we can leave exactly the same

def play_video(path):
    global embeddedAudio
    
    clip = VideoFileClip(path).resize((screen_width, screen_height))
    if(embeddedAudio != True):
        audioclip = AudioFileClip(audio_path)
        newClip = clip.set_audio(audioclip)
        newClip.preview(fullscreen = True)
    else:
        clip.preview(fullscreen = True)
     
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
#print(video_path, thumbnail_path, audio_path) 
 
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