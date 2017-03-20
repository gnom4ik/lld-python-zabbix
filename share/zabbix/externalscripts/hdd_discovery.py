#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
from subprocess import Popen, PIPE

import mod_json


def cmd(command):

    string = str(Popen(command, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
    return string


if '/etc/smartmontools' in str(cmd('whereis smartmontools')):
    hdd_find = "sudo smartctl --scan |grep -o sd[a-z] |uniq"
    mod_json.hdd(re.findall(r'sd[a-z]', cmd(hdd_find)))
else:
    print('Please: sudo apt install smartmontools')
    exit()
