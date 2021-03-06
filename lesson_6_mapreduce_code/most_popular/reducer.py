#!/usr/bin/python

import sys

countTotal = 0
oldKey = None
max_key =None
max_total = 0

# Loop around the data
# It will be in the format key\tval
# Where key is the store name, val is the sale amount
#
# All the sales for a particular store will be presented,
# then the key will change and we'll be dealing with the next store


for key in sys.stdin:
    thisKey = key.strip()
    if oldKey and oldKey != thisKey:
        if countTotal > max_total:
            max_key = oldKey
            max_total = countTotal
        oldKey = thisKey;
        countTotal = 0

    oldKey = thisKey
    countTotal += 1

if oldKey != None:
    if countTotal > max_total:
        max_key = oldKey
        max_total = countTotal


print '{key}\t{total}'.format(key=max_key, total=max_total)

