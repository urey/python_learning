

def is_reversed(i, j):
    k = str(i).zfill(2)
    t = str(j).zfill(2)
    k = k[::-1]
    if k == t:
        return True
    else:
        return False

def cartalk_age():
    for i in range(10, 50):
        k = 0
        t = i
        count = 0
        while t<= 99:
            if is_reversed(k, t):
                count+=1
            k+=1
            t+=1
        print i, count


cartalk_age()
