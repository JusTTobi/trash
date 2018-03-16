import time
def my_decorator(func):
    def wrap(*a, **b):
        print('Функция ' + func.__name__ + ' начала работу!')
        t=time.clock()
        res = func(*a, **b)
        print('Функция ' + func.__name__ + ' закончила работу через ' +str(time.clock() - t))
        return res
    return wrap

@my_decorator
def progress2(start, n, step):
    i = 1
    while i < n:
        start+=step
        i+=1
    return start

print(progress2(2, 100000, 2))

