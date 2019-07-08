'''
-*- coding: utf-8 -*-
@Author  : zy

统计字符串中某字符出现次数

'''
'''
s='13232wwyhbcew89208@@'

new=[]
for i in s:
    if i not in new:
        new.append(i)
        print('字符%s出现的次数为%d'%(i,s.count(i)))
        
''' 