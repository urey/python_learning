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

def fibonacci(n):
    l = [1,1]
    for i in range(2,n):
        l.append(l[i-1]+l[i-2])
        print l[i]
    print l[n-1]




def main():
    fibonacci(100)

if __name__ == '__main__':
    main()
