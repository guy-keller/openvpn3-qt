#!/bin/bash

rm -rf /tmp/openvpn3-qt

mkdir -p /tmp/openvpn3-qt/opt/
cd /tmp/openvpn3-qt/opt/
git clone https://github.com/guy-keller/openvpn3-qt.git

mv /tmp/openvpn3-qt/opt/openvpn3-qt/build/DEBIAN /tmp/openvpn3-qt/
cd /tmp
dpkg-deb --build openvpn3-qt

ls /tmp/openvpn3-qt.deb
dpkg -c openvpn3.deb

rm -rf /tmp/openvpn3-qt
echo "deb package created on /tmp"
