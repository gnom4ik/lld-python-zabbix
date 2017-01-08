#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import re
command = 'lspci |grep \'controller\' |sed \'s/^..:..\..\ //g\'|uniq'
stdout = str(Popen(command, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
stdout = re.findall(r'\\n(.*?):', stdout)

l1 = '{\n'
l2 = '\t\"data\":[\n'
l3 = '\t\t{\n'
l3_1 = '\n\t\t\t'
l4 = '\n\t\t},'
l5 = '\t]\n'
l6 = '}\n'
l7 = '\n\t\t}'

controller = '"{#CONTROLLER}":'
print(l1 + l2)
for string in stdout:
    key = string.split(':')[0]
    print(l3 + l3_1 + controller + '\"' + key + '\"' + l4)
