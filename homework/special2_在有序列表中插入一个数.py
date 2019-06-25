#coding:utf-8
a=[2,3,5,4,4,11,0,12,13]
#print(sorted(a))
b=sorted(a)#实现有序排列
#print(b)

small=[]
big=[]
notchange=[]
tar=int(input('输入一个数'))

for i in range(len(b)):
    if b[i] >tar:
        big.append(b[i])
        #print('big列表',big)
    elif b[i] <tar:
        small.append(b[i])
        #print('small列表',small)
    else:

        print('输入的数已存在')

notchange.append(tar)

result=small+notchange+big
print('插入数后的新列表为',result)


'''
思路：
使用折半查找，先找出中间值，太难了
mid =int(len(a)/2)

中间值mid  和目标tar 比较

如果mid>tar,说明这个数应该在mid之前，区间变化为0~mid
if mid>tar：
    print(a[0:mid])
如果mid<tar,说明这个数应该在mid之后，区间变化为mid~i
如果mid=tar,说明这个数不插入

'''