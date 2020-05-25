# 打印树

# 居中对齐方案
import math

def print_tree(array,unit_width=2):
    length = len(array)
    depth = math.ceil(math.log2(length+1))

    index = 0

    width = 2 ** depth - 1
    for i in range(depth):
        for j in range(2**i):
            print('{:^{}}'.format(array[index],width*unit_width),end=' ' * unit_width)
            index += 1
            if index >= length:
                break

        width = width // 2
        print()

print_tree([x + 1 for x in range(29)])

# 投影栅格方案

import math

def print_tree(array):
    