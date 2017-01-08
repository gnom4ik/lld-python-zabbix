
l1 = '{\n'
l2 = '\t\"data\":\n\t['
l3 = '\t\t{'
l3_1 = '\n\t\t\t'
l4 = '\n\t\t},'
l5 = '\t]\n'
l6 = '}\n'
l7 = '\n\t\t}'

def main(stdin, fname):

    counter = 1
    name = '{1}{3}{5}{0}{4}{1}{2}'.format(fname, '\"', ':', '{', '}', '#')
    print(l1 + l2)
    for string in stdin:
        key = string.split(':')[0]
        if counter < len(stdin):
            print(l3 + l3_1 + name + '\"' + key + '\"' + l4)
            counter += 1
        else:
            print(l3 + l3_1 + name + '\"' + key + '\"' + l7)
    print(l5 + l6)

def hdd(stdin):
    from subprocess import Popen, PIPE
    x = len(stdin) - 1
    n = 0
    print(l1 + l2)
    while n <= x:
        if stdin[n] in stdin:
            smart_status = str(Popen('sudo smartctl -i /dev/' + stdin[n] + ' |grep -o \'Enabled\'', shell=True, stdin=PIPE,stdout=PIPE).stdout.read())
            smart_status = smart_status.replace('b\'', '').replace(' ', '').replace("'", '').rstrip('\\n').split('\\n')
            if n < x:
                if smart_status == ['Enabled']:
                    status = 1
                else:
                    status = 0
                print(l3 + '\t\t\t\"{#DISKNAME}\":' + '\"' + stdin[n] + '\",' + '\n\t\t\t\t\t\"{#SMART_ENABLED}":' + '\"' + str(status) + '\"' + l4)
            elif n == x:
                if smart_status == ['Enabled']:
                    status = 1
                else:
                    status = 0
                print(l3 + '\t\t\t\"{#DISKNAME}\":' + '\"' + stdin[n] + '\",' + '\n\t\t\t\t\t\"{#SMART_ENABLED}":' + '\"' + str(status) + '\"' + l4.replace(",", ""))
        n += 1
    print(l5 + l6)
