#!/usr/bin/python
import sys
import re
import csv


def mapper():

    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:
        if len(line) >= 5:
            words = re.split(r'\.|,|!| |\?|:|;|\"|\(|\)|<|>|\[|\]|#|\$|=|-|\/', line[4])
            for word in words:
                print('{}\t{}'.format(word, 1))


mapper()
