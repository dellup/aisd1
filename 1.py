from random import *
from timeit import timeit
def hairbrush(li):
    n = len(li)
    step = n
    while step > 1 or flag:
        if step > 1:
            step = int(step / 1.247331)
        flag = False
        i = 0
        while i + step < n:
            if li[i] > li[i + step]:
                li[i], li[i + step] = li[i + step], li[i]
                flag = True
            i+=1
    return li
a = [randint(1, 10000) for i in range(50)]
print("Массив до сортировки: " + a)
print("Массив после сортировки: " + hairbrush(a))
time = timeit(hairbrush, number=1)
print("Время выполнения = "+time)
