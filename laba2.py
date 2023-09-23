#O(3n)
n = 4
a = 0
for i in range(n):
    a+=1
for i in range(n):
    a+=1
for i in range(n):
    a+=1

#O(n^3)
a = 0
for i in range(n):
    for j in range(n):
        for k in range(n):
            a+=1
#O(3(log(n)))
num = 0 #берем число, чтобы длительность исполнения алгоритма была максимально возможной
a = [x for x in range(2**23)]
while len(a) > 0:
    middle = len(a) // 2
    if a[middle] == num:
        break
    elif a[middle] < num:
        a = a[middle+1:]
    else:
        a = a[:middle]
a = [x for x in range(2**23)]
while len(a) > 0:
    middle = len(a) // 2
    if a[middle] == num:
        break
    elif a[middle] < num:
        a = a[middle+1:]
    else:
        a = a[:middle]
a = [x for x in range(2**23)]
while len(a) > 0:
    middle = len(a) // 2
    if a[middle] == num:
        break
    elif a[middle] < num:
        a = a[middle+1:]
    else:
        a = a[:middle]




