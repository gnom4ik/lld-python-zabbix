#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from subprocess import Popen, PIPE

from share.zabbix.externalscripts import mod_json

command = 'ps -eo %cpu,command |sort -g |tail -n10 |sed \'s/^....//g;s/^ //g\' |cut -c1-50'
stdout = str(Popen(command, shell=True, stdin=PIPE, stdout=PIPE).stdout.read()).replace('b\'','\\n')
stdout = re.findall(r'\\n(.*?)\\n', stdout.strip('\\nCOMMAND\\n'))
fname = 'PROCESS'
mod_json.main(stdout, fname)
