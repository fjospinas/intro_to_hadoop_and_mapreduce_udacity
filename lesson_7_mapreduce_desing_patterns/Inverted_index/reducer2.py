#!/usr/bin/python

import sys


def reducer():

    list_lines = []

    for line in sys.stdin:
        list_lines.append(int(line))
    list_lines.sort()
    print(', '.join(map(str, list_lines)))


reducer()
