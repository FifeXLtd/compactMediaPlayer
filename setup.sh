#!/bin/bash

echo "Running setup script from GitHub..."
echo "Installing required modules..."
echo "1/7: 'moviepy'"
#sudo pip install moviepy 
echo "2/7: 'pygame'"
sudo pip install pygame
echo "3/7: 'screeninfo'"
#sudo pip install screeninfo
echo "4/7: RPI.GPIO"
echo "Skipping..."
echo "5/7: 'subprocess'"
echo "Skipping..."
echo "6/7: 'glob'"
echo "Skipping..."
echo "7/7: 'os'"
echo "Skipping..."

echo "Installing compactMediaPlayerScript"
sudo mkdir /usr/local/bin/compactMediaPlayer
sudo wget -O /usr/local/bin/compactMediaPlayer/compactMediaPlayer.py https://raw.githubusercontent.com/FifeXLtd/compactMediaPlayer/main/compactMediaPlayer.py

echo "Installing contributing scripts"
sudo wget -O /home/pi/update_UUID.sh https://raw.githubusercontent.com/FifeXLtd/compactMediaPlayer/main/update_UUID.sh
sudo chmod +x /home/pi/update_UUID.sh # give permissions 

echo "Installing omxplayer"
sudo wget http://archive.raspberrypi.org/debian/pool/main/o/omxplayer/omxplayer_20190723+gitf543a0d-1_armhf.deb
sudo dpkg -i omxplayer_20190723+gitf543a0d-1_armhf.deb
sudo apt-get -f install
rm omxplayer_20190723+gitf543a0d-1_armhf.deb
echo "omxplayer installed successfully!"


echo "Creating default mount point"
sudo mkdir /volume                                       # creates directory
sudo chown -R pi:pi /volume  

echo "Giving full permissions to script..."
sudo chmod a+r /usr/local/bin/compactMediaPlayer/compactMediaPlayer.py
sudo chmod a+w /usr/local/bin/compactMediaPlayer/compactMediaPlayer.py
sudo chmod a+x /usr/local/bin/compactMediaPlayer/compactMediaPlayer.py
sudo chmod a+X /usr/local/bin/compactMediaPlayer/compactMediaPlayer.py
echo "Permissions set."

echo "Installing zram"
sudo wget -q https://git.io/vM1kx -O /tmp/rpizram && bash /tmp/rpizram

echo "Automatating script on boot"
sudo sed -i -e '$i # added for compactMediaPlayer by Ben Morris\nsudo python3 /usr/local/bin/compactMediaPlayer/compactMediaPlayer.py &\n' /etc/profile

