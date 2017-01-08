#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import re
command = 'lspci |grep \'controller\' |sed \'s/^..:..\..\ //g\'|uniq'
stdout = str(Popen(command, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
stdout = re.findall(r'\\n(.*?):', stdout)

l1 = '{\n'
l2 = '\t\"data\":\n\t['
l3 = '\t\t{'
l3_1 = '\n\t\t\t'
l4 = '\n\t\t},'
l5 = '\t]\n'
l6 = '}\n'
l7 = '\n\t\t}'
counter = 1
controller = '"{#CONTROLLER}":'
print(l1 + l2)
for string in stdout:
    key = string.split(':')[0]
    if counter < len(stdout):
        print(l3 + l3_1 + controller + '\"' + key + '\"' + l4)
        counter += 1
    else:
        print(l3 + l3_1 + controller + '\"' + key + '\"' + l7)
print(l5 + l6)