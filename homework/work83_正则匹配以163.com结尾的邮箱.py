'''
-*- coding: utf-8 -*-
@Author  : zy

正则匹配以163.com结尾的邮箱

'''

import re

#使用re，进行查找
'''
re.split()
re.match()
re.sub()
re.search()
re.findall()
邮箱的要求

    6~18个字符，
    可使用字母、数字、下划线，
    需以字母开头。
    
^：      表示以什么开头，则^[a-zA-Z]表示以字母开头
[a-zA-Z]：任何一个a到z或A到Z的英文字母
\w：     单词字符[a-zA-Z_0-9]，即a-z或A-Z或0-9或_中的任何一个字符
{5,17}：  表示出现5到17次(至少5次，不超过17次)，则\w{5,17}表示5~17个字符。
                因为还有一个以非数字字母开头的字符，所以^[a-zA-Z]\w{5,17}表示：“6~18个字符，可使用字母、数字、下划线，需以字母开头”
@163.com：表示符合以上规则的用户名后跟上@163.com字符串，即组成一个邮箱地址。

'''
s='www.qq.com,m.ebay.com,qazr@163.com,asda12@qq.com,zy@163.aa,ss44@163.com'

email=re.match(r'^[a-zA-Z]\w{0-20}@163.com',s)

print(email)