# -*- coding: utf-8 -*-


print('')
print('')
print('================Python 算术运算符 print==========================')
# Python算术运算符
a = 21
b = 10
print("a+b: ", a+b)
print("a-b: ", a-b)
print("a*b: ", a*b)
print("a/b: ", a/b)
print("a%b: ", a % b)
print("a**b: ", a**b)
print("a//b: ", a//b)




print('')
print('')
print('================Python 比较运算符 print==========================')
# Python比较运算符
print("a==b: ", a == b)
print("a!=b: ", a != b)
print("a>b: ", a > b)
print("a<b: ", a < b)
print("a>=b: ", a >= b)
print("a<=b: ", a <= b)




print('')
print('')
print('================Python 赋值运算符 print==========================')
# Python赋值运算符
c = 2

# d += c 等效于 d = d + c
d = 0
d += c
print("c=2; d=0; d+=c; d=?; result: ", d)

# d -= c 等效于 d = d - c  （*= /= %= 都类似），可以自己敲着试试
d = 0
d -= c
print("c=2; d=0; d-=c; d=?; result: ", d)




print('')
print('')
print('================Python 位运算符 print==========================')
# Python位运算符
e = 60  # 60 = 0011 1100
f = 13  # 13 = 0000 1101
print("e&f: ", e & f)  # 按位与运算符：参与运算的两个值,如果两个相应位都为1,则该位的结果为1,否则为0
print("e|f: ", e | f)  # 按位或运算符：只要对应的二个二进位有一个为1时，结果位就为1。
print("e^f: ", e ^ f)  # 按位异或运算符：当两对应的二进位相异时，结果为1
print("~f: ",  ~ f)  # 按位取反运算符：对数据的每个二进制位取反,即把1变为0,把0变为1。~x 类似于 -x-1
print("e<<2: ",   e << 2)  # 左移动运算符：运算数的各二进位全部左移若干位，由"<<"右边的数指定移动的位数，高位丢弃，低位补0。
print("e>>2: ",  e >> 2)  # 右移动运算符：把">>"左边的运算数的各二进位全部右移若干位，">>"右边的数指定移动的位数





print('')
print('')
print('================Python 逻辑运算符 print==========================')
# Python逻辑运算符
g = 10
h = 20
i = True
j = False
print("g and h: ", g and h)  # 布尔"与"  如果 x 为 False，x and y 返回 False，否则它返回y的计算值
print("i and j: ", i and j)
print("g or h: ", g or h)  # 布尔"或"  如果 x 是 True，它返回 x 的值，否则它返回 y 的计算值。
print("i or j: ", i or j)
print("not g: ", not g)  # 布尔"非"  如果 x 为 True，返回 False。如果 x 为False, 它返回True
print("not h: ", not h)
print("not i: ", not i)
print("not j: ", not j)





print('')
print('')
print('================Python 成员运算符 print==========================')
# Python成员运算符
k = 10
m = 20
list = [3, 6, 9, 10, 15]
print("k in list: ", k in list)
print("k not in list: ", k not in list)
print("m in list: ", m in list)
print("m not in list: ", m not in list)





print('')
print('')
print('================Python 身份运算符 print==========================')
# Python身份运算符
# id() 函数用于获取对象内存地址。
# is 用于比较内存地址，==比较值
n = 20
o = 20
print("n is o: ", n is o)
print("n is not o: ", n is not o)
print("id(n): ", id(n))
print("id(o): ", id(o))
print("id(n) is id(o): ", id(n) is id(o))  # why？？？
print("id(n) == id(o): ", id(n) == id(o))


