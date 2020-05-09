# Python学习笔记

## Linux环境搭建

- 安装git

```shell
yum install git -y
```

- 安装python依赖环境

```shell
 yum -y install gcc make patch gdbm-devel openssl-devel sqlite-devel
readline-devel zlib-devel bzip2-devel
```

- 创建python账户

```shell
 useradd python
```

- python账户下安装pyenv

```shell
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenvinstaller | bash            获取脚本
```

```shell
#脚本内容
#!/usr/bin/env bash

set -e
[ -n "$PYENV_DEBUG" ] && set -x

if [ -z "$PYENV_ROOT" ]; then
  PYENV_ROOT="${HOME}/.pyenv"
fi

colorize() {
  if [ -t 1 ]; then printf "\e[%sm%s\e[m" "$1" "$2"
  else echo -n "$2"
  fi
}

# Checks for `.pyenv` file, and suggests to remove it for installing
if [ -d "${PYENV_ROOT}" ]; then
  { echo
    colorize 1 "WARNING"
    echo ": Can not proceed with installation. Kindly remove the '${PYENV_ROOT}' directory first."
    echo
  } >&2
    exit 1
fi

shell="$1"
if [ -z "$shell" ]; then
  shell="$(ps c -p "$PPID" -o 'ucomm=' 2>/dev/null || true)"
  shell="${shell##-}"
  shell="${shell%% *}"
  shell="$(basename "${shell:-$SHELL}")"
fi

failed_checkout() {
  echo "Failed to git clone $1"
  exit -1
}

checkout() {
  [ -d "$2" ] || git clone --depth 1 "$1" "$2" || failed_checkout "$1"
}

if ! command -v git 1>/dev/null 2>&1; then
  echo "pyenv: Git is not installed, can't continue." >&2
  exit 1
fi

if [ -n "${USE_GIT_URI}" ]; then
  GITHUB="git://github.com"
else
  GITHUB="https://github.com"
fi

checkout "${GITHUB}/pyenv/pyenv.git"            "${PYENV_ROOT}"
checkout "${GITHUB}/pyenv/pyenv-doctor.git"     "${PYENV_ROOT}/plugins/pyenv-doctor"
checkout "${GITHUB}/pyenv/pyenv-installer.git"  "${PYENV_ROOT}/plugins/pyenv-installer"
checkout "${GITHUB}/pyenv/pyenv-update.git"     "${PYENV_ROOT}/plugins/pyenv-update"
checkout "${GITHUB}/pyenv/pyenv-virtualenv.git" "${PYENV_ROOT}/plugins/pyenv-virtualenv"
checkout "${GITHUB}/pyenv/pyenv-which-ext.git"  "${PYENV_ROOT}/plugins/pyenv-which-ext"

if ! command -v pyenv 1>/dev/null; then
  { echo
    colorize 1 "WARNING"
    echo ": seems you still have not added 'pyenv' to the load path."
    echo
  } >&2

  case "$shell" in
  bash )
    profile="~/.bashrc"
    ;;
  zsh )
    profile="~/.zshrc"
    ;;
  ksh )
    profile="~/.profile"
    ;;
  fish )
    profile="~/.config/fish/config.fish"
    ;;
  * )
    profile="your profile"
    ;;
  esac

  { echo "# Load pyenv automatically by adding"
    echo "# the following to ${profile}:"
    echo
    case "$shell" in
    fish )
      echo "set -x PATH \"${PYENV_ROOT}/bin\" \$PATH"
      echo 'status --is-interactive; and . (pyenv init -|psub)'
      echo 'status --is-interactive; and . (pyenv virtualenv-init -|psub)'
      ;;
    * )
      echo "export PATH=\"${PYENV_ROOT}/bin:\$PATH\""
      echo "eval \"\$(pyenv init -)\""
      echo "eval \"\$(pyenv virtualenv-init -)\""
      ;;
    esac
  } >&2
fi
```

- 追加python下的 .bash_profile 文件

```shell
# Load pyenv automatically by adding
# the following to your profile:

export PATH="/home/python/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

- 启用更新

```shell
. .bash_profile
```

- python版本

```shell
[python@localhost ~]$ python -V
Python 2.6.6
```

- crt 上传下载工具安装

```shell
yum -y install lrzsz
```

- pyenv 安装python3.5.3

```shell
cd /home/python/.pyenv
mkdir cache
rz 上传下载好的python安装包
pyenv install 3.5.3 -v
```

- pyenv virtualenv 创建

```shell
[python@localhost ~]$ pyenv virtualenv 3.5.3 test353
[python@localhost ~]mkdir wardtest
[python@localhost wardtest]$ pyenv local test353
(test353) [python@localhost wardtest]$ pyenv version
test353 (set by /home/python/wardtest/.python-version)
(test353) [python@localhost wardtest]$ python -V
Python 3.5.3
```

- pip 源配置

```shell
[python@localhost ~]$ mkdir .pip
[python@localhost .pip]$ vim pip.conf
[global]
index-url=https://mirrors.aliyun.com/pypi/simple/
trusted-host=mirrors.aliyun.com
```

- 虚拟环境下安装软件

```shell
(test353) [python@localhost wardtest]$ pip install ipython  //交互式python工具
(test353) [python@localhost wardtest]$ pip install jupyter   //web笔记本
```

- jupyter

```shell
[python@localhost ~]$ mkdir jupyter-test
[python@localhost ~]$ cd jupyter-test
[python@localhost jupyter-test]$ pyenv local test353
(test353) [python@localhost jupyter-test]$ pip install jupyter
(test353) [python@localhost jupyter-test]$ jupyter notebook --ip=0.0.0.0
```

- 导出/导入包

```shell
pip freeze > /tmp/packs.txt
pip install -r /tmp/packs.txt
```

## 基础语法

### 运算符

#### 算数运算符

```shell
+
-
*
/ 自然除法（3以后）
// 整除
% 取模
** 幂运算
```

#### 位运算符

```shell
& 位与
| 位或
~ 取反
^ 异或
<< 向左位移
>> 向右位移
```

##### 原码、反码、补码，负数的表示法

```shell
原码 5 0b101
        1    0b1
        -1    -0b1
反码 除符号位取反  
补码 正数是本身，负数符号位不变其余按位取反后+1
负数
```

#### 比较运算符

```shell
==
!=
<
>
<=
>=
```

#### 逻辑运算符

```shell
and 与
or  或
not 非
短路运算 前面结果决定了总的结果
```

#### 赋值运算符

```shell
a = min(3,5)
+=
-=
*=
/=
%=
```

#### 成员运算符

```shell
in
not in
```

#### 身份运算符

```shell
is
is not
```

#### 优先级

#### 表达式

- 算数表达式
- 逻辑表达式
- 赋值表达式

### 程序结构

#### 顺序

#### 分支

##### if语句

```python
a = 4
if a < 5:
    print('a is less than 5')
```

```python
a = 5
if a <4:
    print('a is less than 4')
elif a ==4 :
    print('a is 4')
    else:
    print('a is bigger than 4')
```

##### 分支嵌套if……else……if…elif……else

```python
a = 80
if a < 0 :
    print('worng')
else:
    if a == 0 :
        print('a is 0 ')
    elif a <=100:
        print('right')
    else:
        print('too big')
```

##### 给定一个不超过5位的正数，判断其几位

```python
a = int(input('>>>'))
if a >=1000:
    if a >=100000:
        print('error')
    elif a >= 10000:
        print(5)
    else:
        print(4)
else:
    if a >=100:
        print(3)
    elif a >=10:
        print(2)
    else:
        print(1)
```

#### 循环

##### while

##### for

```python
for i in range(10):
if not i%2:
    print(i)
