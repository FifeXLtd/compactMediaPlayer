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

sudo wget -O /usr/local/bin/compactVideoPlayer.py https://raw.githubusercontent.com/FifeXLtd/compactVideoPlayer/main/compactVideoPlayer.py
