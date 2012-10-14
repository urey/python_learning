

fin = open("E:\\python learning\\words.txt")
mydic = dict()
num = 1
#avo = raw_input('uses_all: ')
line = fin.readline()
while(len(line)):
    string = line.strip()
    mydic[num] = string
    line = fin.readline()
    num+=1
    print mydic
    raw_input('press enter to continue...')
    
    
