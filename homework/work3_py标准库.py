#coding:utf-8

import os,sys,re,math,datetime
#列出5个python标准库
# os：提供了不少与操作系统相关联的函数
#print('os.getcwd()的结果',os.getcwd())

path='/tmp'

nowpath=os.getcwd()
#print('当前目录为',nowpath)

#返回指定目录下的所有文件路径
dirlist=os.listdir(nowpath)
print(dirlist)

#os.path


# os.chdir(path)
# nownowpath=os.getcwd()
# print('修改后的当前目录为',nownowpath)



#print(path)
# sys:   通常用于命令行参数
#
# re:   正则匹配
#
# math: 数学运算
#
# datetime:处理日期时间
