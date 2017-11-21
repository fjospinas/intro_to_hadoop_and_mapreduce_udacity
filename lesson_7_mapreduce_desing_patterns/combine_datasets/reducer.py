#!/usr/bin/python
# Here you will be able to combine the values that come from 2 sources
# Value that starts with A will be the user data
# Values that start with B will be forum node data

import sys
import csv


def reducer():
    reader = csv.reader(sys.stdin, delimiter='\t')
    writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

    actual_user = []

    for line in reader:
        if line[1] == 'A':
            actual_user = line
        elif line[1] == 'B':
            line_output = line[2:]
            line_output.insert(3, line[0])
            line_output += actual_user[2:]
            writer.writerow(line_output)


reducer()
