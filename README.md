OpenVPN3-QT 
============
OpenVPN3 QT Client written in Python3.

## OpenVPN 3
Please download and install OpenVPN 3 from here:  
https://community.openvpn.net/openvpn/wiki/OpenVPN3Linux

To use it in the command line - connect:
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
## Open VPN 3 - QT Client

Alternatively, you can give this QT client a go.

```shell
git clone https://github.com/guy-keller/openvpn3-qt.git
cd openvpn3-qt && chmod +x install.sh && ./install.sh
```

Supports: Debian, Ubuntu, Fedora and RHEL
Desktop Environment: Gnome
