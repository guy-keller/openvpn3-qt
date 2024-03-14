#!/bin/bash

OS_RELEASE=$(cat /etc/os-release | grep NAME)

if [[ "$OS_RELEASE" == *"Debian"* ]] || [[ "$OS_RELEASE" == *"Ubuntu"* ]]; then
  sudo apt install python3 -y
  sudo apt install python3-pip -y
fi

if [[ "$OS_RELEASE" == *"Fedora"* ]] || [[ "$OS_RELEASE" == *"Red Hat"* ]]; then
  sudo dnf install python3 -y
  sudo dnf install python3-pip -y
fi


cd $(dirname "$0")
python3 -m venv venv
source venv/bin/activate

pip3 install -r requirements.txt
sudo cp other/ovpn3-qt.desktop /usr/share/applications

sudo update-desktop-database /usr/share/applications
sudo xdg-desktop-menu forceupdate
