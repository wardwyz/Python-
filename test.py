import inspect

def check(fn):
    def warpper(*args,**kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters #参数
        values = list(params.values()) #
        for i,p in enumerate(args):
            if isinstance(p,values[i].annotation):
                print('==')
        for k,v in kwargs.items():
            if isinstance(v,params[k].annotation):
                print('===')
        return fn(*args,**kwargs)
    return warpper

@check
def add(x,y:int=7)->int:
    return x+y
add(20,10)
add(20,y=10)
add(y=10,x=20)
