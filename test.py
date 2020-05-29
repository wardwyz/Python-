import math

def print_tree(array):
    index = 1
    depth = math.ceil(math.log2(len(array))) 
    #前补零，若不 math.ceil(math.log2(len(array)+1))
    sep = '  '
    for i in range(depth):
        offset = 2**i #步长
        print(sep * (2**(depth -i -1)-1),end='') #end切换默认/n
        line = array[index:index+ offset] #切片
        for j,x in enumerate(line):
            print('{:>{}}'.format(x,len(sep)),end='')
            interval = 0 if i == 0 else 2**(depth-i)-1 #判断是否是第0行
            if j <len(line)-1: #判断是否是最后一个元素
                print(sep * interval,end='')

        index += offset #索引修正
        print()

origin = [0,30,20,80,40,50,10,60,70,90]

total = len(origin)-1
print(origin)
print_tree(origin)
print('*'*50)

def heap_adjust(n,i,array:list):#参数注解
    '''
    调整当前节点（核心算法）

    调整的结点的起点在n//2,保证所有的调整的结点都有孩子结点
    param n: 待比较数个数
    param i:当前节点下标
    param array:待排序数据
    return: None
    '''
    while 2*i <= n:
        #孩子节点：判断2i为左孩子，2i+1为右孩子
        lchile_index = 2*i #左孩子
        max_child_index = lchile_index #假定左孩子为最大索引
        if n> lchile_index and array[lchile_index + 1] > array[lchile_index]:#说明有右孩子
            max_child_index = lchile_index + 1
        
        #和子树的根结点比较
        if array[max_child_index] > array[i]:
            array[i],array[max_child_index] = array[max_child_index],array[i]#交换
            i = max_child_index #索引交换，循环看是否还有子节点
        else:
            break

def max_heap(total,array:list):
    for i in range(total//2,0,-1):
        heap_adjust(total,i,array)
    return array

print_tree(max_heap(total,origin))
print('*'*50)

def sort(total,array:list):
    while total >1:
        array[1],array[total] =  array[total],array[1]
        total -= 1
        if total == 2 and array[total] >= array[total-1]:
            break
        heap_adjust(total,1,array)
    return array

print_tree(sort(total,origin))
print(origin)



