#!/usr/bin/python3
# -*- coding: utf-8 -*-
import mod_json
from subprocess import Popen, PIPE
def cmd(x):
    y = str(Popen(x, shell=True, stdin=PIPE, stdout=PIPE).stdout.read()).replace('b\'', '').replace(' ', '').replace("'", '').rstrip('\\n').split('\\n')
    return y
if len(str(cmd('whereis smartmontools')).split('/')) > 1:
    hdd_find = "sudo smartctl --scan |grep -o sd[a-z] |uniq"
else:
    print('Please: sudo apt install smartmontools')
    hdd_find = ['']
for disk in cmd(hdd_find):
    smart_status = 'sudo smartctl -i /dev/' + disk + ' |grep -o \'Enabled\''
    mod_json.hdd(cmd(hdd_find), cmd(smart_status))

