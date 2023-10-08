from random import *
from timeit import timeit
a = [randint(1, 10000) for i in range(50)]
b=a.copy()
def hairbrush(a):
	n = len(a)
	step = n
	while step > 1 or flag:
		if step > 1:
			step = int(step / 1.247331)
		flag = False
		i = 0
		while i + step < n:
			if a[i] > a[i + step]:
				a[i], a[i + step] = a[i + step], a[i]
				flag = True
			i+=1
	return a

test="""
from random import randint
a = [randint(1, 10000) for i in range(50)]
n = len(a)
step = n
while step > 1 or flag:
    if step > 1:
        step = int(step / 1.247331)
    flag = False
    i = 0
    while i + step < n:
        if a[i] > a[i + step]:
            a[i], a[i + step] = a[i + step], a[i]
            flag = True
        i+=1
"""

print("Массив до сортировки: ",  b)
print("Массив после сортировки: ", hairbrush(b))
timre = timeit(test, number=1)
print("Время выполнения = ", timre)
