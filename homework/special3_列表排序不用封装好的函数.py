'''
-*- coding: utf-8 -*-
@Author  : zy
列表排序，不使用封装好的函数
'''
a=[2,9,4,0,1,56,43,5,90,7]

new=[]
while len(a)>0:

    m = min(a)
    new.append(m)
    a.remove(m)

print('排序后的列表为',new)
