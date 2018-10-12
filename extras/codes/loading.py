#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import random

HOME = xbmcgui.Window(10000)
HOME.setProperty("LoadingPercent", "1%")
control_progress = HOME.getControl(9001)
count = 0
while (count < 100):
    randomInt = random.randint(1, 5)
    count += randomInt
    if count > 100:
        count = 100
    loadingPercent = str(count) + "%"
    control_progress.setPercent(float(count))
    HOME.setProperty("LoadingPercent", loadingPercent)
    HOME.setProperty("LoadingPercentInt", str(count))
    xbmc.sleep(200)
xbmc.executebuiltin("RunScript(script.startup.huadong, home)")
