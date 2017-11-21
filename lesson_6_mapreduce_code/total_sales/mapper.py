#!/usr/bin/python
import sys


def mapper():

    for line in sys.stdin:

        data = line.strip().split('\t')

        if len(data) == 6:

            date, time, store, item, cost, payment = data

            print '{0}\t{1}'.format('Sales', 1)
            print '{0}\t{1}'.format('Total_value', cost)


mapper()
