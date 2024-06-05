import csv
import random
import os

reader = 0

with open('Titanic.csv','r') as input:
    reader = list(csv.DictReader(input))


def show(type = 'top', n = 5 , separator = ','):
    print(*list(reader[0].keys()))

    if type == 'top':
        start = 0
    if type == 'bottom':
        start = len(reader) - n if (len(reader) - n)>=0 else 0
    if type == 'random':
        start = random.randint(0,len(reader))
    stop = start + n

    for i in range (start,stop):
        try:
            for el in reader[i].values():
                print(el+separator+' ', end = '')
            print('\n')
        except:
            print('no more lines')
            break

def str_type(n):
    try:
        n = int(n)
        return 'int'
    except ValueError:
        try:
            n = float(n)
            return 'float'
        except ValueError:
            return 'string'


def info():
    print(len(reader),'х',len(list(reader[0])),sep = '')
    keys = reader[0].keys()
    d = dict.fromkeys(keys,0)
    types = []
    for line in reader:
        for element in keys:
            if (line[element]!='') : 
                d[element]+=1

    for line in reader:
        if '' not in line.values():
            types = [str_type(element) for element in list(line.values())]
            break
    n = 0
    for k in keys:
        print(k,d[k],types[n])
        n+=1
    

def DelNaN():
    k = 0
    while k < len(reader):
        if '' in list(reader[k].values()): 
            del reader[k]
        else: k+=1
                

show('random',21,' ||')
info()



def MakeDS():
    random.shuffle(reader)
    lengh_A = int(len(reader)*0.7)
    arr_A = reader[:lengh_A]
    arr_B = reader[lengh_A:]
    try:
        os.mkdir('workdata')
    except: 
        pass
    try:
        os.mkdir('workdata\\learning')
    except:
        pass
    try: 
        os.mkdir('workdata\\testing')
    except:
        pass
    
    with open('workdata\\learning\\train.csv','w') as write:
        header = reader[0].keys()
        writer = csv.DictWriter(write,fieldnames=header)
        writer.writeheader()
        for line in arr_A:
            writer.writerow(line)

    with open('workdata\\testing\\test.csv','w') as write:
        header = reader[0].keys()
        writer = csv.DictWriter(write,fieldnames=header)
        writer.writeheader()
        for line in arr_B:
            writer.writerow(line)

MakeDS()