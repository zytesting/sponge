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

#使用冒泡排序算法实现，不使用sort函数，已验证，可行。
list=[2,3,5,4,9,6]

s=len(list)

for i in range(s):
    for j in range(s-i-1):
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
print('最终为',list)

