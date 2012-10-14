import math

def check_fermat(a,b,c,n):
    if(math.pow(a,n)+math.pow(b,n)==math.pow(c,n)):
        print 'fermat was wrong'
    else:
        print 'no, that doesn\'t work'

check_fermat(3,3,3,5)

