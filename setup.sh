#!/bin/bash

echo "Running setup script from GitHub..."
echo "Installing required modules..."
echo "1/7: 'moviepy'"
sudo pip install moviepy 
echo "2/7: 'pygame'"
sudo pip install pygame
echo "3/7: 'screeninfo'"
sudo pip install screeninfo
echo "4/7: RPI.GPIO"
echo "Skipping..."
echo "5/7: 'subprocess'"
echo "Skipping..."
echo "6/7: 'glob'"
echo "Skipping..."
echo "7/7: 'os'"
echo "Skipping..."

echo "Installing compactMediaPlayerScript"
sudo wget -O /usr/local/bin/compactMediaPlayer.py https://raw.githubusercontent.com/FifeXLtd/compactMediaPlayer/main/compactMediaPlayer.py
echo "Installing default thumbnail, video and audio files"
echo "1/3: Thumbnail..."
sudo wget -O /home/pi/thumbnail.jpg https://github.com/FifeXLtd/compactMediaPlayer/blob/dc1274a77cee455c1d60bc03b60c6e6dff0592b3/thumbnail.jpg
echo "2/3: Video..."
sudo wget -O /home/pi/video.mp4 https://github.com/FifeXLtd/compactMediaPlayer/blob/dc1274a77cee455c1d60bc03b60c6e6dff0592b3/video.mp4
echo "3/3: Audio..."
sudo wget -O /home/pi/audio.mp3 https://github.com/FifeXLtd/compactMediaPlayer/blob/dc1274a77cee455c1d60bc03b60c6e6dff0592b3/audio.mp3
echo "Default files downloaded successfully to '/home/pi/'


