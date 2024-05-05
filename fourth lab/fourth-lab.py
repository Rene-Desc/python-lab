def task_1():
    pre_arr = input()[:-1]+ ','
    arr = [str(i) for i in pre_arr.split()]
    sett = set(arr)
    print(len(sett))


def task_2():
    A = {int(i) for i in input().split()}
    B = {int(i) for i in input().split()}
    print(A<=B)


def task_3():
    n = int(input())
    citys = set()
    i = 1
    while i<=n:
        city = input()
        if city not in citys:
            citys.add(city)
            print("OK")
        else:
            print("REPEAT")
        i+=1

def task_4():
    words = input().split()
    d = {word:0 for word in words}
    for i in words:
        print(d[i], end = ' ')
        d[i] += 1


def task_5():
    n = int(input())
    arr = []
    for i in range(n):
        Id,obj,count = input().split()
        arr.append((int(Id),obj,int(count)))
    dictt = {Id[0]:dict() for Id in arr}

    ans = dictt.copy()
    for i in range(n):
        ans[arr[i][0]].update({arr[i][1]:0})

    for i in range(n):
        ans[arr[i][0]][arr[i][1]] += arr[i][2]


    print(ans)

def bubble_sort_for_task_6(b):
    for i in range(len(b)):
        for j in range(len(b)-1,0,-1):
            if(b[j][1]>b[j-1][1]):
                b[j],b[j-1] = b[j-1],b[j]
            
            if b[j][1]==b[j-1][1]:
                if b[j][0]<b[j-1][0]:
                    b[j],b[j-1] = b[j-1],b[j]
    return b
            
def task_6():
    arr = input().split()
    dictt = dict.fromkeys(arr,0)
    for i in arr:
        dictt[i]+=1
    
    ans = bubble_sort_for_task_6(list(dictt.items()))


    for i in range(len(ans)):
        print(ans[i][0], end = ' ')