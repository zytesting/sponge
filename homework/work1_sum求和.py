#coding:utf-8

#1.一行代码实现1--100之和,利用sum()函数求和,

#操作对象可以是集合，列表，元组

#print('1到100的和为',sum(range(1,101)))


#print(sum([1,5,9],3))
# print('元组',sum((1,5,9),5))
# print('列表',sum([1,5,9],3))
# print('集合',sum({1,5,9},10))

#目标值为13
# a=[8,9,0,11,4,7,3,2,6]
# print ('和为',sum(a))
#print (a.index(0))
target=int(input('请输入一个目标值'))

a=[8,4,0,2,9,5,3,9,6]

b=len(a)
#print(b)
for i in range(0,b-1):

    for j in range(i+1,b):

        sum=a[i]+a[j]
        # print('和为',sum)

        if  sum== target:
            print('对应的下标分别为',i,j)





