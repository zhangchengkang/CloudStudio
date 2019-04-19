# -*- coding: utf-8 -*-
import sys


print('')
print('')
print('================Python 输出 print==================================================================')
print("print()可以在控制台输出哦，不信你试试看")


print('')
print('')
print('================Python 注释 print==================================================================')
# 注释
print("Hello World")

"""
第三个注释
英文双引号
"""

'''
第四个注释
英文单引号
'''


print('')
print('')
print('================Python 缩进 print==================================================================')
# 缩进
# python最具特色的就是使用缩进来表示代码块，不需要使用大括号 {}
# 缩进的空格数是可变的，但是同一个代码块的语句必须包含相同的缩进空格数。实例如下：
if True:
    print ("TRUE")
else:
    print ("FALSE")


# 以下代码最后一行语句缩进数的空格数不一致，会导致运行错误：
# 可以把注释放开试试，控制台有报错信息
'''
if True:
    print ("Answer")4
    print("TRUE")
else:
    print ("Answer")
  print("FALSE")
'''

print('')
print('')
print('================Python 多行语句 print==================================================================')
# 多行语句
# Python 通常是一行写完一条语句，但如果语句很长，我们可以使用反斜杠(\)来实现多行语句，例如：
total = "item_one " + \
        "item_two " + \
        "item_three"
print (total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
print (total)

# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：
x = 'runoob';print("HELLO");print(x)


print('')
print('')
print('================Python 不换行输出 print==================================================================')
# Print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上 end=""：(python 3才行)
print( x, end=" " )
print("World")


# import 与 from...import
'''
在 python 用 import 或者 from...import 来导入相应的模块。
将整个模块(somemodule)导入，格式为： import somemodule
从某个模块中导入某个函数,格式为： from somemodule import somefunction
从某个模块中导入多个函数,格式为： from somemodule import firstfunc, secondfunc, thirdfunc
将某个模块中的全部函数导入，格式为： from somemodule import *
'''


print('')
print('')
print('================Python import print=========================================================================')
# 导入sys模块
import sys

print ('命令行参数为:', end=" " )
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)



print('')
print('')
print('================python from print===========================================================================')
# 导入 sys 模块的 argv,path 成员
from sys import argv,path
 
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

# 命令行参数
# 很多程序可以执行一些操作来查看一些基本信息，Python可以使用-h参数查看各参数帮助信息：
# $ python -h