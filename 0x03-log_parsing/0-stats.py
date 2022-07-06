#!/usr/bin/python3
'''a script that reads stdin line by line and computes metrics'''

import sys



file_list = []
status_list = []
counter = 1
total_size = 0

def ipCheck(ip):
    ip_list= ip.split('.')
    value = True
    for i in ip_list:
        if (int(i) < 0) or (int(i) > 255):
            value = False
    return value
    
try:
    for line in sys.stdin:
        line_list = line.split()
        ip = line_list[0]
        status_code = line_list[7]
        file_size = line_list[8]
        file_list.append(file_size)
        status_list.append(status_code)
        if (ipCheck(ip)):
            for size in file_list:
                total_size = total_size + int(size)
            if (counter % 10 == 0):
                print(f'File size: {total_size}')
            codeSet = set(status_list)
            codetuple = list(codeSet)
            codetuple.sort()
            for code in codetuple:
                number = status_list.count(code)
                if (counter % 10 == 0):
                    print(f'{code}: {number}')
        counter += 1

except KeyboardInterrupt:
    for size in file_list:
        total_size = total_size + int(size)
    print(f'File size: {total_size}')
    codeSet = set(status_list)
    codetuple = list(codeSet)
    codetuple.sort()
    for code in codetuple:
        number = status_list.count(code)
        print(f'{code}: {number}')
    # print(error)

