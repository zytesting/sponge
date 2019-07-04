'''
-*- coding: utf-8 -*-
@Author  : zy

两个列表[1,5,7,9]和[2,2,6,8]合并为[1,2,2,3,6,7,8,9]
'''
a=[1,5,7,9]
b=[2,2,6,8]
#new =a+b
#a.append(b)#append是作为一个整体进行追加，结果[1, 5, 7, 9, [2, 2, 6, 8]]
a.extend(b)#extend可以将另一个集合中的元素逐一添加到列表中
print(a)
#print(new)
