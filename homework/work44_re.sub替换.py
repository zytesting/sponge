'''
-*- coding: utf-8 -*-
@Author  : zy

a="张明 98分"，用re.sub，将98替换为100
'''
import re
a="张明 98分"
new=re.sub('98','100',a)
print(new)