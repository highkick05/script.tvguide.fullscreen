import sys
import xbmc,xbmcaddon,xbmcvfs
from subprocess import Popen
import os
'''
import psutil

PROCNAME = "ffmpeg.exe"

for proc in psutil.process_iter():
    # check whether the process name matches
    if proc.name() == PROCNAME:
        proc.kill()
'''
# Windows specific
cmd =['/system/xbin/pkill','-2','ffmpeg']
p = Popen(cmd,shell=False)
player = xbmc.Player()
player.stop()
