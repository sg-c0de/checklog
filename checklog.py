#!/usr/bin/env python

from collections import defaultdict
import re

filename = 'events.log'
pattern = re.compile('\[(\d{4}-\d{2}-\d{2} +\d{2}:\d{2}).+\]')
date_counter = defaultdict(int)

with open(filename) as file:
    for line in file:
        if 'NOK' not in line:
            continue

        match = pattern.search(line)
        if match:
            date_str = match.group(1)
            date_counter[date_str] += 1

for k, v in date_counter.items():
    print(f'[{k}] {v}')
