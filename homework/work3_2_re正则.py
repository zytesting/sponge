#coding:utf-8

import re
'''
#re正则表达式
#1---re.match()函数,如果没找到，则返回None
    只从起始位置开始匹配，后边不匹配

#print(re.match('com', 'runwwwoob.com'))

print(re.match('com', 'www.runoob.com'))

#2--re.search(),扫描整个字符串并返回第一个成功的匹配。

print(re.search('aa','www.abc.aa.com'))#结果：（8，10）

#re.match与re.search的区别
re.match只匹配字符串的开始，如果字符串开始不符合正则表达式，则匹配失败，
函数返回None；而re.search匹配整个字符串，直到找到一个匹配。
'''
#3.re.sub(要替换的字符串，目标字符串，完整字符串范围),检索和替换，比较实用
#eg1，检索所有注释

phone = "18877009900 # 这是一个电话号码"

# 删除注释
num = re.sub(r'#.*$', "", phone)
print("电话号码 : ", num)

