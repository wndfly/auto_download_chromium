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

DOWNLOAD_URL_PRE = 'http://commondatastorage.googleapis.com/chromium-browser-snapshots'

SYSTEM_NAME_LIST = {
    'Linux': 'Linux',
    'Windows': 'Win',
    'Darwin': 'Mac'
}


def reporthook(*a):
    """
    download progress bar.
    """
    pro_value = int(float(a[0]) * float(a[1]) / float(a[2]) * 100)

    pro_str = '=' * (pro_value / 2) + '.' * (50 - pro_value / 2)

    if pro_value / 2 < 100:
        pro_str = pro_str.replace('=.', '>.')

    sys.stdout.write('[' + pro_str + '] ' + str(pro_value) + '%.\r')
    sys.stdout.flush()

    if pro_value >= 100:
        sys.stdout.write('\n')


def get_system_ver():
    system_info = platform.system()

    try:
        return SYSTEM_NAME_LIST[system_info]
    except KeyError:
        return ''


def download_chromium(system_ver=SYSTEM_NAME_LIST['Windows']):
    """
    start download chromium.
    """
    if system_ver:
        url_build_code = '%s/%s/LAST_CHANGE' % (DOWNLOAD_URL_PRE, system_ver)

        req = url_request.urlopen(url_build_code)

        build_code = req.read()

        file_name = 'chrome-win32.zip'

        if system_ver == 'Linux':
            file_name = 'chrome-linux.zip'

        if system_ver == 'Mac':
            file_name = 'chrome-mac.zip'

        url_download = '%s/%s/%s/%s' % (DOWNLOAD_URL_PRE, system_ver, build_code, file_name)

        print('Start Download Latest Chromium.')

        url_retrieve(url_download, file_name, reporthook)

        print('Completed Download.')

    else:
        print('Not match chromium with this system!')

if __name__ == '__main__':

    system_ver = get_system_ver()

    download_chromium(system_ver)
