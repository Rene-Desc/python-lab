#task_1
def task_1():
    a,b,c = map(int,input().split())
    maxx = -10000000000
    if a>b and a>c:
        maxx = a
    elif b>c:
        maxx = b
    else:
        maxx = c

    minn = 10000000000
    if a<b and a<c:
        minn = a
    elif b<c:
        minn = b
    else:
        minn = c

    print(maxx,minn)

#task_2
def task_2():
    n = int(input())
    for i in range(n):
        a =''.join( [str(e) for e in range(1,n-i+1)])
        print(a)

#task_3
def task_3():
    n = int(input())
    middle = sum([len(str(j)) for j in range(n,0,-1)])
    for i in range(n):
        a = ''.join([str(j) for j in range(n-i,0,-1)])
        tab = middle - len(a)
        b = a[::-1][1::]
        ans_str = ' '*tab + ''.join(a+b)
        

        print(ans_str)


task_1()
task_2()
task_3()