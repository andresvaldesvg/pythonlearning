#!/usr/bin/env python3

import sys

def hello(name):
    print("Hello {}".format(name))

name = "Andres"
if len(sys.argv)> 1:
    name = sys.argv[1]

if __name__=="__main__":
    hello(name)
