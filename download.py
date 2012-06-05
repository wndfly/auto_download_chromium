#!/usr/bin/env/python
#coding=utf-8

__author__ = 'wm'

import urllib2
import os

if __name__ == '__main__':
    url = 'http://commondatastorage.googleapis.com/chromium-browser-snapshots/Win/LAST_CHANGE'

    req = urllib2.urlopen(url)

    build_code = req.read()

    url2 = 'http://commondatastorage.googleapis.com/chromium-browser-snapshots/Win/%s/chrome-win32.zip' % build_code

    req2 = urllib2.urlopen(url2)

    dir_root = os.getcwd()
    build_dir = os.path.join(dir_root, build_code)

    os.mkdir(build_dir)
    os.chdir(build_dir)

    fHandle = open('chrome-win32.zip', 'wb')

    fHandle.write(req2.read())

    fHandle.close()
