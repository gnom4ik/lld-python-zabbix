#!/usr/bin/python3
# -*- coding: utf-8 -*-

import re
from subprocess import Popen, PIPE

from share.zabbix.externalscripts import mod_json

command = 'lspci |sed \'s/^..:..\..\ //g\'|uniq'
stdout = str(Popen(command, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
stdout = re.findall(r'\\n(.*?):', stdout)
fname = 'CONTROLLER'
mod_json.main(stdout, fname)
