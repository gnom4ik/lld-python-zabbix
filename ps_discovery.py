#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import re
import mod_json
command = 'cat /etc/passwd'
stdout = str(Popen(command, shell=True, stdin=PIPE, stdout=PIPE).stdout.read()).replace('b\'','\\n')
stdout = re.findall(r'\\n(.*?):', stdout)
fname = 'USERNAME'
mod_json.main(stdout, fname)
