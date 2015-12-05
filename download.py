#!/usr/bin/env/python
#coding=utf-8

"""
download latest chromium
"""

from __future__ import unicode_literals

__author__ = 'wm'

try:
    import urllib2 as url_request
except ImportError:
    from urllib import request as url_request

try:
    from urllib import urlretrieve as url_retrieve
except ImportError:
    from urllib.request import urlretrieve as url_retrieve

import sys
import platform

#DOWNLOAD_URL_PRE = 'http://commondatastorage.googleapis.com/chromium-browser-snapshots'
DOWNLOAD_URL_PRE = 'https://commondatastorage.googleapis.com/chromium-browser-continuous'

SYSTEM_NAME_LIST = {
    'Linux': {
        '32': 'Linux',
        '64': 'Linux_x64'
    },
    'Windows': {
        '32': 'Win',
        '64': 'Win_x64'
    },
    'Darwin': {
        '32': 'Mac',
        '64': 'Mac'
    }
}


def reporthook(*a):
    """
    download progress bar.
    """
    pro_value = int(float(a[0]) * float(a[1]) / float(a[2]) * 100)

    pro_str = '=' * int(pro_value / 2) + '.' * int(50 - pro_value / 2)

    if pro_value / 2 < 100:
        pro_str = pro_str.replace('=.', '>.')

    sys.stdout.write('[' + pro_str + '] ' + str(pro_value) + '%.\r')
    sys.stdout.flush()

    if pro_value >= 100:
        sys.stdout.write('\n')


def get_system_ver(bit=64):
    system_info = platform.system()
    machine_info = platform.machine()

    try:
        if machine_info.find('64') == -1 or bit == '32':
            return SYSTEM_NAME_LIST[system_info]['32']
        else:
            return SYSTEM_NAME_LIST[system_info]['64']
    except KeyError:
        return ''


def download_chromium(system_ver=SYSTEM_NAME_LIST['Windows']['32']):
    """
    start download chromium.
    """
    if system_ver:
        url_build_code = '%s/%s/LAST_CHANGE' % (DOWNLOAD_URL_PRE, system_ver)

        req = url_request.urlopen(url_build_code)

        build_code = req.read().decode('utf-8')

        if system_ver.lower().find('linux') != -1:
            file_name = 'chrome-linux.zip'
        elif system_ver.lower().find('mac') != -1:
            file_name = 'chrome-mac.zip'
        else:
            file_name = 'chrome-win32.zip'

        url_download = '%s/%s/%s/%s' % (DOWNLOAD_URL_PRE, system_ver, build_code, file_name)

        print('Start Download Latest Chromium.')

        url_retrieve(url_download, file_name, reporthook)

        print('Completed Download.')

    else:
        print('Not match chromium with this system!')

if __name__ == '__main__':
    if len(sys.argv) >= 2:
        system_ver = get_system_ver(sys.argv[1])
    else:
        system_ver = get_system_ver()

    download_chromium(system_ver)
