'''
-*- coding: utf-8 -*-
@Author  : zy

'''

import json
dict={"name":"zs","age":18,"city":"深圳","tel":"1362626627"}

#字典转为Json字符串
print(type(dict))

#print(type(json.dumps(dict)))#格式为str类型

s='[{"id": 1,"num": 1},{"id": 2,"num": 2},{"id": 3,"num": 3}]'
#print(type(s))
#print(json.loads(s))

res=json.loads(s)
#print(type(json.loads(s)))
for i in res:
    print(i["id"])