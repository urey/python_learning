#-------------------------------------------------------------------------------
# Name:        word count
# Purpose:
#
# Author:      urey
#
# Created:     11/10/2012
# Copyright:   (c) urey 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import string

def num_dict(dic):
    num = dict()
    for key in dic:
        val = dic[key]
        if val not in num:
            num[val] = [key]
        else:
            num[val].append(key)
    print num


def main():
    fin = open("E:\\python learning\\PRIDE AND PREJUDICE.txt")
    line = fin.readline()
    dic = dict()
    num = dict()
    while(len(line)):
        stri = line.strip()
        if len(stri) == 0:
            line = fin.readline()
            continue
        for c in string.punctuation:
            stri = stri.replace(c, '')
        words = stri.split(' ')
        for w in words:
            if len(w) == 0:
                continue
            dic[w] = dic.get(w, 0)+1
        line = fin.readline()
    print dic
    num_dict(dic)
    print len(dic)

if __name__ == '__main__':
    main()
