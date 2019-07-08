'''
-*- coding: utf-8 -*-
@Author  : zy
'''
'''
a=(1)#int
print(type(a))

a=(1,)#tuple元组类型
print(type(a))

a=("1")
print(type(a))#str类型

list=[2,3,5,4,9,6]，从小到大排序，不许用sort，输出[2,3,4,5,6,9]

list=[2,3,5,4,9,6]

s=len(list)

for i in range(s):
    for j in range(s-i-1):
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]
#print('最终为',list）

a=10/3
#print('保留两位小数%.2f'%a)
print('保留两位小数',round(a,2))
'''
#递归求阶乘   2！，3！……

def cal(n):

    if n-1==0:

        return 1
    elif n<0:
        print('负数不能进行阶乘计算')

    else:

        return n * cal(n-1)

print(cal(5))

