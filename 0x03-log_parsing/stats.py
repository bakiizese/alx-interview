#!/usr/bin/python3
''' parsing '''
import sys
import re


pattern1 = r'"GET \/projects\/260 HTTP\/1.1" \d{3} (\d{3})'
pattern2 = r'"GET \/projects\/260 HTTP\/1.1" (\d{3})'
chech = r'^(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}) - \[([^\]]+)\] "GET \/projects\/260 HTTP\/1\.1" (\d{3}) (\d+)$'

count = 0
ls1 = []
ls2 = []
file_size = 0
for line in sys.stdin:
    form = re.match(chech, line)
    if not form:
        continue
    line2 = line
    match1 = re.search(pattern1, line.strip(), re.DOTALL)
    match2 = re.search(pattern2, line2.strip(), re.DOTALL)
    count += 1
    if match1:
        ls1.append(match1.group(1))
    if match2:
        ls2.append(match2.group(1))
    if count == 10:
        file_size = sum(map(int, ls1))
        count = 0
        print(f'File size: {file_size}')
        dic = {}
        for i in sorted(ls2):
            dic[i] = ls2.count(i)
        for key, val in dic.items():
            print(f'{key}: {val}')
        file_size = 0
