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
sudo wget -O /home/pi/compactMediaPlayer.py https://raw.githubusercontent.com/FifeXLtd/compactMediaPlayer/main/compactMediaPlayer.py

echo "Giving full permissions to script..."
sudo chmod a+r /home/pi/compactMediaPlayer.py
sudo chmod a+w /home/pi/compactMediaPlayer.py
sudo chmod a+x /home/pi/compactMediaPlayer.py
sudo chmod a+X /home/pi/compactMediaPlayer.py
echo "Permissions set."

echo "Installing zram"
sudo wget -q https://git.io/vM1kx -O /tmp/rpizram && bash /tmp/rpizram

echo "Automatating script on boot"
sudo sed -i -e '$i # added for compactMediaPlayer by Ben Morris\nsudo python3 /home/pi/compactMediaPlayer.py &\n' /etc/profile


