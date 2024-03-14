#!/bin/bash

echo "Thanks for choosing to install OpenVPN-QT"
echo "We will ask for elevated rights to install dependencies, and configure your system"
echo "- - - - -"

# Blowing away any previous installation
sudo rm -rf /opt/openvpn3-qt/ || echo "No previous installation found - p1"
sudo rm -rf /usr/share/applications/openvpn3-qt.desktop || echo "No previous installation found - p2"
echo "- - - - -"

OS_RELEASE=$(cat /etc/os-release | grep NAME)
echo "Installing OpenVPN3-QT on: $OS_RELEASE"

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

# Creates the folder where the project gets checked out with the right perms
cd /opt
sudo mkdir openvpn3-qt
sudo chmod a+rw openvpn3-qt

# Cloning the project
git clone https://github.com/guy-keller/openvpn3-qt.git

# Set up the app locally ( creates venv and shortcut )
cd /opt/openvpn3-qt/other/
chmod +x setup-app.sh
source setup-app.sh

echo "- - - - -"
echo "If you see any error messages, please do raise a bug on GitHub thanks!"
echo "Otherwise, congratulations OpenVPN3-QT has been installed!"
echo "Push the 'super' button, look for it and start using."
echo "You can now close this window, cheers!"
