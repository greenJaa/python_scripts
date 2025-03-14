#!/usr/bin/env python3
import subprocess

def get_ssid():
    raw_wifi = subprocess.check_output(['netsh', 'WLAN', 'show', 'interfaces'])
    data_strings = raw_wifi.decode('utf-8').split()
    index = data_strings.index('Profile')
    return data_strings[index + 2]


get_ssid();