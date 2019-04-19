# -*- coding: utf-8 -*-
import math
import random

# Python 支持三种不同的数值类型：

# 整型(Int) - 通常被称为是整型或整数，是正或负整数，不带小数点。Python3 整型是没有限制大小的，可以当作 Long 类型使用，所以 Python3 没有 Python2 的 Long 类型。
# 浮点型(float) - 浮点型由整数部分与小数部分组成，浮点型也可以使用科学计数法表示（2.5e2 = 2.5 x 102 = 250）
# 复数( (complex)) - 复数由实数部分和虚数部分构成，可以用a + bj,或者complex(a,b)表示， 复数的实部a和虚部b都是浮点型。


print('')
print('')
print('================Python 数值类型 print==========================')
intNum = 10  # int
floatNum = 10.0  # float
complexNum = 3.14j  # complex

print(intNum)
print(floatNum)
print(complexNum)


print('')
print('')
print('================Python 数学常量 print==========================')
# 数学常量
print("pi : ", math.pi)
print("e : ", math.e)


print('')
print('')
print('================Python 数字类型转换 print==========================')
# Python 数字类型转换

print("int(floatNum): ", int(floatNum))  # int(x) 将x转换为一个整数。
print("float(intNum): ", float(intNum))  # float(x) 将x转换到一个浮点数。
# complex(x) 将x转换到一个复数，实数部分为 x，虚数部分为 0。
print("complex(floatNum): ", complex(floatNum))
# complex(x, y) 将 x 和 y 转换到一个复数，实数部分为 x，虚数部分为 y。x 和 y 是数字表达式。
print("complex(intNum,floatNum): ", complex(intNum, floatNum))


print('')
print('')
print('================Python type() print==========================')
# type() 查询变量所指的对象类型
print("type(intNum): ", type(intNum))
print("type(floatNum): ", type(floatNum))
print("type(complexNum): ", type(complexNum))


print('')
print('')
print('================Python 数学函数 print==========================')
# 数学函数 划重点!

a = 10
b = 20
c = -10
d = [1, 2, 5, 8, 0]
e = 3.33
print("abs(c): ", abs(c))  # 返回数字的绝对值
print("math.fabs(c): ", math.fabs(c))  # 返回数字的绝对值
print("math.ceil(e): ", math.ceil(e))  # 返回数字的上入整数
print("math.floor(e): ", math.floor(e))  # 返回数字的下舍整数
print("math.exp(1): ", math.exp(1))  # exp(x)返回e的x次幂(ex)
# log() 方法返回x的自然对数，x > 0。 如math.log(math.e)返回1.0,math.log(100,10)返回2.0
print("math.log(a): ", math.log(a))
print("math.log10(b): ", math.log10(b))  # 返回以10为基数的x的对数，如math.log10(100)返回 2.0
print("max(d): ", max(d))  # 返回给定参数的最大值，参数可以为序列。
print("min(d): ", min(d))  # 返回给定参数的最小值，参数可以为序列。
print("math.modf(e): ", math.modf(e))  # 返回x的整数部分与小数部分，两部分的数值符号与x相同，整数部分以浮点型表示。
print("math.pow(c): ", math.pow(a, b))  # a**b 运算后的值。
print("round(e): ", round(e, 1))   # 返回浮点数x的四舍五入值，如给出n值，则代表舍入到小数点后的位数。
print("round(e): ", round(e))
print("math.sqrt(a): ", math.sqrt(a))  # 返回数字x的平方根。


print('')
print('')
print('================Python 随机数函数 print==========================')
# 随机数函数 划重点!

# random.choice
print ("从列表中 [1, 2, 3, 5, 9]) 返回一个随机元素 : ", random.choice([1, 2, 3, 5, 9]))
print ("从字符串中 'Kang' 返回一个随机字符 : ", random.choice('Kang'))

# randrange ([start,] stop [,step]) 返回指定递增基数集合中的一个随机数，基数缺省值为1。
'''
start -- 指定范围内的开始值，包含在范围内。
stop -- 指定范围内的结束值，不包含在范围内。
step -- 指定递增基数。
'''
print ("从 1-99 中选取一个奇数 : ", random.randrange(1, 100, 2))
print ("从 0-99 选取一个随机数 : ", random.randrange(100))

# random() 返回随机生成的一个实数，它在[0,1)范围内。
print ("[0,1) : ", random.random())
print ("[0,10) : ", random.random()*10)

# uniform() 方法将随机生成下一个实数，它在 [x,y] 范围内。
print ("(5, 10)  : ",  random.uniform(5, 10))
print ("(7, 14)  : ",  random.uniform(7, 14))

# random.shuffle (lst)  将序列的所有元素随机排序。
list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
random.shuffle(list)
print("对 123456789随机排序 ：", list)


print('')
print('')
print('================Python 三角函数 print==========================')
# 三角函数 划重点!

# acos(x) 返回x的反余弦弧度值。
print ("acos(0) : ",  math.acos(0))
print ("acos(-1) : ",  math.acos(-1))

# asin(x) 返回x的反正弦弧度值。
print ("asin(0) : ",  math.asin(0))
print ("asin(-1) : ",  math.asin(-1))

# atan(x) 返回x的反正切弧度值。
print ("atan(0) : ",  math.atan(0))
print ("atan(10) : ",  math.atan(10))

# atan2(x ,y) 返回给定的 X 及 Y 坐标值的反正切值。
print ("atan2(5,5) : ",  math.atan2(5, 5))
print ("atan2(-10,10) : ",  math.atan2(-10, 10))

# cos(x) 返回x的弧度的余弦值。
print ("cos(3) : ",  math.cos(3))
print ("cos(-3) : ",  math.cos(-3))

# sin(x) 返回的x弧度的正弦值。
print ("sin(3) : ",  math.sin(3))
print ("sin(-3) : ",  math.sin(-3))

# tan(x) 返回 x 弧度的正切值。
print ("(tan(3) : ",  math.tan(3))
print ("tan(-3) : ",  math.tan(-3))

# hypot(x,y) 返回欧几里德范数 sqrt(x*x + y*y)
print ("hypot(3, 2) : ",  math.hypot(3, 2))
print ("hypot(-3, 3) : ",  math.hypot(-3, 3))

# degrees(x) 将弧度转换为角度。
print ("degrees(3) : ",  math.degrees(3))
print ("degrees(math.pi/2) : ",  math.degrees(math.pi/2))

# radians(x) 方法将角度转换为弧度。
print ("radians(math.pi) : ",  math.radians(math.pi))
print ("radians(3) : ",  math.radians(3))
