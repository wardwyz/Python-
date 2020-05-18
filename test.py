source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
target = {}
def flatmap(src,prefix=''):
    for k,v in src.items():
        if isinstance(v,(list,tuple,set,dict)):
            flatmap(v,prefix=prefix+k+'.')
        else:
            target[prefix+k] = v

flatmap(source)
print(target)
            
