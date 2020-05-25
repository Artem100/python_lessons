"""

1. Реализовать все декораторы - таймер, запоминатель, счетчик вызовов и единичный вызов
2. Реализовать примеры с functools - wraps и singledispatch
3. Реализовать свой lru_cache (описание в конце презентации)

"""

import time

def timer(f):
    def tmp(a, b, c):
        t = time.time()
        res = f(a, b, c)
        print('Execution time: {}'.format(time.time() - t))
        return res
    return tmp

def memorize(f):
    cache = {}
    def decorate(*args):
        print(args)
        if args not in cache:
            print('args not in cache')
            cache[args] = f(*args)
        return cache[args]
    return decorate

@timer
@memorize
def func(x, y, z):
    l = [x, y, z]
    for i in l:
        i = i * 2
        print(i)

# print("1")
# func(0, 10_000_000, 10)
# print("2")
# func(0, 10_000_000, 10)
# print("3")
# func(0, 10_000_000, 10)
# print("4")
# func(0, 10_000_000, 10)

###########

# Счетчик вызовов

def profiled(func):
    def inner(*args, **kwargs):
        inner.calls += 1
        return func(*args, **kwargs)
    inner.calls = 0
    return inner

@profiled
def identity(x):
    return x

# identity(10)
# print(identity.calls)
# identity(20)
# print(identity.calls)

###

def once(func):
    def inner(*args, **kwargs):
        if not inner.called:
            print('really doing init')
            func(*args, **kwargs)
            inner.called = True
        else:
            print('not first init')
    inner.called = False
    return inner

@once
def do_init():
    print('doing init')


do_init()
do_init()
do_init()
do_init()