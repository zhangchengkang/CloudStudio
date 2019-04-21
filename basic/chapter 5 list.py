# -*- coding: utf-8 -*-

# Python3 列表


print('')
print('')
print('================Python 列表初始化 print==========================')
# 创建列表

list1 = ['Google', 'kang', 1997, 2000]
list2 = [0,1,2,3,4,5 ]
list3 = ["a", "b", "c", "d"]
print(list1)
print(list2)
print(list3)
print(type(list1))




print('')
print('')
print('================Python 访问列表中的值 print==========================')
# 访问列表中的值

print ("list1[0]: ", list1[0])  # 列表索引从0开始
print ("list2[1:4]: ", list2[1:4])  # 前闭后开

print ("list1[0]: ", list1[-1])  #  反向索引
print ("list2[1:4]: ", list2[-4:-1])




print('')
print('')
print('================Python 列表长度 print==========================')
# 长度
print("len(list1) ： ",len(list1))




print('')
print('')
print('================Python 更新列表 print==========================')
# 更新列表
list4 = ['Google', 'kang', 1997, 2000]

print ("第三个元素为 : ", list4[2])
list4[2] = 2001
print ("更新后的第三个元素为 : ", list4[2])




print('')
print('')
print('================Python 删除列表元素 print==========================')
# 删除列表元素
list5 = ['Google', 'kang', 1997, 2000]
 
print ("原始列表 : ", list5)
del list5[2]
print ("删除第三个元素 : ", list5)




print('')
print('')
print('================Python 列表运算符 print==========================')
# 列表运算符

list6 = [0,1,2]
list7 = [3,4,5]
print("[1, 2, 3] + [4, 5, 6] : ",[1, 2, 3] + [4, 5, 6])
print("['Hi!'] * 4 : ",['Hi!'] * 4)
print("3 in [1, 2, 3] : ",3 in [1, 2, 3])
for x in [1, 2, 3]: print(x, end=" ")  # 列表迭代




print('')
print('')
print('================Python 列表方法 print==========================')
# 列表方法

a = [11, 12, 13, 12, 11]
x = [11, 12, 13, 12, 61]
b = [11, 12, 13, 12]
c = [11, 12, 13, 12]
d = [11, 12, 13, 12, 11]

print("count : ",a.count(11))  #  count(ob) 返回列表中元素 ob 出现的次数。
print("index : ",a.index(11))  #  ndex(ob) 返回列表中元素 ob 第一次出现的索引位置，如果 ob 不在 list 中会报错。

a.sort()
print("sort : ",a)  #  sort() 会将列表中的元素按照一定的规则排序

x.reverse()
print("reverse : ",x)  #  reverse() 会将列表中的元素从后向前排列。

b.append(11)
print("append : ",b)  # append(ob) 将元素 ob 添加到列表 list 的最后。也可以append(list)，相当于运算符+

c.insert(3, 'a')
print("insert : ",c)  # insert(idx, ob) 在索引 idx 处插入 ob ，之后的元素依次后移。

d.remove(11)
print("remove : ",d)  # emove(ob) 会将列表中第一个出现的 ob 删除，如果 ob 不在 list 中会报错。