# compactMediaPlayer

- A interface for loading a thumbnail graphic/splash screen and playing a video file on button press (in loop).
- As this is designed to run all day long, I suggest you boot the pi in terminal auto-login to save on memory(especially on pi zero2)

Two step instruction for installation:

1 - Copy install.sh, video.mp4, thumbnail.jpg & audio.mp3 onto a removable drive and paste inside the home directory of a Raspberry Pi (/home/pi/). Remove drive when you are done.

2 - Create a mount point for future removable drives 
    
     sudo mkdir /volume   # creates directory for mount
     sudo chown -R pi:pi /volume  # give full permissions to directory 
     
     sudo nano /etc/fstab # open mount file
     # create a new line on below the first line and add the following: 
     UUID=PLACE_HOLDER /volume vfat defaults,auto,users,rw,nofail,noatime 0 0
    
3 - Reboot the pi and ensure there is a new empty directory named /volume
    
4 - Execute the install script [PLEASE ENSURE YOU ARE CONNECTED TO THE INTERNET TO ACCESS GITHUB]

    sudo chmod +x /home/pi/install.sh  # give permission to .sh    
    sudo /home/pi/install.sh # execute .sh
 
The Raspberry Pi will now reboot, loading the default files from step one. 

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







