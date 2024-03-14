#!/bin/bash

# Goes into the project folder, and activates venv
cd /opt/openvpn3-qt/
python3 -m venv venv
source venv/bin/activate

# Install the deps and copies the desktop shortcut
pip3 install -r requirements.txt
sudo cp other/openvpn3-qt.desktop /usr/share/applications

# Refresh the menu, so that the app icon is displayed
sudo update-desktop-database /usr/share/applications
sudo xdg-desktop-menu forceupdate
