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
                print(li, step, i)
            i+=1
    return li
a = [999, 5, 6, 2, 33, 755, 42, 454, 324, 22, 2345, 3, 223, 43]
print(hairbrush(a))