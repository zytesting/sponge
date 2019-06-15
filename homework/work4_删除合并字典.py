#coding:utf-8

#4、字典如何删除键和合并两个字典，合并有3种方法,#字典不支持+操作

dic1={'name':'xiao','age':19}
dic2={'sex':'男','class':'2班'}

new={}

'''
注意：dict.items(),
如果只有1个循环变量的话，那么取得是一对键值对
如果有2个循环变量的话，那么分别取key   和  value

#print(dic1.items())
for x,y in dic1.items():
    new[x]=y
for x,y in dic2.items():
    new[x]=y
print('使用items得到的新字典是',new)

'''
#2.使用dict的update方法

# dic1.update(dic2)
# print('合并后的字典为',dic1)

#3.
# dic3={'name':'xiao','age':19}
# dic4={'sex':'男','class':'2班'}

# newdict=dict(dic4,**dic3)
# print('第3种办法合并字典',newdict)

#问题2，字典如何删除键

dic3={'name':'xiao','age':19,'aaa':123}
#del(dic3['aaa'])

print('新的字典',dic3)



