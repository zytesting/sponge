'''
-*- coding: utf-8 -*-
@Author  : zy
s = "ajldjlajfdljfddd"，去重并从小到大排序输出"adfjl"
'''
s = "ajldjlajfdljfddd"
p=[]
for i in s:
    #print(i)
    if i not in p:
        p.append(i)
print('去重后列表为',p)
print('排序后的列表',sorted(p))