```

##### continue

```python
for i in range(10):
if i & 1:
    continue
print(i)
```

##### break

```python
count = 0
for i in range(0,1000,7):
    print(i)
    count += 1
    if count >=20:
        break
```

##### continue\break

##### else

### 实验

#### 判断不超过5位数的位数，一次打印个十百千万位

```python
val = input('>>>')
val = int(val)
if val >=1000:
    if val>=10000:
        num = 5

    else:
        num = 4
else:
    if val >=100:
        num = 3
    elif val >= 10:
        num = 2
    else:
        num = 1
print(num)
a = val
for i in range(num):
    n= a//10
    print(a-n*10)
    a = n  
```

#### 打印一个边长位n的正方形

```python
n=int(input('>>>'))
print('*'*n)
for i in range(n-2):
    print('*'+' '*(n-2)+'*')
print('*'*n)
```

#### 求1-5的阶乘和

```python
a = 1
sum = 0
for i in range(1,6):
    a *= i
    sum += a
print(sum)
```

#### 判断一个数是不是质数

```python
num = int(input("请输入一个数字: "))

if num > 1:
   for i in range(2,num):
       if (num % i) == 0:
           print(num,"不是质数")
           print(i,"乘于",num//i,"是",num)
           break
   else:
       print(num,"是质数")
else:
   print(num,"不是质数")
```

#### 打印九九乘法表

```python
#正三角
for i in range(1,10):
    line = ''
    for j in range(1,i+1):
        line += '{}*{}={:<2} '.format(j,i,i*j)
    print(line)
#倒三角
for i in range(1,10):
    line = ''
    for j in range(i,10):
        line += '{}*{}={:<{}}'.format(i,j,i*j,2 if j<4 else 3)
    print("{:>66}".format(line))
```

#### 打印菱形

```python
n = 10
for i in range(-n,n+1):
    if i <0:
        prespace = -i
    else:
        prespace = i
    print(' '*prespace + '*'*(2*n+1-prespace*2))
```

#### 打印对顶三角形

```python
n = 7
e = n//2

for i in range(-e,n-e):
    prespace = -i if i<0 else i
    print(' '*(e-prespace)+ '*'*(2*prespace+1))
```

#### 打印闪电

```python
for i in range(-3,4):
    if i <0:
        print(' '*(-i)+'*'*(4+i))
    elif  i >0:
        print(' '*3+'*'*(4-i))
```

#### 打印斐波那契数列

```python
#斐波那契数列由0和1开始，之后的斐波那契数就是由之前的两数相加而得出
n = 0
m = 1
print(n)
while m+n<=100:
    c = m+n
    print(c)
    m = n
    n = c
```

```python
#斐波那契的第N项
n = input('input the number: ')
n = int(n)
a = 0
b = 1
count = 0
if n <=0:
    print('false')
elif n <=2:
    if n == 1:
        print('0')
    else:
        print('1')
else:
    while not count == 101:
        c = a+b
        a = b
        b = c
        count += 1
    print(c)
```

```python
peach = 1
for _ in range(9):
    peach = 2 * (peach+1)
print(peach)
```

## 内置数据结构

- 数值型：
  - int:长整型  整数
  - float：整数部分和小数部分  浮点数
  - complex：实数和虚数  复数
  - bool：true、false 布尔值
- 序列对象：
  - 字符串str
  - 列表list
  - tuple
- 键值对：
  - 集合set
  - 字典dict
  
### 数字处理

```python
round()  #四舍六入五取偶
>>> 3//2 向下取整
1
import math
math.floor(2.5)  向下取整
math.ceil(2.9)   向上取整
math.sqrt(9)  平方根
min(1,2,5)
max(1,2,5)
pow(2,3) #x**y
#进制，返回字符串
>>> bin(10)  二进制
'0b1010'
>>> oct(10)  八进制
'0o12'
>>> hex(10)  十六进制
'0xa'

>>> math.pi
3.141592653589793
>>> math.e
2.718281828459045
```

### 类型判断

```python

>>> a = 1
>>> b = 1.2
>>> type(a)
<class 'int'>
>>> type(b)
<class 'float'>
>>> type(type(a))
<class 'type'>

>>> isinstance(4.5,str)
False
>>> isinstance(4.5,(float,int))
True

>>> 1+True+0.3
2.3
```

### list列表

#### 定义

```python
#列表list
lst = [1,2,3,4,5,6]  #定义
lst.index(1)  #索引
lst.index(1,-1)  #负索引
lst.count(1)  #计数
len(lst)  #长度
#修改
In [7]: lst[5] = 9
#增加/插入
In [11]: lst.append(10)  #尾部追加，就地修改
In [19]: lst.insert(2,5) #插入
In [33]: lst1.extend(lst) #追加列表
lst = [1,2,3]
lst1 = [1,4,6]
lst+ lst1  #列表相加
[1, 2, 3, 1, 4, 6]
2* lst1  #乘以列表
[1, 4, 6, 1, 4, 6]
#删除
In [36]: lst.remove(1)
#弹出
In [38]: lst.pop()  #随机弹出
In [40]: lst.pop(2)  #从索引处弹出  
In [43]: lst1.clear() #清空
#反转
In [47]: lst.reverse() #元素反转
#排序
In [49]: lst.sort(key=None, reverse=False) #key后接函数，reverse默认False正序
#in 判断
In [61]: a in lst #判断是否在
#复制
lst1 = lst.copy() #浅拷贝
import copy
lst2 = copy.deepcopy(lst) #深拷贝
```

```python
#random 随机数
In [1]: import random
In [2]: random.randint(1,10)  #返回之间整数
In [3]: random.choice(range(10))  #随机挑选一个
In [4]: random.randrange(1,7,2)   #首 尾 步长 指定范围取
In [66]: random.shuffle(lst) #打乱
In [8]: random.sample([1,2,3,4],2)  #取K个元素
```

#### list实验

##### 求素数

```python
#一个数能被2开始到自己的平方根的正整数整除，就是合数
import math
n = 100
for x in range(2,n):
    for i in range(2,math.ceil(math.sqrt(x))):
        if x % i == 0 :
            break
    else:
        print(x)
#方法二
for i in range(2,100):
    for j in range(2,int(i**0.5)+1):
        if i % j == 0 :
            break
    else:
        print(i)
```

```python
#合数一定可以分解成几个质数的乘积
n = 100
prime = []
for x in range(2,n):
    for i in prime:
        if x % i == 0:
            break
    else:
        print(x)
        prime.append(x)
```

```python
#将上面两种思维合并，可以优化算法
import math
prime = []
n = 100
flag = False
for x in range(2,n):
    for i in prime:
        if x % i == 0:
            flag = True
            break
        if i >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        print(x)
        prime.append(x)
```

##### 效率比较

```python
#效率比较方法
import math
import datetime
prime = []
n = 100000
start = datetime.datetime.now()
count = 0
flag = False
for x in range(2,n):
    for i in prime
        if x % i == 0:
            flag = True
            break
        if x >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        #print(x)
        prime.append(x)
        count += 1
delta = (datetime.datetime.now()- start).total_seconds()
print(delta)
print(count)
```

```python
#通过步长 优化算法
import math
import datetime
prime = []
n = 1000000
start = datetime.datetime.now()
count = 0
flag = False
for x in range(3,n,2):
    for i in prime:
        if x % i == 0:
            flag = True
            break
        if x >= math.ceil(math.sqrt(x)):
            flag = False
            break
    if not flag:
        #print(x)
        prime.append(x)
        count += 1
delta = (datetime.datetime.now()- start).total_seconds()
print(delta)
print(count)
```

##### 杨辉三角

```python
triangle = [[1],[1,1]]
for i in range(2,6):
    cur = [1]
    pre = triangle[i-1]
    for j in range(len(pre)-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
    triangle.append(cur)
print(triangle)
```

```python
#变体
triangle = []
n = 6
for i in range(n):
    cur = [1]
    triangle.append(cur)
    if i == 0:
        continue
    pre = triangle[i-1]
    for j in range(len(pre)-1):
        cur.append(pre[j]+pre[j+1])
    cur.append(1)
print(triangle)
```

```python
#变形
triangle = []
n = 6
for i in range(n):
    row = [1]
    triangle.append(row)
    if i == 0:
        continue
    for j in range(i-1):
        row.append(triangle[i-1][j]+triangle[i-1][j+1])
    row.append(1)
print(triangle)
```

```python
#补零 while实现
n = 6
newline = [1]
print(newline)
for i in range(1,n):
    oldline = newline.copy()
    oldline.append(0)
    newline.clear()
    offset = 0
    while offset <=i:
        newline.append(oldline[offset-1]+oldline[offset])
        offset += 1
    print(newline)
```

```python
#for循环实现
n = 6
newline = [1]
print(newline)
for i in range(1,n):
    oldline = newline.copy()
    oldline.append(0)
    newline.clear()
    for j in range(i+1):
        newline.append(oldline[j-1]+oldline[j])
    print(newline)
```

```python
#对称性  优化
triangle = []
n = 6
for i in range(n):
    row = [1]*(i+1)
    triangle.append(row)
    for j in range(1,i//2+1):
        val = triangle[i-1][j-1]+triangle[i-1][j]
        row[j] = val
        if i != 2*j:
            row[-j-1] = val
print(triangle)
```

```python
#单行覆盖
n = 6
row = [1]*n
for i in range(n):
    offset = n - i
    z = 1
    for j in range(1,i//2+1):
        val = z + row[j]
        row[j], z =val , row[j]
        if i != 2*j:
            row[-j-offset]= val
    print(row[:i+1])  #打印前i+1个元素
```

```python
#打印第m行第k个元素
c(m-1,k-1)=(m-1)!/((k-1)!(m-r)!)
m = 9
k = 5
n = m-1
r = k-1
d = n-r
targets = []
factorial = 1
for i in range(1,n+1):
    factorial *= i
    if i == r:
        targets.append(factorial)
    if i == d:
        targets.append(factorial)
    if i == n:
        targets.append(factorial)

print(targets[2]//(targets[0]*targets[1]))
```

##### 转置矩阵

```python
"""
1 2 3    1 4 7
4 5 6 => 2 5 8
7 8 9    3 6 9
"""
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix)
for i,row in enumerate(matrix):
    for j,col in enumerate(row):
        if i < j :
            temp = matrix[i][j]
            matrix[i][j] = matrix[j][i]
            matrix[j][i] = temp
print(matrix)
```

```python
"""
1 2 3      1 4
4 5 6 >>>  2 5
           3 6
"""
#算法1
matrix = [[1,2,3],[4,5,6]]
tm = []
for row in matrix:
    for i,col in enumerate(row):
        if len(tm) < i + 1:
            tm.append([])

        tm[i].append(col)

print(tm)
#算法二
matrix = [[1,2,3],[4,5,6]]
tm = [[0 for col in range(len(matrix))] for row in range(len(matrix[0]))]

for i,row in enumerate(tm):
    for j,col in enumerate(row):
        tm[i][j] = matrix[j][i]

print(tm)
```

##### 数字统计

```python
#随机产生10个数字，数字范围[1,20]，统计重复的数字有几个，分别是什么，统计不重复的数字有几个，分别是哪些。
import random

nums = []
for _ in range(10):
    nums.append(random.randrange(21))

print('Origin numbers = {}'.format(nums))
print()

length = len(nums)
samenums = []
diffnums = []
states = [0]*length

for i in range(length):
    flag = False
    if states[i] == 1:
        continue
    for j in range(i+1,length):
        if states[j] == 1:
            continue
        if  nums[i] == nums[j]:
            flag = True
            states[j] = 1
    if flag:
        samenums.append(nums[i])
        states[i] = 1
    else:
        diffnums.append(nums[i])

print('same numbers = {1},counter ={0}'.format(len(samenums),samenums))
print('diffnums numbers = {1},counter = {0}'.format(len(diffnums),diffnums))
print(list(zip(states,nums)))
```

### tuple元组

#### tuple的定义

```python
In [1]: t = tuple()
In [3]: t = ()
In [5]: t = tuple(range(1,7,2))
In [7]: t = (1,)        #一个元素的元组
#元组的乘
In [9]: t*5
Out[9]: (1, 1, 1, 1, 1)
In [11]: t = (1,2,3)*6
In [12]: t
Out[12]: (1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3)
In [15]: t = (1,[1,1],4)
In [16]: t[1][0] #元组索引
In [17]: t[1][0] = 10 #元组更改
#元组查询
In [9]: t.index(1,0,2)  #查找元素，开始，结束
In [11]: t.count(1) #返回匹配次数
In [12]: len(t) #返回元素个数
#元组为只读对象，所以没有增改删选项
```

##### 命名元组namedtuple

```python
from collections import namedtuple
Point = namedtuple('_Point',['x','y'])
p = Point(11,22)
print(p.x,p.y)

Student = namedtuple('Student','name age')  #后面的student仅为名称
tom = Student('tom',20)
jerry = Student('jerry',18)
print(tom.name,tom.age)
```

#### tuple实验

##### 接收三个数比较大小

```python
#if else
nums = []
for i in range(3):
    nums.append(int(input('{}:'.format(i))))  #字符串格式化
if nums[0]>nums[1]:
    if nums[0]>nums[2]:
        i3 = nums[0]
        if nums[1]>nums[2]:
            i2 = nums[1]
            i1 = nums[2]
        else:
            i2 = nums[2]
            i1 = nums[1]
    else:
        i2 = nums[0]
        i3 = nums[2]
        i1 = nums[1]
else:
    if nums[0]>nums[2]:
        i3 = nums[1]
        i2 = nums[0]
        i1 = nums[2]
    else:
        if nums[1]<nums[2]:
            i1 = nums[0]
            i2 = nums[1]
            i3 = nums[2]
        else:
            i1 = nums[0]
            i2 = nums[2]
            i3 = nums[1]
print(i1,i2,i3)
```

```python
#改进
nums = []
out = None
for i in range(3):
    nums.append(int(input('{}: '.format(i))))
if nums[0]>nums[1]:
    if nums[0]>nums[2]:
        if nums[1]>nums[2]:
            out = [2,1,0]
        else:
            out = [1,2,0]
    else:
        out = [1,0,2]
else:
    if nums[0]>nums[2]:
        out = [2,0,1]
    else:
        if nums[1]<nums[2]:
            out = [0,1,2]
        else:
            out = [0,2,1]
out.reverse()
for i in out:
    print(nums[i],end=' ')
```

```python
#min函数
nums = []
out = None
for i in range(3):
    nums.append(int(input('{}: '.format(i))))
while True:
    cur = min(nums)
    print(cur)
    nums.remove(cur)
    if len(nums) == 1:
        print(nums[0],end=' ')
        break
```

```python
#sort实现
nums = []
for i in range(3):
    nums.append(int(input('{}: '.format(i))))
nums.sort()
print(nums)
```

##### 冒泡法

```python
numlist = [
    [1,8,4,5,6,7,2,3,9],
    [1,2,3,4,5,6,7,8,9]
]
nums = numlist[0]
print(nums)
length = len(nums)
for i in range(length):
    for j in range(length-i-1):
        if nums[j]>nums[j+1]:
            nums[j],nums[j+1] = nums[j+1],nums[j]
print(nums)
```

### 字符串

#### 字符串定义

```python
In [1]: s1 = 'string' #字符串定义
In [5]: s3 = r'hello \n' #原始字符串
In [11]: sql = """select * from user where name='tom' """
In [12]: sql
Out[12]: "select * from user where name='tom' "
In [26]: sql[1] #字符串索引
In [31]: for c in sql:
    ...:     print(c) #有序的字符集合
In [33]: lst = list(sql) #可迭代
#字符串连接
In [18]: a = 'dkjt'
In [19]: b = 'sdfkj'
In [20]: a+b
Out[20]: 'dkjtsdfkj'

In [24]: a = 'abcd'
In [25]: ','.join(a)
Out[25]: 'a,b,c,d'
#字符串分割  
In [31]: s1.split() #rsplit 反向切
In [32]: s1.split('s') #按分隔符分隔
In [37]: s1.split(' ',maxsplit=2) #maxsplit为分隔次数，-1为遍历
In [7]: a.partition('s') #以分隔符，分割为三部分，分隔符必须指定
In [10]: a.rpartition('s') #反向
#行切
In [40]: 'ab c\n\nde fg\rkl\r\n'.splitlines()
Out[40]: ['ab c', '', 'de fg', 'kl']   #行分隔符包括\n、\r\n、\r等
In [41]: 'ab c\n\nde fg\rkl\r\n'.splitlines(True)
Out[41]: ['ab c\n', '\n', 'de fg\r', 'kl\r\n']
#大小写切换
In [52]: s1.upper() #大
In [53]: s1.lower() #小
In [54]: s1.swapcase() #交换
#字符排版
In [55]: s1.title() #标题单词大写
In [56]: s1.capitalize() #首字符大写
In [60]: s1.center(50) #两边字符填充
In [61]: s1.zfill(50) #左面字符填充
Out[61]: "000000000000000000000000000000l'm a super student."
In [62]: s1.ljust(50) #左对齐
Out[62]: "l'm a super student.                              "
In [63]: s1.rjust(50) #右对齐
Out[63]: "                              l'm a super student."  
#字符串修改
In [64]: 'www.baidu.com'.replace('w','a')
Out[64]: 'aaa.baidu.com'
In [65]: 'www.baidu.com'.replace('w','a',2)
Out[65]: 'aaw.baidu.com'
#去除特殊字符
In [66]: s = "\r \n \t Hello Python \n \t"
In [67]: s.strip()
Out[67]: 'Hello Python'
In [1]: s = 'I am very very very sorry   '
In [4]: s.strip('Iy')
Out[4]: ' am very very very sorry   '
In [5]: s.strip('Iy ')
Out[5]: 'am very very very sorr'
In [6]: s.lstrip('I')
Out[6]: ' am very very very sorry   '
In [7]: s.rstrip('I')
Out[7]: 'I am very very very sorry   '
#字符查找
In [9]: s.find('very')
In [11]: s.find('very',5) #从5个字符开始
In [33]: s.find('very') #反向
In [15]: s.index('I') #返回位置
In [16]: s.count('y') #次数统计
#字符判断
In [18]: s.endswith('very') #判断是否是结尾
In [19]: s.startswith('I') #判断是否是开头
isalnum() #是否是字母和数字组成
isalpha() #是否是字母
isdecimal() #是否只包含十进制数字
isdigit() #是否全部数字(0~9)
isidentifier() #是不是字母和下划线开头，其他都是字母、数字、下划线
islower() #是否都是小写
isupper() #是否全部大写
isspace() #是否只包含空白字符
#字符串格式化
In [13]: "{}:{}".format('192.168.1.100',8888) #位置参数
Out[13]: '192.168.1.100:8888'
In [15]: "{server} {1}:{0}".format(8888, '192.168.1.100', server='Web Server Info : ') #关键字
Out[15]: 'Web Server Info :  192.168.1.100:8888'
In [19]: '{0[0]}.{0[1]}'.format(('ward',1)) #访问元素
Out[19]: 'ward.1'
In [26]: from collections import namedtuple #对象访问
    ...: Point = namedtuple('Point','x y')
    ...: p = Point(4,5)
    ...: "{{{0.x},{0.y}}}".format(p)
Out[26]: '{4,5}'
#对齐
^, <, > 分别是居中、左对齐、右对齐，后面带宽度， : 号后面带填充的字符，只能是一个字符，不指定则默认是用空格填充。+ 表示在正数前显示 +，负数前显示 -；  （空格）表示在正数前加空格
In [27]: '{0}*{1}={2:<2}'.format(3,2,2*3) #左对齐，用空格补齐两位
Out[27]: '3*2=6 '.
In [28]: '{0}*{1}={2:<02}'.format(3,2,2*3) #左对齐，用0补齐两位
Out[28]: '3*2=60'
In [29]: '{0}*{1}={2:>02}'.format(3,2,2*3) #右对齐，用0补齐两位
Out[29]: '3*2=06'
In [30]: '{:^30}'.format('centered') #居中，用空格补齐30为
Out[30]: '           centered           '
In [31]: '{:*^30}'.format('centered')
Out[31]: '***********centered***********'
#进制 b、d、o、x 分别是二进制、十进制、八进制、十六进制。
In [32]: "int: {0:d}; hex: {0:x}; oct: {0:o}; bin: {0:b}".format(42)
Out[32]: 'int: 42; hex: 2a; oct: 52; bin: 101010'
In [33]: "int: {0:d}; hex: {0:#x}; oct: {0:#o}; bin: {0:#b}".format(42)
Out[33]: 'int: 42; hex: 0x2a; oct: 0o52; bin: 0b101010'
In [34]: octets = [192, 168, 0, 1]
    ...: '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
Out[34]: 'C0A80001'
```

#### 字符串实验

##### 判断是几位，打印每一位数字及其重复次数

```python
#输入一个数字
#依次打印每一位数字，个十百千万
mun = ''
while True:
    num = input('input a positive number >>>').strip().lstrip('0')
    if num.isdigit():
        break
print('the length of {} is {}.'.format(num,len(num)))
#倒叙打印1
for i in range(len(num),0,-1):
    print(num[i-1],end=' ')
print()
#倒叙打印2
for i in reversed(num):
    print(i, end=' ')
print()
#负索引
for i in range(len(num)):
    print(num[-i-1],end=' ')
print()
#判断出现次数
counter = [0]*10
for i in range(10):
    counter[i]=num.count(str(i))
    if counter[i]:
        print('the count of {} is {}'.format(i,counter[i]))
print('~'*20)
#迭代字符串本身
counter = [0]*10
for x in mun:
    i = int(x)
    if counter[i] ==0:
        counter[i] = num.count(x)
        print('the count of {} is {}'.format(x,counter[i]))
print('~'*20)
#迭代字符串本身字符
counter = [0]*10
for x in num:
    i = int(x)
    counter[i] += 1
for i in range(len(counter)):
    if counter[i]:
        print(' the count of {} is {}'.format(i,counter[i]))
```

##### 输入5个数字，打印每个数字的位数，将这些数字排序打印，要求升序打印

```python
nums = []
while len(nums) < 5:
    num = input('Please input a number: ').strip().lstrip('0')
    if not num.isdigit():
        continue
    nums.append(int(num))
    print('The length of {} is {}'.format(num,len(num)))

print(nums)

#sort
lst = nums.copy()
lst.sort()
print(lst)

#冒泡法
for i in range(len(nums)):
    flag = False
    for j in range(len(nums)-i-1):
        if nums[j] > nums[j+1]:
            tmp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1]= tmp
            flag = True
    if not flag:
        break
print(nums)
```

### bytes\bytearry

#### bytes\bytearry定义

bytes 不可变字节序列

```python
In [8]: bytes([1,3,5]) #定义
In [11]: bytes('abc','utf8') #编码形式
In [8]: b'abcdef'.replace(b'f',b'k') #替换
In [9]: b'abc'.find(b'b') #查找
In [10]: bytes.fromhex('6162 09 6a 6b00') #类方法
In [12]: 'abc'.encode() #字节编码
In [13]: a='abc'.encode()
In [15]: a.decode() #字节解码
In [11]: 'abc'.encode().hex() #十六进制
In [16]: b'abcdef'[2] #索引
```

bytearry 可变字节数组

```python
In [22]: bytearray(b'abc') #定义
In [26]: bytearray(b'abcdef').replace(b'f',b'k') #将f换为k
In [27]: bytearray(b'abcdef').find(b'b') #索引
In [31]: bytearray.fromhex('6162 09 ') #十六进制编码
In [32]: bytearray('abc'.encode()).hex() #返回十六进制
In [33]: bytearray(b'abcd')[3] #索引
In [42]: b.append(97) #追加
In [44]: b.insert(1,98) #插入
In [46]: b.extend([65,66]) #追加可迭代对象
In [48]: b.remove(66) #移除
In [50]: b.pop() #弹出
In [51]: b.reverse() #反转
In [53]: b.clear() #清空

```

#### bytes\bytearry实验

##### 切片操作

```python
In [2]: 'www.ward.com'[4:8]
Out[2]: 'ward'
In [3]: 'www.ward.com'[4:-4]
Out[3]: 'ward'
In [4]: 'www.ward.com'[4:8:2] #首尾步长
Out[4]: 'wr'

```

### 封装和解构

```python
In [14]: a,b = b,a #左面封装，右面解构。元素互换
```

```python
_,[*_,val],*_ =lst #元素解构
print(val)

#例：环境变量JAVA_HOME =/usr/bin 返回变量名和路径
key,_,val = 'JAVA_HOME=/usr/nim'.partition('=')
print(key)
print(val)
```

### 集合

#### 集合定义

可变、无序、不重复、元素必须可hash、不可修改、不可索引、效率优于list

可hash的类型：数值型 int\float\complex、布尔型 True\False、字符串 string\bytes
、tuple、None、不可变类型可hash

```python
In [2]: a= set() #初始化
In [7]: c = {} #初始化
In [20]: a.add(5) #增加
In [23]: a.update(b) #合并其他集合
In [26]: a.remove(8) #删除，不存在报错
In [28]: a.discard(7)   #删除一个 若没有 不报错
In [31]: a.pop()   #弹出
In [34]: a.clear() #清空
in 、not in 判断元素是否在set中
```

```python
#并集
In [44]: a.union(b) #返回新元素
In [45]: a|b #等同上
In [46]: a.update(b) #就地修改
In [51]: a |= b #同上
#交集
In [55]: a.intersection(b) #返回交集
In [56]: a&b
In [57]: a.intersection_update(b) #就地修改
In [59]: a&=b
#差集：属于前者不属于后者
In [65]: a.difference(b) #返回差集
In [67]: a-b
In [68]: a.difference_update(b) #就地修改
In [71]: a-=b
#对称差集：不属于两者
In [75]: a.symmetric_difference(b) #对称差集
In [76]: a^b
In [77]: a.symmetric_difference_update(b) #就地修改
In [80]: a^=b
#集合运算
In [3]: a.issubset(b) #判断当前集合是否是后面的子集
In [5]: b<=a #同上
In [6]: b<a #判断前面的是不是后面的真子集
In [9]: a.issuperset(b) #判断前面的是否是后面的超集
In [7]: a >= b
In [7]: a > b #判断前面的是否是后面的真超集
In [10]: a.isdisjoint(b) #判断是否有交集 没有返回True
```

#### 集合练习

##### 选择排序

```python
#简单的选择排序1
m_list = [
    [1,9.8,5,6,7,4,3,2],
    [1,2,3,4,5,6,7,8,9],
    [9,8,7,6,5,4,3,2,1]
]
nums = m_list[1]
length = len(nums)
print(nums)

count_swap = 0
count_iter = 0

for i in range(length):
    maxindex = i
    for j in range(i+1,length):
        count_iter += 1
        if nums[maxindex] < nums[j]:
            maxindex = j

    if i!= maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        count_swap += 1

print(nums,count_swap,count_iter)
#算法二
m_list = [
    [1, 9.8, 5, 6, 7, 4, 3, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
]
nums = m_list[1]
length = len(nums)
print(nums)

count_swap = 0
count_iter = 0

for i in range(length//2):
    maxindex = i
    minindex = -i-1
    minorigin = minindex
    for j in range(i+1,length-i):
        count_iter +=1
        if nums[maxindex]<nums[j]:
            maxindex = j
        if nums[minindex]>nums[-j-1]:
            minindex = -j-1

    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        count_swap += 1

        if  i == minindex or i == length + minindex:
            minindex = maxindex

    if minorigin != minindex:
        tmp = nums[minorigin]
        nums[minorigin] = nums[minindex]
        nums[minindex] = tmp
        count_swap +=1

print(nums,count_swap,count_iter)
#算法三
m_list = [
    [1, 9.8, 5, 6, 7, 4, 3, 2],
    [1, 2, 3, 4, 5, 6, 7, 8, 9],
    [9, 8, 7, 6, 5, 4, 3, 2, 1]
]
nums = m_list[2]
length = len(nums)
print(nums)

count_swap = 0
count_iter = 0

for i in range(length//2):
    maxindex = i
    minindex = -i-1
    minorigin = minindex
    for j in range(i+1,length-i):
        count_iter +=1
        if nums[maxindex]<nums[j]:
            maxindex = j
        if nums[minindex]>nums[-j-1]:
            minindex = -j-1
    if nums[maxindex] == nums[minindex]:
        break

    if i != maxindex:
        tmp = nums[i]
        nums[i] = nums[maxindex]
        nums[maxindex] = tmp
        count_swap += 1

        if  i == minindex or i == length + minindex:
            minindex = maxindex

    if minorigin != minindex:
        tmp = nums[minorigin]
        nums[minorigin] = nums[minindex]
        nums[minindex] = tmp
        count_swap +=1

print(nums,count_swap,count_iter)

```

### 字典

#### 字典定义

可变、无序、key不重复

```python
In [1]: d = {'a':1,'b':2} #定义
#元素访问
In [2]: d['a'] #不存在报error
In [3]: d.get('a') #不存在返回缺省值
In [4]: d.setdefault('a') #不存在添加
#增加与修改
In [5]: d['c'] =3 #存在修改 不存在添加
In [7]: d.update(a) #不存在添加 存在覆盖
#删除
In [9]: d.pop('a') #存在移除 不存在返回默认（不存在报错）
In [10]: d.popitem() #返回任意一个
In [11]: d.clear() #清空
#遍历
In [13]: for k in d.keys(): #遍历keys
    ...:     print(k)

In [15]: for v in d.values(): #遍历values
    ...:     print(v)

In [16]: for item in d.items(): #遍历items
    ...:     print(item)

#遍历的同时移除
d = dict(a=1,b=2,c='abc')
keys = []
for k,v in d.items():
    if isinstance(v,str):
        keys.append(k)
for k in keys:
    d.pop(k)
print(d)
#defaultdict   key不存在时会利用函数生成key对应的value
from collections import defaultdict
import random

d = defaultdict(list)
for k in 'abcdef':
    for i in range(random.randint(1,5)):
        d[k].append(i)

print(d)
#OrderedDict  记录输入的顺序
from collections import OrderedDict
import random

d = {'banana': 3, 'apple': 4, 'pear': 1, 'orange': 2}
print(d)
keys = list(d.keys())
random.shuffle(keys)
print(keys)
od = OrderedDict()
for key in keys:
    od[key] = d[key]
print(od)
print(od.keys())
```

##### 字典实验

###### 打印输入的数字的每一位及重复次数

```python
num = input('>>')
#first way
d = {}
for c in num:
    if not d.get(c):
        d[c] = 1
        continue
    d[c] +=1
print(d)

#second way
d = {}
for c in num:
    if c not in d.keys():
        d[c] = 1
    else:
        d[c] += 1
print(d)
#数字重复统计
import random
n = 10
nums = [0]*n
for i in range(n):
    nums[i] = random.randint(-1000,1000)
#print(nums)
t = nums.copy()
t.sort()
#print(t)

d = {}
for x in nums:
    if x not in d.keys():
        d[x] = 1
    else:
        d[x] += 1
print(d)
d1 = sorted(d.items())
print(d1)
```

###### 字符串重复统计

```python
import random
alphabet = 'abcdefghijklmopqrstuvwxyz'

words = []
for _ in range(100):
    #words.append(random.choice(alphabet)+random.choice(alphabet))
    #words.append(''.join(random.sample(alphabet,2)))
    words.append(''.join(random.choice(alphabet) for _ in range(2)))

d = {}
for x in words:
    d[x] = d.get(x,0) +1
print(d)

d1 = sorted(d.items(),reverse=True)
print(d1)
```

### 解析式 生成器

```python
#datetime
In [13]: import datetime
In [16]: d = datetime.datetime.now()
In [17]: d
Out[17]: datetime.datetime(2020, 4, 16, 15, 1, 47, 721357)

In [18]: d.weekday() #周一0
Out[18]: 3
In [20]: d.isoweekday()#周一1
Out[20]: 4
In [19]: d.year #year、month、day、hour、minute、second、microsecond
Out[19]: 2020
In [21]: d.date()
Out[21]: datetime.date(2020, 4, 16)
In [22]: d.time()
Out[22]: datetime.time(15, 1, 47, 721357)
In [23]: d.replace()
Out[23]: datetime.datetime(2020, 4, 16, 15, 1, 47, 721357)
In [24]: d.isocalendar()
Out[24]: (2020, 16, 4)
#时间格式化
In [26]: dt = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")

In [27]: print("{0:%Y}/{0:%m}/{0:%d} {0:%H}::{0:%M}::{0:%S}".format(dt))
2006/11/21 16::30::00

In [28]: dt
Out[28]: datetime.datetime(2006, 11, 21, 16, 30)
#datetime.timedelta 时间差
In [30]: d
Out[30]: datetime.datetime(2020, 4, 16, 15, 1, 47, 721357)

In [31]: d - datetime.timedelta(1)
Out[31]: datetime.datetime(2020, 4, 15, 15, 1, 47, 721357)
In [33]: datetime.timedelta(1).total_seconds()#时间差总秒数
Out[33]: 86400.0
#time.sleep(secs) 将调用线程挂起指定的秒数  
```

```python
#列表解析
In [35]: l1 = list(range(10))

In [36]: l2 = [(i+1)**2 for i in l1]

In [37]: print(l2)
[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

In [38]: print(type(l2))
<class 'list'>

In [39]:   [{x: y} for x in 'abcde' for y in range(3)]
Out[39]:
[{'a': 0},
 {'a': 1},
 {'a': 2},
 {'b': 0},
 {'b': 1},
 {'b': 2},
 {'c': 0},
 {'c': 1},
 {'c': 2},
 {'d': 0},
 {'d': 1},
 {'d': 2},
 {'e': 0},
 {'e': 1},
 {'e': 2}]

In [40]: [(i,j) for i in range(7) for j in range(20,25) if i>4 and j>23]
Out[40]: [(5, 24), (6, 24)]
```

```python
#打印九九乘法表
[print('{}*{}={:<3}{}'.format(j,i,j*i,('\n' if i == j else ' ')),end='') for i in range(1,10) for j in range (1,i+1)]
#生成ID
import random
['{:<04}.{}'.format(n,''.join([random.choice(bytes(range(97,123)).decode()) for _ in range(10)])) for n in range(1,101)]

import random
['{:<04}.{}'.format(i,''.join([chr(random.randint(97,122)) for j in range(10)])) for i in range(1,101)]

import random
import string
['{:<04}.{}'.format(i,''.join(random.choice(string.ascii_lowercase) for _ in range(0,10))) for i in range(1,101)]
```

#### 内建函数

```python
标识 id
	返回对象的唯一标识，CPython返回内存地址
哈希 hash()
	返回一个对象的哈希值
类型 type()
	返回对象的类型
类型转换
	float() int() bin() hex() oct() bool() list() tuple() dict() set() complex() bytes() bytearray()
输入 input([prompt])
	接收用户输入，返回一个字符串
打印 print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
	打印输出，默认使用空格分割、换行结尾，输出到控制台
对象长度 len(s)
	返回一个集合类型的元素个数
isinstance(obj, class_or_tuple)
	判断对象obj是否属于某种类型或者元组中列出的某个类型
	isinstance(True, int)
issubclass(cls, class_or_tuple)
	判断类型cls是否是某种类型的子类或元组中列出的某个类型的子类
	issubclass(bool, int)
绝对值abs(x) x为数值
最大值max() 最小值min()
round(x) 四舍六入五取偶，round(-0.5)
pow(x , y) 等价于 x**y
range(stop) 
	从0开始到stop-1的可迭代对象；range(start, stop[, step])从start开始到stop-1结束步长为step的可迭代对象
divmod(x, y) 等价于 tuple (x//y, x%y)
sum(iterable[, start]) 对可迭代对象的所有数值元素求和
	sum(range(1,100,2))
chr(i) 给一个一定范围的整数返回对应的字符
      p chr(97) chr(20013)
ord(c) 返回字符对应的整数
ord('a') ord('中')
sorted(iterable[, key][, reverse]) 排序
	返回一个新的列表，默认升序
	reverse是反转
	sorted([1, 3, 5], reverse=True)
	sorted({'c':1, 'b':2, 'a':1})
翻转 reversed(seq)
	返回一个翻转元素的迭代器
	list(reversed("13579"))
	for x in reversed(['c','b','a']):
  		 print(x)
    reversed(sorted({1, 5, 9}))
枚举 enumerate(seq, start=0)
    迭代一个序列，返回索引数字和元素构成的二元组
    start表示索引开始的数字，默认是0
    for x in enumerate([2,4,6,8]):
       print(x)

    for x in enumerate("abcde"):
    print(x,end=" ")
迭代器和取元素 iter(iterable)、next(iterator[, default])
    iter将一个可迭代对象封装成一个迭代器
    next对一个迭代器取下一个元素。如果全部元素都取过了，再次next会抛StopIteration异常
    it = iter(range(5))
    next(it)
    it = reversed([1,3,5])
    next(it)
拉链函数zip(*iterables)
    像拉链一样，把多个可迭代对象合并在一起，返回一个迭代器
    将每次从不同对象中取到的元素合并成一个元组
    In [6]: list(zip(range(10),range(10),range(5),range(10)))
    Out[6]: [(0, 0, 0, 0), (1, 1, 1, 1), (2, 2, 2, 2), (3, 3, 3, 3), (4, 4, 4, 4)]
        
```

##函数

#### 定义

```python
#默认参数
def add(x=4, y=5):
	return x+y
#可变参数
def add(*nums):
    sum = 0
    print(type(nums))
    for x in nums:
       sum += x
    print(sum)
#关键字可变参数
def showconfig(**kwargs):
    for k,v in kwargs.items():
    print('{} = {}'.format(k, v))
#混用
def showconfig(username, *args, **kwargs)
#keyword-only
def fn(*args, x):
def(**kwargs, x):   
def fn(*, x,y):
#解构
In [8]:  def add(x,y):
   ...:     return x+y
In [9]: add(*(4,5))
Out[9]: 9
In [10]: add(*[4,5])
Out[10]: 9
In [11]: add(*{4,9})
Out[11]: 13

In [12]: d = dict(x=5,y=6)
In [13]: add(*d)
Out[13]: 'yx'
In [14]: add(**d)
Out[14]: 11    
```

```python
#接受至少两个参数，返回最小最大值
import random
def DoubleValues(*nums):
    print(nums)
    return max(nums),min(nums)

print(*DoubleValues(*[random.randint(10,20) for _ in range(10)]))

#接受参数N，答应上三角，下三角
#上三角
def show(n):
    tail = ' '.join([str(i) for i in range(n,0,-1)])
    width = len(tail)
    for i in range(1,n):
        print('{:>{}}'.format(' '.join([str(j) for j in range(i,0,-1)]),width))
    print(tail)

show(12)

#下三角
def showtail(n):
    tail = ' '.join([str(i) for  i in range(n,0,-1)])
    print(tail)

    for i in range(len(tail)):
        if tail[i] == ' ':
            print(' '*i,tail[i+1:])

showtail(12)
```

```python
#插入排序
m_list = [
    [1,9,8,5,3,4,2,6,7],[1,2,3,4,5,6,7,8,9]
]
nums = [0] + m_list[0]  #增加哨兵位

length = len(nums)
for i in range(2,length):
    nums[0] = nums[i]   #放置哨兵
    j = i -1
    if nums[j] > nums[0]:
        while nums[j] > nums[0]:
            nums[j+1] = nums[j]
            j -= 1
        nums[j+1] = nums[0]
nums.pop(0)        
print(nums)
```

#### 作用域、返回值

```python
#返回值
"""
没有return语句，隐式调用return None
一个函数可以存在多个return语句，但是只有一条可以被执行
return语句之后的其他语句不会被执行
函数不能返回多个值
"""
def fn(x):
    for i in range(x):
        if i > 3:
            return i
    else:
        print("{} is not greater than 3".format(x))

#函数嵌套	
"""
一个函数中定义了另一个函数称为函数嵌套
内部函数不能被外部直接使用
"""
```

作用域:一个标识符的可见范围

对比

1. 作用域对比

![image-20200419163832733](python%E7%AC%94%E8%AE%B0.assets/image-20200419163832733.png)

![image-20200419163925861](python%E7%AC%94%E8%AE%B0.assets/image-20200419163925861.png)

2. 嵌套对比

![image-20200419164526977](python%E7%AC%94%E8%AE%B0.assets/image-20200419164526977.png)

```python
"""闭包
自由变量：未在本地作用域中定义的变量。
闭包：内层函数引用到了外层函数的自由变量
"""
def counter():
    c = [0]
    def inc():
        c[0] += 1
        return c[0]
    return inc

foo = counter()
print(foo(),foo())
c = 100
print(foo())
```

```python
"""
nonlocal 将变量标记为不在本地作用域定义，而在上级作用于定义，不是全局作用于定义
"""
a = 50
def counter():
   # nonlocal a 
   # a += 1
    print(a)
    count = 0 
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

foo = counter()
foo()
foo()
```

```python
"""默认作用域"""
#函数体内不改变默认值，xyz都是传入参数或者默认参数的副本，无法修改
def foo(xyz=[],u='abc',z=123):
    xyz = xyz[:]
    xyz.append(1)
    print(xyz)
    
foo()
print(1,foo.__defaults__)
foo()
print(2,foo.__defaults__)
foo([19])
print(3,foo.__defaults__)
foo([10，5])
print(4,foo.__defaults__)
#使用不可变类型默认值，如果使用缺省值就创建列表，如果传入列表就修改
def foo(xyz=None,u='abc',z=123):
    if xyz is None:
        xyz = []
    xyz.append(1)
    print(xyz)
    
foo()
print(1,foo.__defaults__)
foo()
print(2,foo.__defaults__)
foo([19])
print(3,foo.__defaults__)
foo([10，5])
print(4,foo.__defaults__)
```

```python
"""函数销毁"""
#全局函数
def foo(xyz=[],u='abc',z=123):
    xyz.append(1)
    return xyz

print(foo(),id(foo),foo.__defaults__)#覆盖
def foo(xyz=[],u='abc',z=123):
    xyz.append(1)
    return xyz

print(foo(),id(foo),foo.__defaults__)
del foo								#删除
print(foo(),id(foo),foo.__defaults__)
#局部函数
def foo(xyz=[],u='abc',z=123):
    xyz.append(1)
    def inner(a=10):
        pass
    print(inner)
    def inner(a=100):	#覆盖
        print(xyz)
    print(inner)
    return inner 

bar = foo()
print(id(foo),id(bar),foo.__defaults__,bar.__defaults__)
del bar							#删除函数名称，函数应用计数减一				
print(id(foo),id(bar),foo.__defaults__,bar.__defaults__)
```

#### 树

1. 树

   1. 非线性结构，每个元素有多个前驱和后继
   2. N个元素的集合
      1. n=0 空树
      2. 树的根root 没有前驱
      3. 除了根，其余元素只有一个前驱
   3. 概念
      1. 结点：树中的数据元素
      2. 度degree：结点拥有的子树的数目最大值，d(v)
      3. 叶子结点：结点的度为0,
      4. 分子结点：结点度不为0
      5. 分支：结点之间的关系
      6. 内部结点：除根之外的分支结点，也不包括叶子结点
      7. 孩子结点：结点的子树的根结点
      8. 双亲结点：各子树的根结点
      9. 兄弟结点：相同双亲结点的结点
      10. 祖先结点：根结点到该结点所经过的所有结点
      11. 子孙节点：结点的所有子树上的结点
      12. 结点的层次：根节点第一层以此类推，L(v)
      13. 树的深度depth：层次最大值
      14. 堂兄弟：双亲在同一层
      15. 有序树：结点的子树是顺序的
      16. 无序树：结点的子树是无序的
      17. 路径：一条线串下来，前一个都是后一个的前驱
      18. 路径长度：路径上的结点数-1，也是分子数
      19. 森林：m棵不想交的数的集合
          1. 对于子树而言，其子树的集合就是森林
   4. 树的特点
      1. 唯一各根
      2. 子树不想交
      3. 双亲比孩子结点层次小1

2. 二叉树

   1. 每个结点最多两棵树
   2. 是有序树
   3. 五种基本形态

      1. 空二叉树
      2. 只有一个根结点
      3. 根结点只有左树
      4. 根结点只有右树
      5. 根结点只有左子树和右子树
   4. 斜树

      1. 左斜树
      2. 右斜树
   5. 满二叉树

      1. 所有分支结点都存在左子树和右子树，并且所有叶子结点只存在最下面一层
      2. 同样深度二叉树中，满二叉树结点最多
      3. K为深度，结点数为2^k-1
   6. 完全二叉树

      1. 二叉树的深度为K，二叉树的层次从1到K-1层的结点数都达到了最大个数，在第K层的所有结点都集中在最左边
      2. 完全二叉树由满二叉树引出
      3. 满二叉树一定是完全二叉树
      4. K为深度，结点总数最大值为2^k-1，当达到最大值时候就是满二叉树
   7. 二叉树性质

      1. 二叉树的第i层至多有2^(i-1)个结点
      2. 深度为k的二叉树，至多有2^k-1个结点
      3. 对任何一颗二叉树，其终端结点数为n0,度数为2的结点数为n2，n0=n2+1。即，叶子结点数-1等于度数为2的结点数。
      4. 深度为k的二叉树，至少有k个结点
      5. 含有n个结点的二叉树深度至多为n,最小为math.ceil(log2(n+1))
      6. 具有n 个结点的完全二叉树深度为int(log2(n+1))

#### 递归函数

```python
def foo1(b,b1=3):
    print('foo1',b,b1)
    
def foo2(c):
    foo3(c)
    print('foo2',c)
    
def foo3(d):
    print('foo3',d)
    
def main():
    print('main')
    foo1(100,101)
    foo2(200)
    print('main ending')
    
main()
```

```python
#斐波拉契数列
import datetime
# Fib Seq
start = datetime.datetime.now()
pre = 0
cur = 1 # No1
print(pre, cur, end=' ')
n = 35
# loop
for i in range(n-1):
    pre, cur = cur, pre + cur
    print(cur, end=' ')
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)

# Fib Seq
start = datetime.datetime.now()
pre = 0
cur = 1 # No1
print(pre, cur, end=' ')
# recursion
def fib1(n, pre=0,cur=1):
    pre, cur = cur, pre + cur
    print(cur, end=' ')
    if n == 2:
        return
    fib1(n-1, pre, cur)

fib1(n)
delta = (datetime.datetime.now() - start
         ).total_seconds()
print(delta)

start = datetime.datetime.now()
def fib2(n):
    if n < 2:
        return 1
    return fib2(n-1) + fib2(n-2)

for i in range(n):
    print(fib2(i), end=' ')
delta = (datetime.datetime.now() - start).total_seconds()
print(delta)
```

```python
#求N的阶层
def fac(n):
    if n == 1 :
        return 1
    return n*fac(n-1)

def fac1(n,p = 1):
    if n == 1 :
        return p
    p *= n
    print(p)
    fac1(n-1,p)
    return p

def fac2(n,p = None):
    if p is None:
        p = [1]
    if n == 1:
        return p[0]
    p[0] *= n
    print(p[0])
    fac2(n-1,p)
    return p

n = 10
print(fac(n))
print(fac1(n))
print(fac2(n))
```

```python
#将一个数列逆序排列
#方法一
data = str(input('>>>'))

def revert(x):
    if x == -1:
        return ''
    return data[x] + revert(x-1)

print(revert(len(data)-1))
#方法二
def revert(n,lst=None):
    if lst is None:
        lst = []
        
    x,y = divmod(n,10)
    lst.append(y)
    if x == 0:
        return lst
    return revert(x,lst)

revert(int(input('>>>')))
#方法三
num = int(input('>>>'))

def revert(num,target=[]):
    if num:
        target.append(num[len(num)-1])
        revert(num[:len(num)-1])
    return target

print(revert(str(num)))
```

```python
#猴子第一天摘下若干颗桃子，当即吃一半，有多吃了一个，第二天又将剩下的吃了一半，又吃一个，以后每天早上吃前一天剩下的一半零一个，到第十天早上吃时，只剩下一个桃子，求第一天共摘多少个桃子。
#方法一
def peach(days = 10):
    if days == 1:
        return 1
    return (peach(days-1)+1)*2

print(peach())
#方法二
def peach(days=1):
    if days ==10:
        return 1
    return (peach(days + 1)+1)*2

print(peach())

```

#### 匿名函数

```python
print((lambda :0)())
print((lambda x, y=3: x + y)(5))
print((lambda x, y=3: x + y)(5, 6))
print((lambda x, *, y=30: x + y)(5))
print((lambda x, *, y=30: x + y)(5, y=10))
print((lambda *args: (x for x in args))(*range(5)))
print((lambda *args: [x+1 for x in args])(*range(5)))
print((lambda *args: {x+2 for x in args})(*range(5)))
[x for x in (lambda *args: map(lambda x: x+1, args))(*range(5))]
[x for x in (lambda *args: map(lambda x: (x+1,args), args))(*range(5))]
```

#### 生成器

```python
#生成器
#举例1
def inc():
    for i in range(5):
        yield i
print(type(inc))
print(type(inc()))
x = inc()
print(type(x))
print(next(x))
for m in x:
    print(m,'*')
for m in x:
    print(m,'**')
    
#举例2
y = (i for i in range(5))
print(type(y))
print(next(y))
print(next(y))

#举例3
def gen():
    print('line 1')
    yield 1
    print('line 2')
    yield 2
    print('line 3')
    return 3

next(gen())
next(gen())

g = gen()
print(next(g))
print(next(g))
print(next(g))  #取完
print(next(g,'End'))

#无限循环
#对比1
def counter():
    i = 0
    while True:
        i += 1
        yield i 

def inc(c):
    return next(c)

c = counter()
print(inc(c))
print(inc(c))
1
2
#对比2
def counter():
    i = 0
    while True:
        i += 1
        yield i 

def inc(c):
    c = counter()
    return next(c)


print(inc(c))
print(inc(c))
1
1
#计数器
def inc():
   def counter():
       i=0
       while True:
          i += 1
          yield i

   c = counter()
   return lambda : next(c)
foo = inc()
print(foo())
print(foo())
#处理递归问题
def fib():
   x=0
   y=1
   while True:
       yield y
       x, y = y, x+y

foo = fib()
for _ in range(5):
   print(next(foo))

for _ in range(100):
   next(foo)
print(next(foo))
#yield from
def inc():
    for x in range(1000):
        yield x
foo = inc()
print(next(foo))
print(next(foo))
print(next(foo))
#等价于
def inc():
    yield from range(1000)
foo = inc()
print(next(foo))
print(next(foo))
print(next(foo))
```

#### 实验

```python
#字典扁平化
#源字典{'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
#目标字典{'a.c': 2, 'd.f.g': 4, 'a.b': 1, 'd.e': 3}
source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}
target = {}
def flatamp(src,prefix=''):
    for k,v in src.items():
        if isinstance(v,(list,tuple,set,dict)):
            flatamp(v,prefix=prefix+k+'.')
        else:
            target[prefix+k] = v

flatamp(source)
print(target)
#改造 dest字典可以内部或外部提供
source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}

def flatamp(src,dest=None,prefix=''):
    if dest == None:
        dest = {}
    for k,v in src.items():
        if isinstance(v,(list,tuple,set,dict)):
            flatamp(v,dest,prefix=prefix+k+'.')
        else:
            dest[prefix+k] = v
    return dest

print(flatamp(source))
#改造 不暴露给外部内部的字典
source = {'a':{'b':1,'c':2},'d':{'e':3,'f':{'g':4}}}

def faltmap(src):
    def _flatamp(src,dest=None,prefix=''):
        for k,v in src.items():
            key = prefix + k
            if isinstance(v,(list,tuple,set,dict)):
                _flatamp(v,dest,key + '.')
            else:
                dest[key] = v
        dest = {}
        _flatamp(src,dest)
        return dest

print(flatamp(source))
```

```python
#字符串base64编码
alphabet = b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
teststr = 'abcd'
teststr = 'ManMa'

def base64(src):
    ret = bytearray()
    length = len(src)
    r = 0
    for offset in range(0,length,3):
        if offset + 3 <= length:
            triple = src[offset:offset + 3 ]
        else:
            triple = src[offset:]
            r = 3 - len(triple)
            triple = triple + '\x00'*r
            
        #print(triple,r)
        b = int.from_bytes(triple.encode(),'big')
        print(hex(b))
        
        for i in range(18,-1,-6):
            if i == 18:
                index = b >> i
            else:
                index = b >> i & 0x3F
            ret.append(alphabet[index])
            
        for i in range(1,r+1):
            ret[-i] = 0x3D
    return ret

print(base64(teststr))


import base64
print(base64.b64encode(teststr.encode()))
```

```python
#求2个字符串的最大公共子串
```







































































