#-------------------------------------------------------------------------------
# Name:        模块1
# Purpose:
#
# Author:      urey
#
# Created:     10/10/2012
# Copyright:   (c) urey 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def hsitogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0)+1
    print d

def main():
    s = raw_input('input string')
    hsitogram(s)

if __name__ == '__main__':
    main()
