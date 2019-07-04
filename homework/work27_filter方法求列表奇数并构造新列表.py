'''
-*- coding: utf-8 -*-
@Author  : zy
filter方法求出列表所有奇数并构造新列表

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def cal(a):
    return a%2==1

newlist=filter(cal,a)
newnew=[]

for i in newlist:
     newnew.append(i)
print('所有奇数构成的新列表为',newnew)
'''


#2利用推导公式
a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

res=[i for i in a if i%2 == 1]

print('利用推导公式得出所有奇数构成的新列表为',res)


