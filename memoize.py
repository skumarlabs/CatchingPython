from functools import wraps


def memoize(fn):
    cache = dict()

    @wraps(fn)
    def inner(n):
        if n not in cache:
            cache[n] = fn(n)

        return cache[n]

    return inner


@memoize
def fib(n):
    print("calling fn with {}".format(n))
    return 1 if n < 3 else fib(n - 1) + fib(n - 2)


print(fib(10))
print(fib(12))
