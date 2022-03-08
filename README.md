compactMediaPlayer

A interface for loading a thumbnail graphic/splash screen and playing a video file on button press (in loop).

As this is designed to run all day long, I suggest you boot the pi in terminal auto-login to save on memory(especially on pi zero2)
Two step instruction for installation:

compactMediaPlayer will encounter 3 different situations:
    
    1 - There is no USB connected: this will load the default files from the home directory
    2 - There is a USB connected, but it is unregistered(new): this will go detected and a system remount will occur forcing a reboot
    3 - There is a USB connected, and it is registered: this will load the USB files on boot no problem.
    
For installation I suggest you start with a clean flash of an existing Raspberry Pi OS. I used the 1.1GB RPI legacy (with desktop enviroment).


[INSTALLATION]

1 - Copy install.txt, video.mp4, thumbnail.jpg & audio.mp3 onto a removable drive and paste inside the home directory of a Raspberry Pi (/home/pi/). Remove drive when you are done.

Next, create a new file within the home directory named install.sh and paste the contents of 'install.txt' into it. Delete install.txt once this is done.

2 - Enter the following 3 lines within a terminal window:

FIRST ENSURE YOU HAVE AN INTERNET CONNECTION

    # add next line under the first line and add:
    UUID=PLACE_HOLDER /volume vfat defaults,auto,users,rw,nofail,noatime 0 0
    
    # next we can install 
    sudo chmod +x /home/pi/install.sh   # give permissions
    sudo /home/pi/install.sh   # execute script
    # the script will reboot system once everything has complete
    
The Raspberry Pi will now reboot. Please keep in my if you have a USB attached, it will reboot twice (as it is unregistered) so please be patient. 

Attach a button to GPIO 17 to start video play, and use GPIO 24 to exit (you can only exit in thumbnail mode).

CHANGE MEDIA FILES:

Attach a removable drive including 3 seperate folders: 'video', 'thumbnail' and 'audio'. 
Keep in mind, the system will always first check for embedded audio within the video file before resorting to a audio overlay.

Inisde each folder, put the file you wish to play. The file name can be anything you wish, with the following extensions:

Tested 'video' formats 
    
    .mp4
    .mov

Tested 'thumbnail' formats:  
   
    .jpg
    .png 

Tested 'audio' formats:
    
    .wav
    .mp3
Keep in mind if you wish to change media, you must reboot the pi before it can take effect.



