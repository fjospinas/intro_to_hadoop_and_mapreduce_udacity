#!/usr/bin/python

import sys


def reducer():
    count_total = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            # Something has gone wrong. Skip this line.
            continue

        this_key, this_count = data
        if old_key and old_key != this_key:
            print old_key, "\t", count_total
            old_key = this_key
            count_total = 0

        old_key = this_key
        count_total += float(this_count)

    if old_key != None:
        print old_key, "\t", count_total


reducer()
