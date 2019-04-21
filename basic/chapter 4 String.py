# -*- coding: utf-8 -*-

# Python3 字符串




print('')
print('')
print('================Python 字符串初始化 print==========================')
# 创建字符串，字符串类型

str1 = 'Hello World!'
str2 = "zhangchengkang"
print("str2 : ",str2)
print("type(str2) : ", type(str2))




print('')
print('')
print('================Python 字符串运算符 print==========================')
# 字符串运算符

a = "Hello "
b = "World "
print("a + b ：", a + b)
print("a * 2 ：", a * 2)
print("a[1] ：", a[1])
print("a[1:4] ：", a[1:4])  # 左闭右开
print("H in a : ","H" in a)
print("H not in a : ","H" not in a)




print('')
print('')
print('================Python 字符串方法 print==========================')
# 字符串操作

line = "a,b,c,d,e"
str4 =","
print("split : ",line.split(str4))  # 以","为分隔符截取字符串  

array = ['a', 'b', 'c', 'd', 'e']
print("join : ",str4.join(array))  # 以","为分隔符连接数组

c = " Hello World "
print("replace : ",c.replace("Hello","No Hello"))  # 用No Hello 替换Hello

print("upper : ",c.upper())  # 字符串转大写
print("lower : ",c.lower())  # 字符串转小写

print("去两端空格 :"+c.strip()+"aaaaa")  # 去两端空格
print("去头部空格 :"+c.lstrip()+"aaaaa")  # 去头部空格
print("去尾部空格 :"+c.rstrip()+"aaaaa")  # 去尾部空格


# 请注意：以上方法原字符串值都不会发生改变，只是新生成了一个字符串
d = "wo bu hui bian de o"
e = d.upper()
print("origin String : ",d)
print("new String : ",e)


print('')
print('')
print('================Python 多行字符串 print==========================')
# 多行字符串

f = """hello world.
it is a nice day."""
print(f)  # 换行

g = "hello world." + \
        "it is a nice day."
print (g)  # 不换行