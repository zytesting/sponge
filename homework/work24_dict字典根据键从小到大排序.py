'''
-*- coding: utf-8 -*-
@Author  : zy
字典根据键从小到大排序dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
'''
'''
dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}


newkey=sorted(dict.keys())
print(newkey)

newdict=sorted(dict.items(),key=lambda x:x[0])
print(newdict)

# for key,value in dict.items():
#     print(key,value)
#
#     keys.append(key)
#     values.append(value)
#print('所有的key为',keys)
#print('所有的value为',values)

# newkeys=sorted(keys)
# newvalues=[]
# print('排序后的key为',newkeys)
#
# newdict=[]
# for m in newkeys: 
#     newvalues.append(dict[m])
# print('各个key对应的value为',newvalues)

'''

dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}
print(sorted(list(zip(dict.keys(),dict.values()))))


#注：lambda x:x[0],表示按照第一维度，也就是key来排序。当前前提必须是一个可可遍历的列表
# new=sorted(dict.items(),key=lambda x:x[0])
# print(new)