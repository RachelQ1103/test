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
