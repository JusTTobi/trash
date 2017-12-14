def factor(x):
    if x == 1:
        return x
    return x*factor(x-1)

print(factor(3))

def progress(start, n, step):
    if n == 1:
        return start
    return progress(start, n-1, step) + step


def progress2(start, n, step):
    i = 1
    while i < n:
        start+=step
        i+=1
    return start

print(progress(2, 5, 2))

#print(progress(2, 10000, 2))

L=[1, [2, (1, (2, 3))], [1, (4, 10)]]
#print(sum(L))

def sum_lt(L):
    s = 0
    for i in L:
        if not (type(i) == list or type(i) == tuple):
            s+=i
        else:
            s+=sum_lt(i)
    return s

print(sum_lt(L))

input()
