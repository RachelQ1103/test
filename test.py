
——数学运算——

输入以下试试结果
1 + 2
2 - 3
3 * 4
4 / 5

求mod（余数）
5% 6

求方（2的10次方和100次方）
2 ** 10
2 ** 100

注意2**100的结果，最后会有个L，代表这是很大的数字



在运算符左右加上空格，增加程序可读性（readability）
可读性是代码很重要的衡量标准，因为「程序是给人读的，顺便可以给机器执行而已」。
一段代码编写花1小时的话，那就还有至少9小时要读它，所以漂亮整齐可读性高的代码非常重要

还有一个笑话是讲写好代码的重要性的：
「写代码时时刻设想你就是将来要来维护这坨代码的人。
最好设想你的代码会被一个挥着斧头的精神病来维护。
而且这个挥着斧头的精神病还知道你住在哪儿。 」

当然代码规范有多个指标，运算符两边空格只是其中一个。



——浮点数——

带小数点的数叫浮点数（float）
操作符两边有一个float结果会自动转换成float
输入以下试试结果
5/2
5/2.0
5.0/2

如果只有一个0可以省略，比如
5/.2
5/2.
但不要这么做，这样不好，有人喜欢这么做，因为没教好



——字符串——

单引号和双引号等价

单引号
'string'

双引号
"string"

多行字符串要用三引号，三引号可以是三个单引号也可以是三个双引号，成对出现即可
'''multi-line
string'''

"""
i
am
good
"""



——注释——

程序的注释就是程序员的笔记，写在源代码中，只有程序员能看到，编译器会删掉注释
每个语言都有自己的注释方法（这些人在想什么！！）
python的注释符号是 #，井号直到行尾的内容会被编译器忽略

也可以用三引号当做多行注释使用



——转义符——

转义符是字符串中的特殊符号，由反斜杠（backslash）开始，接另一个字符结束
常用的转义符有
还有一些别的转义符，但极少使用，对于这种东西，不必记忆，知道有这么回事就好了。
\n     # 换行
\t     # TAB（制表符）
\\     # 一个反斜杠 \
\a     # 系统警铃声，有的系统不会响

例子：
print ‘I \n am \n\n good\n'



———变量———

内置的基本数据有以下几种类型
int          整数（integer）
str           字符串    
float          浮点数
bool          布尔变量（只有两个值True或False）
None          空数据类型，表示空


为一个变量赋值就创建了一个变量
python变量没有类型，不同类型的值赋值到同一个变量


a = 1  # a是int
a = 1.1 # 是float
a = ‘good’ # string 类型
。。。

例子：
a = 10
b = 20
print a * b     # 200

s = ‘I am good’
print s



——比较运算和逻辑操作——

下面分别是 相等、不等、小于、大于、小于等于、大于等于
==
!=
<
>
<=
>=

三种逻辑操作分别是 与、或、非
and
or
not

比较运算和逻辑操作的结果都是bool（布尔值），True和False

例子：
1 == 1
1 == 2
1 != 1
1 != 2
1 < 2
1 > 2
1 <= 1
1 >= 1

1 == 1 and 2 == 2   # true
1 == 1 and 1 == 2   # false
1 == 1 or 1 == 2    # true
not 1 == 1

可以加括号来让代码直观一点
((1 == 1) and (2 == 2)) or (1 == 2)



——字符串操作——

字符串可以判断相等、判断是否包含、相加、取子字符串

例子：
# 判断相等或者包含
print 'good' == 'good'
print 'good' == 'bad'
print 'good' != 'bad'
print 'possible' in 'impossible'

# 相加
print 'very' + 'good'
print 'very ' + 'good'

# 重复（不重要，了解一下就好）
print 'ha' * 3
print 'ha ' * 3

# 得到子字符串
# 字符串相当于一个一定长度的数组，可以用数字下标访问
# 看例子，输入看看结果

# s的长度为7，但是下标是从0开始的，所以最大下标是6
s = 'iamgood'
# 在「交互式解释环境」中，直接输入变量就可以显示变量的值，无需print它
s[0]
s[1]
s[2]
#...
s[6]

# 字符串可以切片
# 语法如下
# s[开始下标:结束下标]
s[0:3]  # ‘iam'
s[1:3]  # ‘am'

# 省略下标参数意思是取到底
s[:3]   # 'iam'
s[2:]   # 'mgood'

# 下标是负数代表反着来（看看就好，不必记忆）
s[:-1]  # 'iamgoo'
s[:-2]  # 'iamgo'



———选择控制———

# 只有if
if 1 > 2:
 print 'true'

# if带else  
if 1 > 2:
 print 'true'
else:
 print 'false'

# 多个if else
if 1 > 2:
 print '1'
elif 1 > 3:
 print '2'
