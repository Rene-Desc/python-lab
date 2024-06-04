import re
def task1():
    import math
    f_in = open('input.txt')
    f_out = open('output.txt','w')
    f_out.write(str(math.prod([int(i) for i in f_in.read().split()])))

def task2():
    import re
    f_in = open('input.txt')
    f_out = open('output.txt','w')
    arr = sorted([re.sub("\n",'',line)[::-1] for line in f_in])
    arr = [element[::-1] for element in arr]
    for elelment in arr:
        f_out.write(elelment+' ')

def task3():
    f_in = open('input.txt')
    f_out = open('output.txt','w')

    maxx = ('',-1)
    minnimum = ('',999)
    for element in f_in:

        for j in range(len(element)):
            if '0'<=element[j]<='9':
                age = int(element[j:])

                maxx = (element[:j],age) if age > maxx[1] else maxx
            
                minnimum = (element[:j],age) if age < minnimum[1] else minnimum
                break

    f_out.write(''.join(map(str,maxx))+' ')
    f_out.write(''.join(map(str,minnimum)))

def task4():
    import json
    import pandas
    name = input()
    with open(name, 'r') as j:
        js_data = json.loads(j.read())
        
    json_data = pandas.DataFrame(js_data)
    json_data.to_csv(name[:-4]+'.csv')