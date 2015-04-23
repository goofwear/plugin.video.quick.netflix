#!/usr/bin/python
# -*- coding: utf-8 -*-
import urllib
import sys
import re
import os
import subprocess
import xbmcplugin
import xbmcgui
import xbmcaddon

chrome64 = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe'
path = 'C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe http://www.netflix.com/MyList?leid=595&link=subnav --kiosk'
path64 = 'C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe http://www.netflix.com/MyList?leid=595&link=subnav --kiosk'
RemoteNav = xbmc.translatePath('special://home/addons/plugin.video.quick.netflix/resources/nav.exe')

def showSite():
    subprocess.Popen(RemoteNav, shell=False)
    if os.path.exists(chrome64):
        subprocess.Popen(path64, shell=False)
    else:
        subprocess.Popen(path, shell=False)
    
showSite()