elif 1 > 4:
 print '3'
else:
 print None


# 例子
# 求绝对值
n = -1
if n < 0:
 n = -n

# 判断奇偶
n = 1
if n % 2 == 0:
 print 'even'
else:
 print 'odd'



——循环——

# 循环的意思是只要条件成立，就不断执行循环体的代码，语法如下

n = 1
while n < 5:
 print n
 n = n + 1

# 记得要在循环体内改变循环条件，否则循环永远不会结束


# 循环可以跳过（结束当前循环），也可以跳出（结束整个循环）
# 例子

# 这个例子是跳过偶数，所以偶数不会被执行print
# 跳过当前循环的语句是 continue
n = 1
while n < 10:
 n = n + 1
 if n % 2 == 0:
  continue
 print n

# 这个例子是结束循环，语句是 break
# 所以这段代码实际上只print了 1 2
n = 1
while n < 10:
 print n
 n = n + 1
 if n == 3:
  break

while循环还可以带一个else语句，从来没见任何人用过，就不说了。。













——变量名和函数名命名规则——

变量名和函数名只能包含 字母、_下划线或数字
并且只能以 字母和下划线开头，不能以数字开头



——function（函数）——

# 函数简单说来就是一块代码，调用函数的时候相当于调用了函数内容包含的一系列代码

# 函数定义语法如下，其中 print_star是函数名
# print '*' 是函数体（函数体就是函数里面的内容）

def print_star():
 print '*'

# 定义好函数后，调用函数的方法是  函数名()
print_star()    # 这样会打印一个 * 到屏幕


# 函数可以带参数，如下函数，带了一个参数n，参数放在括号中

def print_star(n):
 print '*' * n

# 调用如下
print_star(4)


# 函数可以有多个参数
def add(a, b):
 print a + b

add(1, 2)
add(3, 5)
add(100, 8)


# 函数可以有「返回值」，返回值的意思是函数本身是一个值，就像变量一样，它的值就是它的返回值

def add(a, b):
 return a + b

number = add(1, 3)
print number

# 注意看上面的语句，add(1, 3)被当做一个值赋值给了变量number
# 也就是说这个函数调用是一个数值，数值的值就是函数的返回值（写得很糟糕。。。）

# 例如，使用函数来求绝对值
def abs(n):
 if n < 0:
  n = -n
 reurn n

print abs(0)
print abs(-8)
print abs(3)


# 例如，使用函数检查一个数字是否是奇数（奇数对2取余数不等于0）
def isOdd(n):
 if n % 2 != 0:
  return True
 else:
  return False

print isOdd(1)
print isOdd(2)
print isOdd(3)
print isOdd(4)

# 练习，实现isEven函数，偶数返回True，奇数返回False

# 返回两个参数中较小的一个
def min(a, b):
 if a < b:
  return a
 else:
  return b

print min(1, 2)
print min(3, 2)


# 练习，实现max函数，接受两个参数，返回较大的那一个值





——list（列表）——

list（列表）是一种可以存储多个变量的类型
list（列表）和字符串一样，下标从0开始，操作也一样（用下标取元素，切片取子list）

list中可以存不同类型的任意数据（任意类型都可以存在列表中）
list 初始化如下，不同元素用逗号分隔

l1 = [5, 4, 3, 2, 1]
l2 = [1, "good", True]

# len()函数可以求list长度
print len(l1)   # 5
print len(l2)   # 3


# 用for in循环遍历list

# 下面的代码会输出列表内的所有变量
# 注意element这个变量名可以随便取，一般用i

for element in l:
 print element

# 切片语法等同于字符串


# 列表自带了一些函数，可以实现不同的功能，用法如下

# 排序，最常用的情况是按时间排序、windows资源管理器里面的文件排序等

l = [3, 2, 1]
l.sort()
print l
# 输出是 [1, 2, 3]，默认升序排序

# 列表可以添加元素
l = [1, 2]
l.append(3)
print l
l.append(3.3)
print l
l.append('good')
print l

# 列表 还可以删除、插入数据等，暂且不表


# 例子，得到列表中最小的元素
l = [6, 4, 5]
min = l[0]      # l的第一个元素赋值给min变量

# 遍历l，如果min变量的值大于元素的值，就把元素赋值给min变量
# 这样循环遍历完之后，min变量中存的就是整个list中最小的值了
for i in l:
 if min > i:
  min = i

print m


# 题目，得到列表中最大的元素
l = [1, 2, 3]
max = l[0]

# 补全剩下的代码

# 题目，得到列表中所有数字的合

# 题目，得到列表中所有数字的平均数
# 提示，len函数可以求list长度（也就是数字个数），上文有写













——练习题——

1. 实现函数 sum(n)，返回1到n的累计和，用循环实现
print sum(3)    # 6
print sum(100)  # 5050，高斯

