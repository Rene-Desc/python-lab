def factorial(n):
    ans = 1
    for i in range(1,n+1):
        ans *= i
    return ans

#task_1
def task_1():
    n = int(input())
    stroki = []
    for i in range(n):
        arr = ' '.join([str(factorial(i)//(factorial(j)*factorial(i-j))) for j in range(i+1)])
        stroki.append(arr)
        #print(arr)

    midlle = (len(stroki[-1]))//2

    for i in range(n):
        middle_i = len(stroki[i])//2
        print(' '*(midlle - middle_i)+ stroki[i])

#task_2
def task_2(t):
    n = 2**t
    stroki = []
    for i in range(n):
        arr = ' '.join([str(factorial(i)//(factorial(j)*factorial(i-j))) for j in range(i+1)])
        stroki.append(arr)
        #print(arr)

    st_tr = []
    for i in range(n):
        integer_tr = [int(j) for j in stroki[i].split()]
        st = ''
        for k in range(len(integer_tr)):
            if (integer_tr[k])%2 == 0: st+=' '
            else: st+='*'
        st_tr.append(st)

    midlle_st = (len(st_tr[-1]))//2
    #print(st_tr)

    for i in range(n):
        middle_st_i = len(st_tr[i])//2
        print(' '*(midlle_st - middle_st_i)+ st_tr[i])



task_2(4)



