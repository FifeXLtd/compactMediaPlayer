#!/bin/bash

echo "Updating mount point with new storage device..."

new_UUID=$(sudo blkid -s UUID -o value /dev/sda1)

old_UUID=$(awk '{print $1}' /etc/fstab)
old_UUID=$(echo $old_UUID| cut -c 11-19)

lfstab_line=$(grep -n "rw" /etc/fstab)

old_UUID="UUID=${old_UUID}"
echo Old USB UUID: $old_UUID
echo New USB UUID found: $new_UUID

old_line=$(grep -r $old_UUID /etc/fstab)

a="UUID=${new_UUID}"
b="/volume vfat defaults,auto,users,rw,nofail,noatime 0 0"
new_line="${a} ${b}"
echo "updated: ${new_line}"

sudo sed -i '2 c '"$new_line"'' /etc/fstab

echo "Remounting complete"
echo "Rebooting system..."
sudo reboot



