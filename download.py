#!/usr/bin/env/python
#coding=utf-8

__author__ = 'wm'

import urllib2
import urllib
import sys
import os

def reporthook(*a):
    #os.system('cls')
    #print 'Download process: ' + str(int(float(a[0]) * float(a[1]) / float(a[2]) * 100)) + '%.'
    pro_value = int(float(a[0]) * float(a[1]) / float(a[2]) * 100)

    pro_str = '=' * (pro_value / 2)  + '.' * (50 - pro_value / 2)

    if pro_value / 2 < 100:
        pro_str = pro_str.replace('=.', '>.')

    #sys.stdout.write('Download process: ' + str(pro_value) + '%.\r')
    sys.stdout.write('[' + pro_str + '] ' + str(pro_value) + '%.\r')
    sys.stdout.flush()

    if pro_value >= 100:
        sys.stdout.write('\n')

if __name__ == '__main__':
    url = 'http://commondatastorage.googleapis.com/chromium-browser-snapshots/Win/LAST_CHANGE'

    req = urllib2.urlopen(url)

    build_code = req.read()

    url2 = 'http://commondatastorage.googleapis.com/chromium-browser-snapshots/Win/%s/chrome-win32.zip' % build_code

    #req2 = urllib2.urlopen(url2)

    #dir_root = os.getcwd()
    #build_dir = os.path.join(dir_root, build_code)

    #os.mkdir(build_dir)
    #os.chdir(build_dir)

    #fHandle = open('chrome-win32.zip', 'wb')

    #fHandle.write(req2.read())

    #fHandle.close()

    print 'Start Download Latest Chromium.'

    urllib.urlretrieve(url2, 'chrome-win32.zip',reporthook)

    print 'Completed Download.'
