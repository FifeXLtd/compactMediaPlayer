#! /bin/bash

## Installation script for 'compactMediaPlayer' by Ben Morris for FifeX Ltd

## First let's obtain the 'compactMediaPlayer.sh' script from GitHub 

sudo wget -O /home/pi/setup.sh https://raw.githubusercontent.com/FifeXLtd/compactMediaPlayer/main/setup.sh
sudo chmod +x /home/pi/setup.sh
sudo /home/pi/setup.sh

echo "Installation successful"
echo "Rebooting..."
sudo reboot
