def task_1():
    strr = input()
    el = strr[0]
    words = []
    for i in strr[1:]:
        if i == el[-1]:
            el+=i
        else:
            words.append(el)
            el = i
    words.append(el)
    ans_numbers = [str(len(element)) for element in words]
    ans = ''.join([words[i][0]+ans_numbers[i] for i in range(len(words))])
    print(ans)

def task_2():
    strr = input()

    numbers_strr = list(strr)
    for i in range(len(strr)):
        if not(strr[i].isdigit()):
            numbers_strr[i] = ' '
    numbers_strr = ''.join(numbers_strr)
    numbers = [int(el) for el in numbers_strr.split()]

    words_strr = list(strr)
    for i in range(len(strr)):
        if (strr[i].isdigit()):
            words_strr[i] = ' '
    words_strr = ''.join(words_strr)
    words = [el for el in words_strr.split()]

    ans = ''.join(words[i]*numbers[i] for i in range(len(words)))
    
    print(ans)

def task_3():
    numbers = {'0':'','1':'один','2':'два','3':'три','4':'четыре','5':'пять','6':'шесть','7':'семь','8':'восемь','9':'девять'}
    numbers_hundred = {'1':'сто','2':'двести','3':'триста','4':'четыреста','5':'пятьсот','6':'шестьсот','7':'семьсот','8':'восемьсот','9':'девятьсот'}
    numbers_11_19 = {'0':'','11':'одиннадцать','12':'двенадцать','13':'тринадцать','14':'четырнадцать','15':'пятьнадцать','16':'шестнадцать','17':'семнадцать','18':'восемнадцать','19':'девятнадцать'}
    numbers_decades = {'0':'','1':'десять','2':'двадцать','3':'тридцать','4':'сорок','5':'пятьдесят','6':'шестьдесят','7':'семьдесят','8':'восемьдесят','9':'девяносто'}
    n = input()
    k = len(n)
    ans = ''
    for el in n:
        if k == 4:
            print('одна тысяча')
            break
        elif k == 3:
            ans += (numbers_hundred[n[-k]]) + ' '
        elif k == 2:
            if 11<=int(n[-k]+n[-k+1])<=19:
                ans += (numbers_11_19[n[-k]+n[-k+1]]) + ' '
                break
            else:
                ans+=(numbers_decades[n[-k]])+ ' '
        elif k == 1:
            ans+=(numbers[n[-k]])
        k-=1
    print(ans)

def task_4():
    arr = ['abc', 'bcd', 'abc', 'abd', 'abd', 'dcd', 'abc']
    dict_ans  = {b:0 for b in arr}
    for element in arr:
        dict_ans[element]+=1
    ans = [b[1] for b in dict_ans.items()]
    print(*ans)

def task_5():
    b = [
        [10,20,30],
        [40,50,60],
        [70,80,80]
    ]

    if(b[0][0]*b[1][1]*b[2][2] - b[0][0]*b[1][2]*b[2][1] - b[0][1]*b[1][0]*b[2][2] + b[0][1]*b[1][2]*b[2][0] + b[0][2]*b[1][0]*b[2][1] - b[0][2]*b[1][1]*b[2][0]) == 0:
        print("Столбцы линейно зависимы")
    else:
        print("Столбцы линейно независимы")

    for i in range(3):
        print(*b[i])


def task_6():
    strr = input()
    strr = ''.join([i[0].upper() for i in strr.split()])
    print(strr)


task_6()