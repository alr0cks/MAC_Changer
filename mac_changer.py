#!/usr/bin/env python

import subprocess

subprocess.call("ifconfig wlan0 down", shell=True)
subprocess.call("ifconfig wlan0 hw ether 12:23:34:45:56:67", shell=True)
subprocess.call("ifconfig wlan0 up", shell=True)

