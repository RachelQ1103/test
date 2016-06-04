——变量名和函数名命名规则——

变量名和函数名只能包含 字母、_下划线或数字
并且只能以 字母和下划线开头，不能以数字开头



——function（函数）——

函数简单说来就是一块代码，调用函数的时候相当于调用了函数内容包含的一系列代码

函数定义语法如下，其中 print_star是函数名
print '*' 是函数体（函数体就是函数里面的内容）

def print_star():
 print '*'

定义好函数后，调用函数的方法是  函数名()
print_star()    
这样会打印一个 * 到屏幕


函数可以带参数，如下函数，带了一个参数n，参数放在括号中

def print_star(n):
 print '*' * n

 调用如下
print_star(4)


函数可以有多个参数
def add(a, b):
 print a + b

add(1, 2)
add(3, 5)
add(100, 8)


函数可以有「返回值」，返回值的意思是函数本身是一个值，就像变量一样，它的值就是它的返回值

def add(a, b):
 return a + b

number = add(1, 3)
print number

注意看上面的语句，add(1, 3)被当做一个值赋值给了变量number
也就是说这个函数调用是一个数值，数值的值就是函数的返回值（写得很糟糕。。。）

例如，使用函数来求绝对值
def abs(n):
 if n < 0:
  n = -n
 reurn n

print abs(0)
print abs(-8)
print abs(3)


例如，使用函数检查一个数字是否是奇数（奇数对2取余数不等于0）
def isOdd(n):
 if n % 2 != 0:
  return True
 else:
  return False

print isOdd(1)
print isOdd(2)
print isOdd(3)
print isOdd(4)

练习，实现isEven函数，偶数返回True，奇数返回False

返回两个参数中较小的一个
def min(a, b):
 if a < b:
  return a
 else:
  return b

print min(1, 2)
print min(3, 2)


练习，实现max函数，接受两个参数，返回较大的那一个值
