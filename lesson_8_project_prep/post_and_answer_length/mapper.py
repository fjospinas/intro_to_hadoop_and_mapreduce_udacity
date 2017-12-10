#!/usr/bin/python

import sys
import csv
from datetime import datetime as dt


def mapper():
    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:

        if len(line) == 19:

            id_node, body, type_node, parent_id = [line[0], line[4], line[5], line[6]]

            str_print = '{0}\t{1}\t{2}'

            if type_node == 'question':
                str_print = str_print.format(id_node, 'A', len(body))
            elif type_node == 'answer':
                str_print = str_print.format(parent_id, 'B', len(body))
            else:
                continue

            print str_print


if __name__ == "__main__":
    mapper()
