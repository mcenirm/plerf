#!/usr/bin/env python

from __future__ import print_function
import re
import sys


def sort_nicely(l):
    """ Sort the given list in the way that humans expect.
        cf http://blog.codinghorror.com/sorting-for-humans-natural-sort-order/
    """
    def convert(text):
        return int(text) if text.isdigit() else text

    def alphanum_key(key):
        return [convert(c) for c in re.split('([0-9]+)', key)]

    l.sort(key=alphanum_key)
    return l


for x in sort_nicely(list(sys.argv[1:])):
    print("""<img src='{0}'>""".format(x))
