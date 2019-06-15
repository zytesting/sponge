#coding:utf-8

'''
#1---set，集合实现去重

aalist=[1,3,3,56,8,90,0,2]

print(set(aalist))

#2--使用新列表来接收，用  in，not in

aalist=[1,3,3,56,8,90,0,2]

newlist=[]

for i in aalist:
    if i not in newlist:
        newlist.append(i)
#print(newlist)


#3--利用列表的index方法，只返回这个数的第一个索引，所以之后的重复数据都不会再显示
aalist=[1,3,3,56,8,90,0,2,0,17,62,25]
newlist=[]

#  #enumerate() 函数用于将一个可遍历的数据对象
# (如列表、元组或字符串)组合为一个索引序列，同时列出数据和数据下标
for index,i in enumerate(aalist):
    f=aalist.index(i)
    print('列表元素---%s，下标--%s'%(i,index))
    print('--------%s，第一个索引：%d'%(i,f))
    print('*************************')
#     if aalist.index(i) == index:
#         newlist.append(i)
# print(newlist)
'''
#4--利用列表的count方法
aalist=[1,3,3,56,8,90,0,2,0,17,62,25,0]
#print(aalist.count(0))返回每个元素出现过得总次数




#5--利用字典的key,不重复
