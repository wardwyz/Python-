import inspect
def check(fn):
    def wrapper(*args, **kwargs):
        sig = inspect.signature(fn)
        params = sig.parameters
        values = list(params.values())
        for i,p in enumerate(args):
            param = values[i]
            if param.annotation is not param.empty and not isinstance(p, param.annotation):
                print(p,'!==',values[i].annotation)
        for k,v in kwargs.items():
            if params[k].annotation is not inspect._empty and not isinstance(v, params[k].annotation):
                print(k,v,'!===',params[k].annotation)
        return fn(*args, **kwargs)
    return wrapper
@check
def add(x, y:int=7) -> int:
    return x + y

print(add(20,10))