#!/usr/bin/env python
__author__ = 'applicant'
import sys
from sortedcontainers import SortedSet

def reduce(stdin):
    current_key = None
    neighbors = SortedSet()

    for line in stdin:
        #bye bye whitespace
        line = line.strip()
        # parse the mapper input
        key, friend = line.split('\t', 1)
        if current_key == key:
            neighbors.add(friend)
        else:
            if current_key:
                yield '%s\t%s' % (current_key, '\t'.join(neighbors))
                neighbors = SortedSet()
            current_key = key
            neighbors.add(friend)
    #make sure to include the last entry
    yield '%s\t%s' % (current_key, '\t'.join(neighbors))

if __name__ == '__main__':
    for output in reduce(sys.stdin):
        print output









