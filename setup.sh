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
sudo pip install glob
echo "Skipping..."
sudo pip install os
echo "Skipping..."
