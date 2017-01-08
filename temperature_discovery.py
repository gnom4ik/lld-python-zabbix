#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import re
import mod_json
x = 'sensors'
y = str(Popen(x, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
stdout = re.findall('\w\w\w\w\d+|\w\w\w\w \d+', y)
fname = 'TEMPSENS'
mod_json.out(stdout, fname)
