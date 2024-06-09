import numpy as np
def task_1():
    mt = []
    reader = []

    with open('input.txt') as input:
        for i in range (6):
            reader = (input.readline().strip().split(','))
            if i > 2:
                reader = [int(s) for s in reader]
                mt.append(reader)

    print(np.sum(mt) , np.max(mt), np.min(mt))


def task_2():
    arr = np.array([int(q) for q in input().split()])
    arr1 =[arr[0]]
    arr2 = []

    cnt = 1
    for i in range(1,len(arr)): 
        if arr[i]!= arr1[-1]:
            arr1.append(arr[i])
            arr2.append(cnt)
            cnt = 0
        cnt+=1
    arr2.append(cnt)


    print(arr1,arr2)



def task_3():
    arr = np.random.normal(size=(10,4))
    print(arr,'\n',np.min(arr),np.max(arr),np.mean(arr),np.std(arr))



def task_4():
    arr = [int(q) for q in input().split()]
    maxx = -99999999
    for i in range(1,len(arr)):
        if arr[i-1] == 0 and arr[i]> maxx:
            maxx = arr[i]
    print(maxx)



def task_5():
    m = (1,2)
    cov1 = [float(k) for k in input().split()]
    cov = np.array(cov1).reshape(len(m),len(m))
    arr = np.random.multivariate_normal(m, cov, size=(1,1))
    print(np.log(arr)) 



def task_6():
    a = np.arange(16).reshape(4,4)
    str1=np.array(a[0,:])
    str2=a[2,:]
    a[0,:] = str2
    a[2,:] = str1
    print(a)




def task_7():
    url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
    iris = np.genfromtxt(url, delimiter=',', dtype='object')
    species = np.array(iris[:,4])
    print(np.unique(species,return_counts=True))

def task_8():
    arr = [int(element) for element in input().split(',')]
    arr2 = [w for w in range(len(arr)) if arr[w]]
    print(arr2)
