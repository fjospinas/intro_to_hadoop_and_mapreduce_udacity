#!/usr/bin/python

import sys
import csv


def reducer():

    actual_parent_id = None
    question_length = None
    cumulate_answers = 0.0
    total_answers = 0

    reader = csv.reader(sys.stdin, delimiter='\t')

    for line in reader:

        id_node, type_node, post_l = line

        if actual_parent_id and id_node != actual_parent_id:

            avg = cumulate_answers / total_answers if total_answers != 0 else 0
            print '{0}\t{1}\t{2}'.format(actual_parent_id, question_length, avg)
            cumulate_answers = total_answers = 0

        if type_node == 'A':

            actual_parent_id = id_node
            question_length = post_l

        elif type_node == 'B':
            cumulate_answers += float(post_l)
            total_answers += 1

    if actual_parent_id is not None:
        avg = cumulate_answers / total_answers if total_answers != 0 else 0
        print '{0}\t{1}\t{2}'.format(actual_parent_id, question_length, avg)


if __name__ == "__main__":
    reducer()
