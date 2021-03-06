#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re
from subprocess import Popen, PIPE

import mod_json

cmd = 'sensors'
stdout = str(Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
stdout = re.findall(r'\\n([^:]+):\s+[\+\-]?\d', stdout)
fname = 'TEMPSENS'
mod_json.main(stdout, fname)
