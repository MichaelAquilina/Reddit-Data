#! /usr/bin/python

import os

def search_files(path):
    for p1 in os.listdir(path):
        abs_path = os.path.join(path, p1)
        if os.path.isdir(abs_path):
            for p2 in search_files(abs_path):
                yield p2
        else:
            yield abs_path

if __name__ == '__main__':
    
    import sys

    path = ''
    if len(sys.argv) > 1:
        path = sys.argv[1]

    print path, len(list(search_files(path)))

