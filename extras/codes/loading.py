#!/usr/bin/python
# -*- coding: utf-8 -*-

import xbmc
import xbmcgui
import random

HOME = xbmcgui.Window(10000)
HOME.setProperty("LoadingPercent", "1%")
control_progress = HOME.getControl(9001)
loading_count = 0
count = 3
while (count < 100):
    randomInt = random.randint(1, 5)
    count += randomInt
    loading_count += 1
    if count > 100:
        count = 100
    if loading_count % 3 == 1:
        HOME.setProperty("LoadingPoint", ".")
    elif loading_count % 3 == 2:
        HOME.setProperty("LoadingPoint", "..")
    elif loading_count % 3 == 0:
        HOME.setProperty("LoadingPoint", "...")
    loadingPercent = str(count) + "%"
    control_progress.setPercent(float(count))
    HOME.setProperty("LoadingPercent", loadingPercent)
    HOME.setProperty("LoadingPercentInt", str(count))
    xbmc.sleep(200)
xbmc.executebuiltin("RunScript(script.startup.huandong, home)")
