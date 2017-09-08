#!/bin/bash

#this script should install the needed pieces to make wxpython work with python3
#please report difficulties to christopherrehm@web.de
#this script comes without warranty.

apt-get install dpkg-dev build-essential python3.4-dev # use appropriate Python version
apt-get install libjpeg-dev libtiff-dev
apt-get install libwebkitgtk-dev
apt-get install libgtk2.0-dev
apt-get install libsdl1.2-dev libgstreamer-plugins-base0.10-dev
apt-get install freeglut3
apt-get install freeglut3-dev

apt-get install python3-pip

pip3 install --upgrade --pre -f http://wxpython.org/Phoenix/snapshot-builds/ wxPython_Phoenix

