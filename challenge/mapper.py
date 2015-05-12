#!/usr/bin/env python
__author__ = 'applicant'
import sys
import itertools

def friend_permutations(friends):
    for p in itertools.permutations(friends):
        i = iter(p)
        yield zip(i,i)[0]

def map(stdin):
    for line in stdin:
        #bye bye whitespace
        line = line.strip()
        for pair in friend_permutations(line.split('\t')):
            #output edges
            yield '%s\t%s' % (pair[0], pair[1])

if __name__ == '__main__':
    for output in map(sys.stdin):
        print output

