#!/usr/bin/python
import sys
import re
import csv


def mapper():

    reader = csv.reader(sys.stdin, delimiter='\t')

    patt = re.compile('fantastically|FANTASTICALLY')

    for line in reader:
        if len(line) >= 5:
            if patt.search(line[4]):
                print('{}'.format(line[0]))


mapper()
