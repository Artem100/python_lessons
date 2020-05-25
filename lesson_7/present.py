import time

def timer(f):
    def tmp(*args):
        t = time.time()
        res = f(*args)
        print('Execution time: {}'.format(time.time() - t))
        return res
    return tmp

def memorize(f):
    cache = {}
    def decorate(*args):
        #print(args)
        if args not in cache:
            print('args not in cache')
            cache[args] = f(*args)
            print(cache)
        return cache[args]
    return decorate

@timer
@memorize
def long_story(x, y):
    l = []
    for i in range(y):
        l.append(x)

print("1")
long_story(0, 10_000_000)
print("2")
long_story(0, 10_000_000)

