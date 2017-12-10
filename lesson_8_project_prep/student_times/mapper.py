#!/usr/bin/python

import sys
import csv
from datetime import datetime as dt


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:

        if len(line) == 19:

            user, time_str = [line[3], line[8]]

            if time_str != 'added_at':

                if time_str.find('+') > 0:
                    time_str = time_str[:time_str.find('.')]

                time_obj = dt.strptime(time_str, '%Y-%m-%d %H:%M:%S')
                hour = str(time_obj.hour)

                print '{0}\t{1}\t1'.format(user, '0' + hour if time_obj.hour < 10 else hour)


mapper()
