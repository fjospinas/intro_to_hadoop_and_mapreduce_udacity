#!/usr/bin/python

import sys


def get_max(dic):
    vals = [value for key, value in dic.items()]
    max_val = max(vals)
    key_max = [key for key, value in dic.items() if value == max_val]
    return key_max


def reducer():

    actual_user = None
    dict_hours = {}

    for line_act in sys.stdin:
        line = line_act.strip().split("\t")

        if actual_user and line[0] != actual_user:

            key_max = get_max(dict_hours)
            for key in key_max:
                print '{0}\t{1}'.format(actual_user, key)

            actual_user = line[0]
            dict_hours = {}

        actual_user = line[0]
        if line[1] in dict_hours:
            dict_hours[line[1]] = dict_hours[line[1]] + 1
        else:
            dict_hours[line[1]] = 1

    if actual_user != None:
        key_max = get_max(dict_hours)
        for key in key_max:
            print '{0}\t{1}'.format(actual_user, key)


reducer()
