#!/usr/bin/python3
# -*- coding: utf-8 -*-

from subprocess import Popen, PIPE
import re
md_find = "cat /proc/mdstat |grep -o 'md[0-9]*' |uniq"
y = str(Popen(md_find, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
z = re.findall('md\d+', y)
l1 = '{\n'
l2 = '\t\"data\":[\n'
l3 = '\t\t{\n'
l4 = '\n\t\t},'
l5 = '\t]\n'
l6 = '}\n'

if z == []:
    exit()
else:
    print(l1 + l2)
    for n in range(len(z)):
        if n < (len(z) -1):
            print(l3 + '\t\t\t\"{#MDRAID}\":' + '\"' + z[n] + '\"' + l4)
        elif (n +1) == len(z):
            print(l3 + '\t\t\t\"{#MDRAID}\":' + '\"' + z[n] + '\"' + l4.replace(",", ""))
        n += 1
    print(l5 + l6)