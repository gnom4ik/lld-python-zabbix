#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
def cmd(x):
    y = str(Popen(x, shell=True, stdin=PIPE, stdout=PIPE).stdout.read()).replace('b\'', '').replace(' ', '').replace("'", '').rstrip('\\n').split('\\n')
    return y
if len(str(cmd('whereis smartmontools')).split('/')) > 1:
    hdd_find = "sudo smartctl --scan |grep -o sd[a-z] |uniq"
else:
    print('Please: sudo apt install smartmontools')
    hdd_find = ['']
block_dev = cmd(hdd_find)
l1 = '{\n'
l2 = '\t\"data\":[\n'
l3 = '\t\t{\n'
l4 = '\n\t\t},'
l5 = '\t]\n'
l6 = '}\n'
x = len(block_dev) - 1
n = 0
print(l1 + l2)
while n <= x:
        if block_dev[n] in cmd(hdd_find):
            if n < x:
                smart_status = 'sudo smartctl -i /dev/' + block_dev[n] + ' |grep -o \'Enabled\''
                if cmd(smart_status) == ['Enabled']:
                    status = 1
                else:
                    status = 0
                print(l3 + '\t\t\t\"{#DISKNAME}\":' + '\"' + block_dev[
                    n] + '\",' + '\n\t\t\t\"{#SMART_ENABLED}":' + '\"' + str(status) + '\"' + l4)
            elif n == x:
                smart_status = 'sudo smartctl -i /dev/' + block_dev[n] + ' |grep -o \'Enabled\''
                if cmd(smart_status) == ['Enabled']:
                    status = 1
                else:
                    status = 0
                print(l3 + '\t\t\t\"{#DISKNAME}\":' + '\"' + block_dev[
                    n] + '\",' + '\n\t\t\t\"{#SMART_ENABLED}":' + '\"' + str(status) + '\"' + l4.replace(",", ""))
        n += 1
print(l5 + l6)
