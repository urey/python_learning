


def has_no_chr(s, e):
    flag = True
    for c in s:
        if c == e:
            flag = False
    return flag

def avoids(s, le):
    for i in range(len(le)):
        if not has_no_chr(s, le[i]):
            return False
    return True

def uses_only(s, le):
    for c in s:
        flag = False
        for e in le:
            if c == e:
                flag = True
        if not flag:
            return False
    return True

def uses_only_all(s, le):
    if uses_only(s, le) and uses_only(le, s):
        return True
    else:
        return False

def uses_all(s, le):
    return uses_only(le, s)
    
def is_abece(s):
    for i in range(len(s)-1):
        if s[i]>s[i+1]:
            return False
    return True

def tridou(s):
    if len(s)<6:
        return False
    else:
        if s[0]==s[1] and s[2]==s[3] and s[4] == s[5]:
            return True
        else:
            return tridou(s[1:])
            
def is_triple_double(word):
    """Tests if a word contains three consecutive double letters."""
    i = 0
    count = 0
    while i < len(word)-1:
        if word[i] == word[i+1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            count = 0
            i = i + 1
    return False      
#print uses_only('apple', 'apl')

fin = open("E:\\python learning\\words.txt")
num_no_avo = 0
num = 1
#avo = raw_input('uses_all: ')
line = fin.readline()
while(len(line)):
    string = line.strip()
    if is_triple_double(string):
        print string
        num_no_avo+=1
    line = fin.readline()
    num+=2
print num_no_avo, num, float(num_no_avo)/float(num)
