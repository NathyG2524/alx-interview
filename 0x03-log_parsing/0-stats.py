#!/usr/bin/python3
from distutils.log import error
from ipaddress import ip_address
import sys
import fileinput


if __name__ == "__main__":
    file_list = []
    status_list =[]
    counter = 0
    total_size = 0

    try:
        for line in fileinput.input():
        # counter += 1
        
            line_list = line.split()
            ip = line_list[0]
            status_code = line_list[7]
            file_size = line_list[8]
            file_list.append(file_size)
            status_list.append(status_code)
            # print(counter)
        
            
            for size in file_list:
                total_size = total_size + int(size)
            if (counter % 10 == 0):
                print(f'File size: {total_size}')

            codeSet = set(status_list)
            # print(codeSet)
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
        # print(codeSet)
        codetuple = list(codeSet)
        codetuple.sort()
        for code in codetuple:
            number = status_list.count(code)
            
            print(f'{code}: {number}')
        print(error)
            
# ip_address = f'{sys.argv[0]}.{sys.argv[1]}.{sys.argv[2]}.{sys.argv[3]}'
# date = sys.argv[0]
# status_code = sys.argv[0]
# file_size = sys.argv[0]



