#注册函数
def reg(cmd):
    def _reg(fn):
        cmd_tbl[cmd] = fn
        return fn
    return _reg

#自定义函数
@reg('war')
def foo1():
    print('ward')

@reg('py')
def foo2():
    print('python')

def command_dispatcher():
    cmd_tbl = {} #构建全局函数

    #注册函数
    def reg(fn):
        def _reg(fn):
            cmd_tbl[cmd] = fn
            return fn
        return _reg

    #缺省函数
    def default_func():
        print('Unknown command')

    #调度器
    def dispatcher():
        while True:
            cmd = input('>>>')
            if cmd.strip() == '':
                return
            cmd_tbl.get(cmd,default_func)()
    return reg,dispatcher

reg,dispatcher = command_dispatcher()

@reg('war')
def foo1():
    print('ward')

@reg('py')
def foo2():
    print('python')

dispatcher()