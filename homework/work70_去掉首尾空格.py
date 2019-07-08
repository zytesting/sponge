'''
-*- coding: utf-8 -*-
@Author  : zy

a = "  hehheh  ",去除收尾空格
'''
import re

a = " hehheh abc "
#print(a.strip()) #去首尾空格
#print(a.lstrip())#去左空格

b=a.replace(" ","")
print(b)