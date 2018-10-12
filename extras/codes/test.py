#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import xbmc

extrasdir = xbmc.translatePath("special://skin/extras")
downloaddir = "C:/Download"
print "current dir is: %s" % os.getcwd()
print "skin extras dir is: %s" % extrasdir

os.chdir(downloaddir)
print "current dir is: %s" % os.getcwd()
url = os.getcwd() + "/20160810-111059351.mkv"
xbmc.Player().play(url)
xbmc.executebuiltin("ActivateWindow(fullscreenvideo)")
