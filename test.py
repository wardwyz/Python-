def counter(base):
    def inc(step = 1):
        nonlocal base
        base += step
        return base
    return inc

foo1 = counter(10)
print(foo1())
foo2 = counter(10)
print(foo2())
print(foo1 == foo2)
