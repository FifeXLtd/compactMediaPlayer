# compactMediaPlayer

- A interface for loading a thumbnail graphic/splash screen and playing a video file on button press (in loop).
- As this is designed to run all day long, I suggest you boot the pi in terminal auto-login to save on memory(especially on pi zero2)

Two step instruction for installation:

1 - Copy install.sh, video.mp4, thumbnail.jpg & audio.mp3 onto a removable drive and paste inside the home directory of a Raspberry Pi (/home/pi/). Remove drive when you are done.

2 - Enter the following 3 lines within a terminal window:
     
    
    sudo chmod +x /home/pi/install.sh       
    sudo /usr/local/bin/install.sh 
    sudo mv install.sh /usr/local/bin # move install script to bin directory as it is no longer needed

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