2. 实现函数 factorial(n)，返回n的阶乘（就是从1累乘到n）
print factorial(5)  # 120

3. 写一个函数，求下面的结果，参数是n
1-2+3-4+5-6+7...n

4 写一个函数，求下面的结果，参数是n
1+2-3+4-5+6-7...n



——list and string练习题——

5. max(l) # l是一个列表，返回列表最大的元素

6. min(l) # l是一个列表，返回列表最小的元素

7. average(l) # 返回列表元素平均值

8. 翻转列表（这题有点难，要用下标交换头尾元素，不会做跳过）
l = [1, 2, 3, 4, 5]
调用reverse_list(l) 后
print l
[5, 4, 3, 2, 1]



——import——

python的精髓，就是把别人写好的功能导入使用，别人写好的模块叫库（lib），你通过import就能导入并使用

例如，要使用一些数学函数或者数学定义（比如PI和自然对数的底数e），就要导入math
import math

导入后要这样使用（格式是  模块.属性   或者  模块.函数()：
print math.pi
print math.e

# 求平方根
math.sqrt(100) # 10.0
math.sqrt(10)  # 3.1622776601683795


写程序：求两点距离，函数如下
distance(x1, y1, x2, y2)


还有什么三角函数，角度弧度转换函数，浮点数（就是带小数点的数）取整，向上向下取整等各种函数
这些库的使用方法是查看官方文档，下面就是数学库的文档，随便看看，不必细究
https://docs.python.org/2/library/math.html

为什么说不必细究呢。。

有句话叫 RTFM（Read The Fucking Manual）
但是编程最大的问题其实就是根本没文档或者没告诉你文档在哪，或者文档乱写一气根本不好用
就像一个没有说明书的电视机，并且遥控器按钮上没有文字。。
所以可以用这句话反击 I’ll RTFM if you just tell me where TFM that I’m supposed to FR is F located.

总之大部分软件的文档都糟糕至极，所以你不必现在去看python的文档。










答案


——练习题——

1. 实现函数 sum(n)，返回1到n的累计和，用循环实现
print sum(3)    # 6
print sum(100)  # 5050，高斯


python中，用range获得数字列表
>>> range(1, 5)
[1, 2, 3, 4]


注意下面的 range(1, n+1)

def sum(n):
  s = 0
  for i in range(1, n+1):
    s = s + i
  return s


2. 实现函数 factorial(n)，返回n的阶乘（就是从1累乘到n）
print factorial(5)  # 120

def factorial(n):
  s = 1
  for i in range(1, n+1):
    s = s * i
  return s


3. 写一个函数，求下面的结果，参数是n
1-2+3-4+5-6+7...n

观察规律
奇数都是+
偶数都是-

def foo(n):
  s = 0
  for i in range(1, n+1):
    if i % 2 == 1:
      s = s + i
    else:
      s = s - i
  return s

还可以写成这样，就是偶数让它为负数，不过逻辑不够直观

def foo1(n):
  s = 0
  for i in range(1, n+1):
    if i % 2 == 0:
      i = -i
    s = s + i
  return s


4 写一个函数，求下面的结果，参数是n
1+2-3+4-5+6-7...n

观察规律
除了1之外
奇数都是-
偶数都是+

答案如下
def bar(n):
  s = 0
  for i in range(1, n+1):
    if i % 2 == 0 or i == 1:
      s = s + i
    else:
      s = s - i
  return s



——list and string练习题——

5. max(l) # l是一个列表，返回列表最大的元素

思路就是用一个变量存最大值，遍历列表进行比较，如果有更大的值就赋值给变量，最终得到列表的最大值
def max(l):
  maximum = l[0]
  for i in l:
    if i > maximum:
      maximum = i
  return maximum


6. min(l) # l是一个列表，返回列表最小的元素

思路同上，自行编写


7. average(l) # 返回列表元素平均值

遍历列表，得到列表元素个数和总和
有了元素个数和总和，就有了平均值


8. 翻转列表（这题有点难，要用下标交换头尾元素，不会做跳过）
l = [1, 2, 3, 4, 5]
调用reverse_list(l) 后
print l
[5, 4, 3, 2, 1]



——import——
python的精髓，就是把别人写好的功能导入使用，别人写好的模块叫库（lib），你通过import就能导入并使用

例如，要使用一些数学函数或者数学定义（比如PI和自然对数的底数e），就要导入math
import math

导入后要这样使用（格式是  模块.属性   或者  模块.函数()：
print math.pi
print math.e

# 求平方根
math.sqrt(100) # 10.0
math.sqrt(10)  # 3.1622776601683795


写程序：求两点距离，函数如下
distance(x1, y1, x2, y2)
