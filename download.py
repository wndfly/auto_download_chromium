#!/usr/bin/env/python
#coding=utf-8

__author__ = 'wm'

'''
download latest chromium
'''

import urllib2
import urllib
import sys
import os
import platform

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

    system_info = platform.system()

    system_name_list = {
        'Linux' : 'Linux',
        'Windows' : 'Win',
        'Darwin' : 'Mac'
    }

    try:
        system_ver = system_name_list[system_info]
    except Exception:
        system_ver = ''

    if system_ver:
        url_build_code = 'http://commondatastorage.googleapis.com/chromium-browser-snapshots/%s/LAST_CHANGE' % system_ver

        req = urllib2.urlopen(url_build_code)

        build_code = req.read()
        
        file_name = 'chrome-win32.zip'

        if system_ver == 'Linux':
            file_name = 'chrome-linux.zip'
        
        if system_ver == 'Mac':
            file_name = 'chrome-mac.zip'
        
        url_download = 'http://commondatastorage.googleapis.com/chromium-browser-snapshots/%s/%s/%s' % (system_ver, build_code, file_name)

        #req2 = urllib2.urlopen(url2)

        #dir_root = os.getcwd()
        #build_dir = os.path.join(dir_root, build_code)

        #os.mkdir(build_dir)
        #os.chdir(build_dir)

        #fHandle = open('chrome-win32.zip', 'wb')

        #fHandle.write(req2.read())

        #fHandle.close()

        print 'Start Download Latest Chromium.'

        urllib.urlretrieve(url_download, file_name, reporthook)

        print 'Completed Download.'

    else:
        print 'Not match chromium with this system!'
