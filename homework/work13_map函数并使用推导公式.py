#coding:utf-8
a=[1,2,3,4,5]
'''
def square(x):
    s=x ** 2  #求平方数
    return s

#print(type(map(square,a)))

print(list(map(square,a)))
'''
print(list(map(lambda x:x ** 2,a)))


#推导公式看不懂，太多
