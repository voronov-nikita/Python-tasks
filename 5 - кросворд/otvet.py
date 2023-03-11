import itertools as it


def function1(ls):
    otvet = []
    for cols in range(len(ls) // 2):
        otv1 = []
        otv2 = []
        for rows in range(len(ls) // 2):
            otv1.append(ls[cols][rows])
            otv2.append(ls[rows][cols])
        otvet.append(''.join(otv1))
        otvet.append(''.join(otv2))
    return otvet


def function2(ls):
    for i in range(len(ls)):
        ls[i] = ''.join(ls[i])
    return ls


t = int(input())
ls = []

for _ in range(t):
    otv = []
    n = int(input())
    for i in range(2 * n):
        otv2 = []
        for g in input():
            otv2.append(g)
        otv.append(otv2)
    ls.append(otv)

for elem in ls:
    tf = False
    for g in it.permutations(elem):
        otv=[]
        for i in set(function1(g)):
            if i not in function2(elem):
                break
            otv.append(i)
        if not(tf) and len(otv)==len(elem):
            for i in range(0, len(otv), 2):
                print(otv[i])
            tf = True
    if ls[ls.index(elem)] != ls[-1]:
        print()
