#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import re
import mod_json
cmd = 'sensors'
stdout = str(Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
print(stdout)
stdout = re.findall(r'\\n(.*?)[+]', stdout)
fname = 'TEMPSENS'
mod_json.main(stdout, fname)
