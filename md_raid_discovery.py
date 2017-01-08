#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import re
import mod_json
md_find = "cat /proc/mdstat |grep -o 'md[0-9]*' |uniq"
y = str(Popen(md_find, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
stdout = re.findall('md\d+', y)
controller = 'MDRAID'
if stdout:
    mod_json.main(stdout, controller)
else:
    exit()
