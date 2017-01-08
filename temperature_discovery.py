#!/usr/bin/python3
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
import re
x = 'sensors'
y = str(Popen(x, shell=True, stdin=PIPE, stdout=PIPE).stdout.read())
z = re.findall('\w\w\w\w\d+|\w\w\w\w \d+', y)
n = 0
l1 = '{\n'
l2 = '\t\"data\":[\n'
l3 = '\t\t{\n'
l4 = '\n\t\t},'
l5 = '\t]\n'
l6 = '}\n'
l7 = '\n\t\t}'
print(l1 + l2)
for n in range(len(z)):
    if n < (len(z) -1):
        print(l3 + '\t\t\t\"{#TEMPSENS}\":' + '\"' + z[n] + '\"' + l4)
    elif n +1 == len(z):
        print(l3 + '\t\t\t\"{#TEMPSENS}\":' + '\"' + z[n] + '\"' + l7)
    n += 1
print(l5 + l6)