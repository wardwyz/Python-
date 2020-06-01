

def logger(fn):
    def _logger(*args,**kwarg):
        print('begin')
        ret = fn(*args,**kwarg)
        print('end')
        return ret
    return _logger

@logger
def add(x,y):
    return x+y

print(add(4,5))