OpenVPN3-QT 
============
OpenVPN3 QT Client written in Python3.

## OpenVPN 3
First and foremost, please download and install OpenVPN 3 from here:  
https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux

Quick command line overview - connect to a vpn:
```shell
openvpn3 session-start --config /home/user/Documents/example.ovpn
```

To check if you are connected:
```shell
openvpn3 sessions-list
```

To disconnect:
```shell
openvpn3 session-manage --path "/net/openvpn/v3/sessions/UUID_FROM_SESSIONS_LIST" --disconnect
```

## OpenVPN 3 - QT Client

Once you know that openvpn3 is working, give this QT client a go!  

To install copy and paste the following commands in a terminal:
```shell
cd /opt && sudo mkdir openvpn3-qt && sudo chmod a+rw openvpn3-qt
git clone https://github.com/guy-keller/openvpn3-qt.git
cd openvpn3-qt && chmod +x install.sh && ./install.sh
```

After running the commands above you are good to go.  
Press the 'super' key, and look for the OpenVPN3 shortcut.

Supports: Debian, Ubuntu, Fedora and RHEL    
Desktop Environment: Gnome

### Screenshots

Shortcut:    
<img src="other/assets/shortcut.png" width="450" heigth="200">

UI - Fields:  
<img src="other/assets/ui-1.png" width="450" heigth="200">

UI - Connect:  
<img src="other/assets/ui-2.png" width="450" heigth="200">

UI - Connected:  
<img src="other/assets/ui-3.png" width="450" heigth="200">

### Uninstalling / Removing OpenVPN3 - QT Client

Paste the following in a terminal:
```shell
sudo rm -rf /opt/openvpn3-qt/
sudo rm -rf /usr/share/applications/ovpn3-qt.desktop
```

### Disclaimer

THIS CODE IS PROVIDED AS IS WITHOUT WARRANTY OF ANY KIND, EITHER EXPRESS OR IMPLIED, INCLUDING ANY IMPLIED WARRANTIES OF FITNESS FOR A PARTICULAR PURPOSE, MERCHANTABILITY, OR NON-INFRINGEMENT.
ALL RIGHTS RESERVED TO THE COMPANIES/TRADEMARKS MENTIONED.

