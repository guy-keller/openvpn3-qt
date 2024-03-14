#!/bin/bash

# Blowing away any previous installation
sudo rm -rf /opt/openvpn3-qt/
sudo rm -rf /usr/share/applications/openvpn3-qt.desktop

OS_RELEASE=$(cat /etc/os-release | grep NAME)

# Installing deps on DEB based distros
if [[ "$OS_RELEASE" == *"Debian"* ]] || [[ "$OS_RELEASE" == *"Ubuntu"* ]]; then
  sudo apt install python3 -y
  sudo apt install python3-pip -y
  sudo apt install git -y
fi

# Installing deps on RPM based distros
if [[ "$OS_RELEASE" == *"Fedora"* ]] || [[ "$OS_RELEASE" == *"Red Hat"* ]]; then
  sudo dnf install python3 -y
  sudo dnf install python3-pip -y
  sudo dnf install git -y
fi

# Cloning the project
cd /opt
git clone https://github.com/guy-keller/openvpn3-qt.git
sudo chmod a+rw openvpn3-qt

# Set up the app locally ( creates venv and shortcut )
cd /opt/openvpn3-qt/other/
chmod +x setup-app.sh
source setup-app.sh
