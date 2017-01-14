#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import re
import mod_json
command = 'ps -eo command |sed \'s/\[//g;s/\]//g;s/^-//g\' |uniq'
stdout = str(Popen(command, shell=True, stdin=PIPE, stdout=PIPE).stdout.read()).replace('b\'','\\n')
stdout = re.findall(r'\\n(.*?)\\n', stdout.strip('\\nCOMMAND\\n'))
fname = 'PROCESS'
mod_json.main(stdout, fname)
