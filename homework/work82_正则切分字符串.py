'''
-*- coding: utf-8 -*-
@Author  : zy

s="info:xiaoZhang 33 shandong",用正则切分字符串输出['info', 'xiaoZhang', '33', 'shandong']
'''

#按照：或者空格来切分
import re

s="info:xiaoZhang 33 shandong"
s_str=":| "
s=re.split(s_str,s)
print('切分后为',s)




