#!/usr/bin/python
import sys


def reducer():
    sales_total = 0
    old_key = None

    for line in sys.stdin:
        data = line.strip().split("\t")
        if len(data) != 2:
            # Something has gone wrong. Skip this line.
            continue

        this_key, this_sale = data
        if old_key and old_key != this_key:
            print old_key, "\t", sales_total
            old_key = this_key
            sales_total = 0

        old_key = this_key
        sales_total += float(this_sale)

    if old_key != None:
        print old_key, "\t", sales_total


reducer()

