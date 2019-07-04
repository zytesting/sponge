#coding:utf-8
a=[1,2,3,4,5]
'''
def square(x):
    s=x ** 2  #求平方数
    return s

#print(type(map(square,a)))

print(list(map(square,a)))

'''
newlist=list(map(lambda x:x ** 2,a))

#print('列表平方后的新列表为',newlist)

#推导公式求出大于10的数，并输出
res=[i for i in newlist if i >10]

print('大于10的数组成的新列表',res)

